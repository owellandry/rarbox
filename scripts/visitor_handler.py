from colorama import Fore, Style, init
from config.firebase_config import initialize_firebase
from google.cloud import firestore

# Inicializar colorama
init(autoreset=True)

# Inicializar Firestore
db = initialize_firebase()

def register_visitor(visitor_name, visitor_relation):
    doc_ref = db.collection('visitors').document()
    doc_ref.set({
        'name': visitor_name,
        'relation': visitor_relation
    })
    print(Fore.GREEN + f"Visitor {visitor_name} registered." + Style.RESET_ALL)

def get_visitor_data():
    while True:
        print(Fore.CYAN + "\nPor favor, ingresa los datos del visitante:" + Style.RESET_ALL)
        visitor_name = input(Fore.GREEN + "Nombre completo del visitante (ej. Juan Pérez): " + Style.RESET_ALL).strip()
        
        if visitor_name:
            visitor_relation = input(Fore.GREEN + "Relación con el anfitrión: " + Style.RESET_ALL).strip()
            return visitor_name, visitor_relation
        else:
            print(Fore.RED + "\nEl nombre no puede estar vacío. Inténtalo de nuevo." + Style.RESET_ALL)

if __name__ == "__main__":
    visitor_name, visitor_relation = get_visitor_data()
    register_visitor(visitor_name, visitor_relation)
