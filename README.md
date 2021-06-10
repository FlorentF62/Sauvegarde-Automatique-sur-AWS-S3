![Python 3.9](https://img.shields.io/badge/python-3.9%2B-green)
![Boto3](https://img.shields.io/badge/boto3-AWS_S3-yellow)
![GNU/GPL-V3](https://img.shields.io/badge/GNU-GPLv3-blue)

# Sauvegarde Automatique sur AWS S3

Dans le cadre de mon projet 6 pour ma formation, Je dois développé un projet Opensources, j'ai décidé de faire un petit outil en Python de sauvegarde automatique qui envoie le fichier créer au format zip sur le AWS S3.


       ___   ___        __        __    ___________
      /    \ \  \      /  \      /  /  /  _________)
     /  /\  \ \  \    /    \    /  /   |  |_______   
    /  /__\  \ \  \  /  /\  \  /  /    \_________  \
   /  ______  \ \  \/  /  \  \/  /               |  |
  /  /      \  \ \    /    \    /      __________|  |
 /__/        \__\ \__/      \__/       \___________/

Le script python, compresse les fichiers au format zip d'un répertoire donné, il est envoyé dans le répertoire temporaire choisie par l'utilisateur, pour être envoyé dans le répertoire au nom de la machine qui est sauvegardé, comme cela il est plus facile de retrouvé les sauvegarde des machines.

Pour que le projet fonctionne il y a plusieurs près requi :

  - Avoir un compte amazon AWS avec un buccket de créer
  - Avoir activé IAM de amazon AWS et autorisé le control total
  - Il y a des fichier à complaité pour le sauvegarde

Comme vous avez un compte S3, il vous faut le IAM.

  - 
