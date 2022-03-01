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