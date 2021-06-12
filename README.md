![Python 3.9](https://img.shields.io/badge/python-3.9%2B-green)
![Boto3](https://img.shields.io/badge/boto3-AWS_S3-yellow)
![GNU/GPL-V3](https://img.shields.io/badge/GNU-GPLv3-blue)
![Windows](https://img.shields.io/badge/Compatible-Windows-red)
![Linux](https://img.shields.io/badge/Compatible-Linux-white)

# Sauvegarde Automatique sur AWS S3

Dans le cadre de mon projet 6 pour ma formation, Je dois développé un projet Opensources, j'ai décidé de faire un petit outil en Python de sauvegarde automatique qui envoie le fichier créer au format zip sur le AWS S3.

Le script python, compresse les fichiers au format zip d'un répertoire donné, il est créer dans le répertoire temporaire choisie par l'utilisateur, pour être envoyé dans le répertoire au nom de la machine qui est sauvegardé, comme cela il est plus facile de retrouvé les sauvegarde des machines.

Toute les opérations sont automatique une fois les fichier de configuration correctement rencénier

_________________________________________________________________________________________________________________________________________________________________________________

Pour que le projet fonctionne il y a plusieurs près requi :

  - Avoir un compte amazon AWS avec un buccket de créer
  - Avoir activé IAM de amazon AWS et autorisé le control total
  - Il y a des fichier à complaité pour le sauvegarde

Comme vous avez un compte S3, il vous faut le IAM.

  - Dans IAM (Identity ans Access Management), il fait créer un groupe avec les autorissation AmazonS3FullAccess
  - Dans les utilisateur créer un utilisateur 
        - Avec un Accès par programmation : Active une ID de clé d'accès et clé d'accès secrète pour AWS API, CLI, SDK et d'autres outils de développement, 
        - Puis choisir le groupe créer précédament
        - Créer une clé de Balise
        - Créer enfin l'utilisateur
  - Un fois cela fait, télécharger le fichier avec extention .CSV, il y a les code qu'il fait pour le programme de sauvegarde

Ouvrir le fichier avec un éditeur de texte ou un tableur type LibreOffice Calc.
Le fichier contient 2 ligne, les valeur sont séparé par des virgule, dans le tableur elle sont dans le tableau, il y a 2 valeur qu'il faut pour pouvoir exacuté le sauvegarde sur le S3 :

  - Access key ID
  - Secret access key

C'est 2 valeur sont à copier réspectivement dans ID.S3 et ACCESS_KEY.S3, pour pouvoir ce connecté à S3

MAis il y a encore du travail de modification à faire, il y encore deux fichiers de configuration pour le S3 et deux fichiers de configuration pour la création et lasauvegarde du du zip.

Les deux fichiers de configuration pour le S3 sont :

  - REGION.S3 (il faut indiqué la région AWS ou le bucket est stocké, par exemple eu-west-2)
  - BUCKET.S3 (il faut indiqué le nom que vous avez mis à la création du bucket)

Les deux fichier de configuration pour la création et l'envoie de l'archive sont :

  - REPSAVE.S3 (inscrir le répertoire à sauuver)
  - COMPRESS.S3 (inscrir le répertoire temporaire)

Pour ce deux fichier il y a une vérification sur quel système le logiciel est executé, mais pour Linux, on écrit simplement comme on écrit sous Linux classiquement, exemple /home, mais pour Windows, il faut écrire avec un double "\", exemple C:\\SAUVE.

Pour le fichier configuration ARCHIVE.S3, ce la nom que vous voulez donné à votre archeve, donc nom de l'archive = nom de la machine + mot dans le fichier ARCHIVE.S3 + date.zip.

