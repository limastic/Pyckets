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

# Conception

Flask est utilisé pour le serveur. 

Voici la hiérarchie des fichiers :

> Pyckets
> > static
> > > assets (contient uniquement des éléments graphiques)
> > > > img
> > > > > events
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
> > templates (fichiers html des pages du site)
> > > index.html |
> > > social.html |
> > > soon.html
> >
> > .gitignore
> >
> > app.py (fonctions flask gérant le serveur)
> >
> > README.md
> >
> > requirements.txt (modules requis pour le projet)

