import firebase_admin
from firebase_admin import credentials, firestore

# Ruta al archivo JSON de credenciales
cred = credentials.Certificate("/Users/arlo/Documents/Mis_Proyectos/Python/Personal_Cheatsheet/practice/lista_tareas_firebase/venv/keys/lista-tareas-fef11-firebase-adminsdk-w3j3y-c4b8f3006a.json")
firebase_admin.initialize_app(cred)

# Cliente de Firestore
db = firestore.client()

def get_collection():
    return db.collection('lista_tareas_col')
