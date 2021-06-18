![Python 3.9](https://img.shields.io/badge/python-3.9%2B-green)
![Boto3](https://img.shields.io/badge/boto3-AWS_S3-yellow)
![GNU/GPL-V3](https://img.shields.io/badge/GNU-GPLv3-blue)
![Windows](https://img.shields.io/badge/Compatible-Windows-red)
![Linux](https://img.shields.io/badge/Compatible-Linux-white)


# Sauvegarde Automatique sur AWS S3

Dans le cadre de mon projet 6 pour ma formation, je dois développer un projet Opensources, j'ai donc décidé de faire un petit outil en Python, qui a pour but, une sauvegarde automatique, qui envoie le fichier créer au format zip sur le AWS S3.

Le script python compresse les fichiers au format zip d'un répertoire donné, il est créé dans le répertoire temporaire choisi par l'utilisateur, pour être ensuite, être envoyé dans le répertoire au nom de la machine qui est sauvegardé, comme cela, il est plus facile de retrouver les sauvegardes des machines.

Toute les opérations sont automatiques, une fois les fichiers de configuration correctement renseignés.

_________________________________________________________________________________________________________________________________________________________________________________

Pour que le projet fonctionne, il y a plusieurs prés-requis :

  - Avoir un compte amazon AWS avec un bucket de créé,
  - Avoir activé IAM de amazon AWS et autoriser le contrôle total,
  - Il y a des fichier à compléter pour la sauvegarde.

Comme vous avez un compte S3, il vous faut l'IAM.

  - Dans IAM (Identity and Access Management), il faut  créer un groupe avec les autorisations AmazonS3FullAccess
  - Dans les utilisateurs créer un utilisateur avec un accès par programmation : 
	⁃	 Activer une ID de clé d'accès et clé d'accès secrète pour AWS API, CLI, SDK et d'autres outils de développement, 
	⁃	Puis choisir le groupe créé précédemment,
	⁃	Créer une clé de Balise,
	⁃	Créer enfin l'utilisateur,
	⁃	Une fois cela fait, télécharger le fichier avec extension .CSV, il y a les codes qu'il faut pour le programme de sauvegarde

Ouvrir le fichier avec un éditeur de texte ou un tableur type LibreOffice Calc.
Le fichier contient 2 lignes, les valeurs sont séparées par des virgules, dans le logiciel de tableur, elles sont dans le tableau, il y a 2 valeurs qu'il faut afin d’exécuter la sauvegarde sur le S3 :

  - Access key ID
  - Secret access key

Ces 2 valeurs sont à copier respectivement dans ID.S3 et ACCESS_KEY.S3, pour pouvoir se connecter à S3

Mais, il y a encore des modifications à faire, deux fichiers de configuration pour le S3 et deux autres, pour la création et la sauvegarde du zip.

Les deux fichiers de configuration pour le S3 sont :

  - REGION.S3 (il faut indiquer la région AWS ou le bucket est stocké, par exemple eu-west-2)
  - BUCKET.S3 (il faut indiquer le nom que vous avez mis à la création du bucket)

Les deux fichier de configuration pour la création et l'envoi de l'archive sont :

  - REPSAVE.S3 (inscrit le répertoire à sauver)
  - COMPRESS.S3 (inscrit le répertoire temporaire)

Pour ces deux fichiers, il y a une vérification sur quel système le logiciel est exécuté, sous Linux , par exemple /home, mais pour Windows, il faut écrire avec un double "\", exemple C:\\SAUVE.

Pour le fichier configuration ARCHIVE.S3, c'est le nom que vous voulez donner à votre archive, donc nom de l'archive = nom de la machine + mot dans le fichier ARCHIVE.S3 + date.zip.

______________________________________________________________________________________________________________________________________________________________________________

### Appel et execution du script

![Appel](https://zupimages.net/up/21/24/3uit.png)

### Vérification sur le S3

![verif](https://zupimages.net/up/21/24/0mx0.png)

══════════════════════════════════════╣ Créer par Florent ╠══════════════════════════════════════
