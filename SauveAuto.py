# Programme de sauvegarde automatique
# Auteur : Florent FOVET
# Date : 06/2021
# Version v1.0.1

# Importation des modules
import platform
import os
import zipfile
import boto3


# Nom de la machine
def pc_name():
    pcname = platform.node()
    return pcname


# Définition du système d'exploitation
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



# Définition et copie du répertoire
repertoire = os.fsencode(repertoire1)

for file in os.listdir(repertoire):
    filename = os.fsdecode(file)
    if filename.endswith(".zip") or filename.endswith(".jpg") or filename.endswith(".png"):

        strg = repertoire1 + sys_exp + filename
        print(strg)
        file = open(strg,'rb')
        object = resource.Object(bt, filename)
        object.put(Body=file,ContentType='')
    else:
        continue
