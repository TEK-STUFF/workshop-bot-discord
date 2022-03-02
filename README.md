# Workshop - Bot discord python   

[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue?style=flat-square&logo=license-gplv3)](https://choosealicense.com/licenses/gpl-3.0/)

Un petit workshop Epitech pour faire un bot discord en python !

#

## Introduction

On va utiliser le wrapper python de l'API de Discord afin de coder un début de bot et de se familiariser avec l'API   
La version "rewrite" du wrapper python sera utilisée afin de supporter les dernières fonctionnalités de Discord.
   
Différents wrappers existent pour l'API de Discord. Il n'y a pas de différence de perf majeure entre les wrappers Python, JS, C#, etc...   
   
Le but de ce workshop n'est pas de vous faire recoder MEE6 mais bien de vous montrer la puissance et le côté très accessible de l'outil.

#
## Outils   
> Python   

Afin de pouvoir réaliser ce workshop, il vous faudra une installation à jour de python (version 3.5.3 minimum). Afin de vérifier votre installation :   

`$ python3 --version`

Nous allons ensuite avoir besoin de pip pour installer les modules nécéssaires :

Ubuntu - Debian : `$ apt install python3-pip`   
Fedora - RHEL : `$ dnf install python3-pip`   
Arch - Manjaro : `$ pacman -S python3-pip`   

Une fois votre version de python et de pip à jour, nous pouvons procéder à l'installation des modules nécéssaires.

> Lib Discord   

`$ python3 -m pip install -U discord.py`   

Voilà.

Je vais donc vous laisser ouvrir votre éditeur de texte préféré, éventuellement équipé de diverses extensions pour coder en python.   

***

# Le commencement

## Création de l'application

Pour pouvoir créer votre premier bot, il faut se connecter à son compte Discord sur la page [Discord Developers](https://discord.com/login?redirect_to=%2Fdevelopers%2Fapplications).

Une fois sur le portail développeur, il vous faudra créer une nouvelle application.

![Developer Portal](./img/devportal.png)

Quelques infos vous seront demandées pour finir la création de l'application. (mettez un nom un peu marrant, histoire que vous reconnaissiez votre bot ensuite)

![App Creation](./img/botcreation.png)

Félicitations, votre application est vivante !

#

## Création d'un utilisateur "bot"

Naviguez dans le menu "Bot" dans la barre de gauche

![Bot Creation](./img/buildabot.png)

Puis cliquez sur le bouton "Add bot". Et voilà, le bot est né !

#

## Gestion des permissions

Pour l'instant, je vous recommande d'activer toutes les options des "Priviledged Gateway Intents", ça nous permettra de tester plein de choses sans être bloqués par un manque de perms. Pour un vrai bot censé partir en production c'est toujours mieux de limiter la portée des permissions au strict nécessaire

Même chose pour les "Bot Permissions" juste en dessous, des permissions administrateur permettent de ne pas être limités pendant la phase de test et de découverte.

Pensez à sauvegarder les changements, ne fermez pas la page ! (on en aura besoin plus tard)

---

# Inviter le bot sur le serveur

Maintenant que le bot est crée et mis en place correctement, nous allons pouvoir l'inviter sur notre serveur de test, que vous pouvez rejoindre [ici](https://discord.gg/kSrQajP94r).

Afin de pouvoir inviter le bot, il nous faudra creer le lien d'invitation de celui-ci. Pour cela, il faut retourner sur la page Discord Developer de notre bot, puis naviguer dans l'onglet OAuth2 sur la gauche.

![LinkGen step 1](./img/linkgen-step1.png)

Ensuite, remplissez les champs comme ci-dessus (In-App authorization, scope bot, permissions Administrator)

Encore dans le panneau de gauche, nous allons nous rendre dans "URL Generator", puis cocher quelques cases supplémentaires (promis, c'est bientôt fini)

![LinkGen step 2](./img/linkgen-step2.png)

Nous allons encore séléctionner le scope "bot", puis les permissions administrateur, pour enfin trouver notre lien tout neuf en bas de la page !

En cliquant sur celui-ci vous allez pouvoir inviter le bot sur le serveur rejoint précédemment, normalement vous avez les perms pour ça.

Si vous comptez mettre le bot sur d'autres serveurs, gardez le lien bien au chaud, ça vous évitera de devoir refaire cette étape.

## Le bot est sur le serveur, let's goooooo !

---

# Hello world

###### fichier : helloworld.py

Enfin, on va coder !

Le wrapper discord.py fonctionne sur une base de fonctions asynchrones et d'events. Pour plus d'infos, je vous invite à lire [la documentation](https://discordpy.readthedocs.io/en/stable/) et l'[API Reference](https://discordpy.readthedocs.io/en/stable/api.html).

La base de notre bot va tourner autour du "client", qui représente dans le code l'utilisateur que nous avons crée précédemment.

La déclaration du client est réalisée comme suit :

```
#!/usr/bin/env python3
#coding=utf8

import discord

client = discord.Client()
```

Sauf que là, si on lance le programme, eh bah il se passe pas grand chose :/

# Récupération du token de connexion

Pour qu'il se passe quelque chose, on va devoir aller chercher le token de notre bot sur le portail développeur

![Copy Token](./img/copytoken.png)

**ATTENTION !** : si quelqu'un trouve le moyen de récupérer ce token, cette personne aura le contrôle total de votre bot (et accessoirement des serveurs sur lesquels il se trouve) (mauvaise idée, vu qu'on l'a mis admin)

Ce token permet de prendre contrôle du bot, et de recevoir les divers events depuis l'API Discord. Cela est bien evidemment nécessaire pour pouvoir développer plein de fonctionnalités rigolotes.

Comme évoqué précedemment, il est important de garder notre token le plus caché possible. Nous allons donc utiliser le module dotenv pour nous permettre de stocker le token dans un fichier caché, séparé de notre code.

Ce fichier caché permet d'ajouter une variable d'environnement présente uniquement dans le dossier d'exécution du bot. La syntaxe est la suivante :

![Dotenv](./img/dotenvsetup.png)

Installation du module python-dotenv :

`$ pip install python-dotenv`

Une fois le module installé, nous allons pouvoir ajouter les lignes suivantes dans notre programme :

```
from dotenv import load_dotenv
from os import getenv

load_dotenv()
TOKEN = getenv('DISCORD_TOKEN')
```

Nous avons donc récupéré le token dans la variable globale *TOKEN*. Le fonctionnement peut être vérifié avec un simple `print(TOKEN)`.

Notre bot peut désormais communiquer avec l'API de Discord, il ne nous manque plus qu'à lui dire de se connecter.

Cela est effectué en ajoutant cette ligne à la toute fin du fichier (elle devra rester à la fin, car elle joue le rôle d'un "main"):

`client.run(TOKEN)`

Désormais, à l'exécution du programme, le bot apparaît avec un statut "connecté" sur le serveur !

![Online](./img/onlinebot.png)

# Mise en place du "on_ready"

Au tout début du workshop, j'ai évoqué le fonctionnement du wrapper python par évenements asynchrones. Nous allons ici coder notre premier gestionnaire d'events, le "on_ready". Cet event sera déclenché à chaque connexion du bot au service, une fois que celle-ci est effectuée et que tout est en ordre.

```
@client.event
async def on_ready() -> None :
    print(f"Je suis connecté à discord avec le compte '{client.user}' !")
    serveur = client.guilds[0]
    channel = serveur.get_channel(948344509006229504)
    if channel is not None :
        await channel.send("Bonjour discord !")
    else :
        print("Oups, je n'ai pas pu récupérer le channel")
```

On peut voir ici la syntaxe pour déclarer un gestionnaire d'évènements, ainsi que les fonctions asynchrones. Encore une fois, je vous invite à lire l'[API Reference](https://discordpy.readthedocs.io/en/stable/api.html) pour plus d'infos, et aussi pour découvrir tous les évènements disponibles pour un bot.