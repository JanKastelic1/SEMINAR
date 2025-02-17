from flask import Blueprint, render_template
from flask_login import login_required,current_user

views = Blueprint('views',__name__)

@views.route('/')
@login_required
def home():
    return render_template("hrbet_feed.html", user=current_user)

"""@views.route('/hrbet')
@login_required
def hrbet():
    return render_template("hrbet.html",user = current_user)

@views.route('/prsa')
@login_required
def prsa():
    return render_template("prsa.html",user = current_user)

@views.route('/noge')
@login_required
def noge():
    return render_template("noge.html",user = current_user)

@views.route('/ramena')
@login_required
def ramena():
    return render_template("ramena.html",user = current_user)

@views.route('/roke',methods = ['GET','POST'])
@login_required
def roke():
    return render_template("roke.html",user = current_user)"""

