# Programme de sauvegarde automatique
# Auteur : Florent FOVET
# Date : 06/2021
# Version v1.0.6

# Importation des modules
import platform
import os
import datetime
import boto3
import zipfile

# Nom de la machine
def pc_name():
    pcname = platform.node()
    return pcname


# Date de la machine
def date():
    now = datetime.datetime.now()
    datedef = now.strftime("%d-%m-%Y")
    return datedef


# Définition des paramèttre de fichier à compressé
def retrieve_file_paths(dirName):
    # chemins de fichiers de configuration variables
    filepaths = []
    # Lire tous les répertoires, sous-répertoires et listes de fichiers
    for root, directories, files in os.walk(dirName):
        for filename in files:
            filepath = os.path.join(root, filename)
            filepaths.append(filepath)
    return filepaths


# définition du système d'exploitation
system_exploitation = platform.system()
sys_explo = len(system_exploitation)
if sys_explo <= 5:
    sys_exp = '/'
else:
    sys_exp = '\\'

# Les variable de S3
# ID de connexion à AWS S3
id_o = open(str("ID.S3"))
ids3 = id_o.read()

# Access Key de connexion à AWS S3
ak_o = open(str("ACCESS_KEY.S3"))
ak = ak_o.read()

# Définition de la région où est le Bucket
rg_o = open(str("REGION.S3"))
rg = rg_o.read()

# Définition du bucket
bt_o = open(str("BUCKET.S3"))
bt = bt_o.read()
bt0 = str(bt + '/' + pc_name() + '/')

# Définiion du réperoire à compresser
comp_0 = open(str("COMPRESS.S3"))
sauve = comp_0.read()

# Définiion du réperoire à sauvegardé
rep_0 = open(str("REPSAUVE.S3"))
repertoire1 = rep_0.read()

# Définiion du réperoire à sauvegardé
arc_0 = open(str("ARCHIVE.S3"))
archive = arc_0.read()

# Nom du PC
print("Nom du PC : ", pc_name())

# Connexion au S3 en mod client
client = boto3.client(
    's3',
    aws_access_key_id=ids3,
    aws_secret_access_key=ak,
    region_name=rg
)

# Connexion au S3 en mod resource
resource = boto3.resource(
    's3',
    aws_access_key_id=ids3,
    aws_secret_access_key=ak,
    region_name=rg
)

# Création du fichier de sauvegarde
# Le répertoire à compressé
dir_name = repertoire1

# Appelle la fonction pour récupérer tous les fichiers et dossiers du répertoire assigné
filePaths = retrieve_file_paths(dir_name)

# Création du fichier compressé au format Zip
zip = str(pc_name() + '-' + archive + '-' + date() + '.zip')
zip_file = zipfile.ZipFile(sauve + sys_exp + zip, 'w')
with zip_file:
    # écrit chacun des fichiers par un
    for file in filePaths:
        zip_file.write(file)
    filename2 = str(zip)
    print('Le fichier ' + filename2 + ' a été créé avec succès !')

# Configuration fichers à sauvegardé
repertoire = os.fsencode(sauve)

for file in os.listdir(repertoire):
    filename1 = os.fsdecode(file)
    if filename1.endswith(".zip"):
        strg = sauve + sys_exp + filename1
        print("Envoye sur le S3 du fichier : " + strg)
        file = open(strg, 'rb')
        # Création de sous répertoire dans le Bucket
        client.put_object(
            Bucket=bt, 
            Body='', 
            Key=str(pc_name() + '/')
        )
        # Paramètre et copier du ou des fichiers et du bucket
        object1 = resource.Object(
            bt,
            pc_name() + '/' + filename1
        )
        object1.put(
            Bucket=bt,
            Body=file,
            ContentType=''
        )

    else:
        continue
