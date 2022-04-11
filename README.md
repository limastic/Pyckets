# Pyckets

**Pyckets** est une plateforme de vente de tickets en ligne.

# Changelog : 

## V.O :
- Site affiché en se connectant en local au **serveur flask**.
- Redirection vers les autres pages du site en cliquant sur les boutons
- Pages temporaires qui seront bientot complétées
- **CSS** et **Javascript** liés au **HTML** (+ images avec `{{ url_for('static', filename='nom') }}`)
- Affichage d'une variable passable dans l'url (donc avec la méthode **GET**)
- Opérations sur les variables passées aussi dans l'url 

## V.1 : 
- Ajout de l'onglet "mon compte"
- Ajout d'un formulaire d'inscription dans cet onglet
- Récupération des données entrées dans le formulaire dans la relation Profile
- Vérification préalable de l'unicité des données (adresse email unique)

## V.2 :
- Ajout de la page "se connecter" permettant de se connecter au compte inscrit
- Gestion des mots de passes (non cryptés)
- Possibilité de se déconnecter
- Ré-organisation de la structure des templates html (jinja)

## V.3 :
- Ajout de la possibilité de créer un évènement (Si on a plus de 18 ans)
- Correction d'un bug de la v2 sur l'affichage du nom d'utilisateur
- gestion du mauvais remplissage du formulaire de création d'évènement
- création d'une relation "Events" pour les évènements
- Nécéssité d'être connecté pour creer un évènement.

# Conception

Flask est utilisé pour le serveur, SQL-Alchemy pour gérer la base de données, jinja pour les templates et pour
limiter la redondance du code  
Pour le Frontend, HTML CSS + Javascript utilisés.

Voici la hiérarchie des fichiers :

> Pyckets :
> > database :
> > > site.db
> > 
> > problèmes :
> > > Problèmes / solutions.txt
> >
> > static :
> > > assets (contient uniquement des éléments graphiques) :
> > > > img :
> > > > > events :
> > > > > > cabin.png |
> > > > > > cake.png |
> > > > > > circurs.png |
> > > > > > game.png |
> > > > > > museum.png |
> > > > > > submarine.png
> > > > >
> > > > > avataaars.svg
> > > > >
> > > > icon.png 
> >
> >  logo.png
> >
> >  script.js (script)
> >
> >  style.css (feuille de style pour le html)
> >
> > templates (fichiers html des pages du site) :
> > > index.html |
> > > social.html |
> > > soon.html |
> > > already_known.html |
> > > signup.hmtl |
> > > signedup.html |
> > > 404.html |
> > > account.html |
> > > dev.html |
> > > logged_in.html |
> > > message.html (template servant de base pour bcp d'autres) |
> > > not_logged_in.html |
> > > signin.html |
> > > succesfuly_disconnected.html |
> > > unknown_email.html |
> > > wrong_password.html |
> > > createEvent.html |
> > > eventExists.html |
> > > eventSuccesfullyCreated.html |
> > > invalidCategory.html |
> > > tooYoung.html |
> > 
> > .gitignore
> >
> > app.py (fonctions flask gérant le serveur)
> >
> > convert_birth_date.py (Fonction pour convertir une date de naissance en age)
> >
> > README.md
> >
> > requirements.txt (modules requis pour le projet)

