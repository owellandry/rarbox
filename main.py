# main.py

from scripts.motion_simulator import simulate_motion_detection
from scripts.audio_recognition import recognize_audio
from scripts.visitor_handler import get_visitor_data, register_visitor

def main():
    # Simula la detección de movimiento
    print("Iniciando simulación de detección de movimiento...")
    simulate_motion_detection()

    # Reconoce el audio
    print("Reconociendo audio...")
    audio_text = recognize_audio()
    print("Texto del audio:", audio_text)

    # Obtén los datos del visitante
    print("Obteniendo datos del visitante...")
    visitor_name, visitor_relation = get_visitor_data()
    print(f"Datos del visitante obtenidos: {visitor_name}, {visitor_relation}")

    # Registra al visitante
    print("Registrando al visitante...")
    register_visitor(visitor_name, visitor_relation)
    print("Registro del visitante completado.")

if __name__ == "__main__":
    main()
