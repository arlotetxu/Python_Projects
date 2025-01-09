import firebase_admin
from firebase_admin import credentials, firestore

# Ruta al archivo JSON de credenciales
# Macos:
cred = credentials.Certificate("/Users/arlo/Documents/Mis_Proyectos/Python/keys_ssh/lista-tareas-fef11-firebase-adminsdk-w3j3y-188ed50279.json")
# Ubuntu
#cred = credentials.Certificate("/home/arlo/Documentos/mis_proyectos/python/Keys_SSH/lista-tareas-fef11-firebase-adminsdk-w3j3y-82fce2550a.json")
firebase_admin.initialize_app(cred)

# Cliente de Firestore
db = firestore.client()

def get_collection():
    return db.collection('lista_tareas_col')
