# API Dokumentacija

## Avtentikacijske poti

### Prijava
**URL:** `/login`  
**Metoda:** `POST`  
**Opis:** Avtenticira uporabnika in ga prijavi.  
**Parametri zahteve:**
- `email` (string): Uporabnikov email.
- `password` (string): Uporabnikovo geslo.

**Odgovor:**
- Uspeh: Preusmeri na domačo stran.
- Neuspeh: Prikaže sporočilo o napaki.

### Odjava
**URL:** `/logout`  
**Metoda:** `GET`  
**Opis:** Odjavi trenutnega uporabnika.  
**Odgovor:** Preusmeri na prijavno stran.

### Registracija
**URL:** `/sign-up`  
**Metoda:** `POST`  
**Opis:** Registrira novega uporabnika.  
**Parametri zahteve:**
- `email` (string): Uporabnikov email.
- `firstName` (string): Uporabnikovo ime.
- `password1` (string): Uporabnikovo geslo.
- `password2` (string): Potrditev uporabnikovega gesla.

**Odgovor:**
- Uspeh: Preusmeri na domačo stran.
- Neuspeh: Prikaže sporočilo o napaki.

## Poti za nalaganje

### Nalaganje medijev
**URL:** `/upload`  
**Metoda:** `POST`  
**Opis:** Naloži medijsko datoteko z opisom in vrsto vaje.  
**Parametri zahteve:**
- `file` (datoteka): Medijska datoteka za nalaganje.
- `description` (string): Opis medija.
- `vrsta_id` (integer): ID vrste vaje.

**Odgovor:**
- Uspeh: Preusmeri na domačo stran z uspešnim sporočilom.
- Neuspeh: Prikaže sporočilo o napaki.

## Poti za news-feed

### News Feed
**URL:** `/news-feed`  
**Metoda:** `POST`  
**Opis:** Prikaže news feed z možnostjo filtriranja po vrsti vaje.  
**Parametri zahteve:**
- `vrsta_id` (integer): ID vrste vaje za filtriranje (neobvezno).

**Odgovor:** Prikaže stran z novičarskim virom s filtriranimi objavami.

## Poti za upravljanje objav

### Brisanje objave
**URL:** `/delete-post/<int:post_id>`  
**Metoda:** `POST`  
**Opis:** Izbriše objavo in pripadajočo medijsko datoteko. Uporabnik lahko briše le svoje objave  
**Parametri zahteve:** Ni

**Odgovor:**
- Uspeh: Preusmeri na novičarski vir z uspešnim sporočilom.
- Neuspeh: Prikaže sporočilo o napaki.
