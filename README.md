# SoftDesk API - Application de suivi de problèmes
---
# Prérequis

- Python 3
- Environnement virtuel
- pipfile

## Comment installer l'environnement virtuel ?
Dans votre terminal :

> pip install pipenv

> pipenv shell

> pipenv install

### Pour plus de précisions : https://pypi.org/project/pipenv/

---

## Comment exécuter le serveur de l'API SoftDesk ?
Dans votre terminal :

_assurez-vous d'être à la racine de votre projet_

> cd .\softdeskproject\

Faites les migrations !

> py -m manage makemigrations

Votre terminal affichera un message pour chacune des foreignKey 
`Was comments.comment_author_user_id renamed to comments.comment_auth_user (a ForeignKey)?
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit and manually define a default value in models.py.`

Option 1
>>> 1 (ou None)

Jusqu'à ce que les migrations se lancent, puis terminez avec la commande suivante :

> py -m manage migrate

Vous pouvez lancer le serveur avec la commande suivante :

> py -m manage runserver

Vous devriez voir dans le terminal : _`Starting development server at http://127.0.0.1:1234/`_

1234 correspond au port de votre serveur local

Avant de requêter l'API SoftDesk, vous pouvez à présent continuer de suivre les instructions de la documentation sur [PostMan](https://documenter.getpostman.com/view/19936781/2s8YmGW6ZB)

Django Rest Framework possède déjà une interface web, donc vous pouvez également vous servir des instructions données sur PostMan pour requêter l'API depuis n'importe quel navigateur.

---
