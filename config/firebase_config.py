# config/firebase_config.py
import firebase_admin
from firebase_admin import credentials, firestore

def initialize_firebase():
    # Reemplaza 'path/to/serviceAccountKey.json' con la ruta a tu archivo de credenciales
    cred = credentials.Certificate('config/serviceAccountKey.json')
    firebase_admin.initialize_app(cred)
    return firestore.client()
