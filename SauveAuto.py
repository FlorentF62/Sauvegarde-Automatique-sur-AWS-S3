# Programme de sauvegarde automatique
# Auteur : Florent FOVET
# Date : 06/2021
# Version v1.0.2 Zip Extension

# Importation des modules
import platform
import os
import boto3
import zipfile


# Nom de la machine
def pc_name():
    pcname = platform.node()
    return pcname


# Définition des paramèttre de fichier à compressé
def retrieve_file_paths(dirName):
    # chemins de fichiers de configuration variables
    filePaths = []
    # Lire tous les répertoires, sous-répertoires et listes de fichiers
    for root, directories, files in os.walk(dirName):
        for filename in files:
            filePath = os.path.join(root, filename)
            filePaths.append(filePath)
    return filePaths


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
id = id_o.read()

# Access Key de connexion à AWS S3
ak_o = open(str("ACCESS_KEY.S3"))
ak = ak_o.read()

# Définition de la région où est le Bucket
rg_o = open(str("REGION.S3"))
rg = rg_o.read()

# Définition du bucket
bt_o = open(str("BUCKET.S3"))
bt = bt_o.read()

# Définiion du réperoire à sauvegardé
comp_0 = open(str("COMPRESS.S3"))
sauve = comp_0.read()

# Définiion du réperoire à compressé
rep_0 = open(str("REPSAUVE.S3"))
repertoire1 = rep_0.read()

# Nom du PC
print("Nom du PC : ", pc_name())

# Connexion au S3 en mod client
client = boto3.client(
    's3',
    aws_access_key_id = id,
    aws_secret_access_key = ak,
    region_name = rg
)

# Connexion au S3 en mod resource
resource = boto3.resource(
    's3',
    aws_access_key_id = id,
    aws_secret_access_key = ak,
    region_name = rg
)

# Création du fichier de sauvegarde
# Le répertoire à compressé
dir_name = repertoire1

# Appelle la fonction pour récupérer tous les fichiers et dossiers du répertoire assigné
filePaths = retrieve_file_paths(dir_name)

# Création du fichier compressé au format Zip
zip_file = zipfile.ZipFile(sauve + sys_exp + pc_name() + '-archive.zip', 'w')
with zip_file:
        # écrit chacun des fichiers par un
    for file in filePaths:
        zip_file.write(file)

    print('Le fichier ' + pc_name() + '-archive.zip a été créé avec succès !')

# Configuration fichers à sauvegardé
repertoire = os.fsencode(sauve)

for file in os.listdir(repertoire):
    filename = os.fsdecode(file)
    if filename.endswith(".zip"):

        strg = sauve + sys_exp + filename
        print(strg)
        file = open(strg,'rb')
        object = resource.Object(bt, filename)
        object.put(Body=file,ContentType='')
    else:
        continue
