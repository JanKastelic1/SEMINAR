from flask import Blueprint,render_template,request,flash, redirect, url_for,Response,jsonify,Flask
import re
from .models import User,Hrbet_slike,Vrsta,Vaje
from werkzeug.security import generate_password_hash,check_password_hash
from werkzeug.utils import secure_filename
from . import db
from flask_login import login_user,login_required,logout_user,current_user
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'Website/static'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
auth = Blueprint('auth',__name__)

def check(email):

    # pass the regular expression
    # and the string into the fullmatch() method
    if(re.fullmatch(regex, email)):
        return True

    else:
        return False
    
"""@auth.template_filter('b64encode')
def b64encode_filter(data):
    return base64.b64encode(data).decode('utf-8')"""

@auth.route('/login',methods =['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email = email).first()
        if user:
            if check_password_hash(user.password,password):
                flash('Logged in successfully!',category='success')
                login_user(user,remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
            

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up',methods =['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email = email).first()
        if user:
            flash('Email already exists!', category = 'error')
        elif(check(email) != True):
            flash('Email incorrect!', category='error')
        elif len(first_name) < 2:
            flash('Name must be longer than 2 characters.',category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.',category='error')
        elif len(password1) < 12:
            flash('Password is too short.',category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1,method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user,remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("signup.html",user=current_user)



"""@auth.route('/hrbet', methods = ['GET','POST'])
@login_required
def hrbet():
    if request.method == 'POST':
        file = request.files['file']
        message= request.form.get('description')

        upload = Img(filename=file.filename, data=file.read(),message=message)
        db.session.add(upload)
        db.session.commit()

        return f'Uploaded: {file.filename}'"""
    

"""@auth.route('/hrbet', methods = ['GET','POST'])
@login_required
def hrbet():
    if request.method == 'POST':
        message= request.form.get('description')
        file = request.files['file']
        pic_filename = secure_filename(file.filename)
        vrsta_vaje = request.form.get('vrsta')

        file.save(os.path.join(UPLOAD_FOLDER,pic_filename))

        upload2 = Vrsta(ime_vaje = vrsta_vaje)
        upload3 = Vaje(opis_vaje = message,slika = pic_filename)
        upload = Hrbet_slike(filename=pic_filename,message=message)
        db.session.add(upload2,upload3)
        db.session.commit()
        db.session.add(upload3)
        db.session.commit()

        flash('Picture uploaded!', category='success')
        return render_template('hrbet_feed.html',user=current_user)


    return render_template('hrbet.html')"""

"""@auth.route('/hrbet/feed', methods = ['POST','GET'])
def news_feed():
    categories_id = request.form.get('category')
    if categories_id:
        slike = Vaje.query.filter_by(vrsta_id = categories_id).all()
    image_folder = os.path.join(app.static_folder, 'Hrbet')
    image_list = [url_for('static', filename=f'Hrbet/{img}') for img in os.listdir(image_folder)]
    result = Hrbet_slike.query.with_entities(Hrbet_slike.message)

    return render_template('hrbet_feed.html', images=image_list,user=current_user,messages=result)"""



@auth.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'POST':
        file = request.files['file']
        description = request.form.get('description')
        vrsta_id = request.form.get('vrsta_id')

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))

            new_vaje = Vaje(opis_vaje=description, slika=filename, vrsta_id=vrsta_id, user_id=current_user.id)
            db.session.add(new_vaje)
            db.session.commit()


            flash('File uploaded successfully!', category='success')
            return redirect(url_for('views.home'))
        

    vrste = Vrsta.query.all()
    return render_template('hrbet.html', user=current_user, vrste=vrste)

@auth.route('/news-feed', methods=['GET', 'POST'])
@login_required
def news_feed():
    vrsta_id = request.form.get('vrsta_id')
    vrste = Vrsta.query.all()
    if vrsta_id:
        vaje = Vaje.query.filter_by(vrsta_id=vrsta_id).all()
    else:
        vaje = Vaje.query.all()

    return render_template('hrbet_feed.html', user=current_user, vaje=vaje,Vrsta = vrste)

@auth.route('/delete-post/<int:post_id>', methods=['POST'])
@login_required
def delete_post(post_id):
    vaja = Vaje.query.get_or_404(post_id)
    if vaja.user_id != current_user.id:
        flash('You do not have permission to delete this post.', category='error')
        return redirect(url_for('auth.news_feed'))

    try:
        # Delete the file from the directory
        os.remove(os.path.join(UPLOAD_FOLDER, vaja.slika))
    except Exception as e:
        flash(f'Error deleting file: {e}', category='error')
        return redirect(url_for('auth.news_feed'))

    # Delete the post from the database
    db.session.delete(vaja)
    db.session.commit()
    flash('Post deleted successfully!', category='success')
    return redirect(url_for('auth.news_feed'))









    


    


