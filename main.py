# main.py
from scripts.motion_simulator import simulate_motion_detection
from scripts.audio_recognition import recognize_audio
from scripts.visitor_handler import get_visitor_data, register_visitor
from scripts.call_simulator import simulate_call_to_host

def main():
    # Simular detección de movimiento
    simulate_motion_detection()
    
    # Reconocer audio del visitante
    audio_text = recognize_audio()
    print(f"Texto del audio: {audio_text}")

    # Solicitar y registrar datos del visitante
    visitor_name, visitor_relation = get_visitor_data()
    register_visitor(visitor_name, visitor_relation)

    # Simular llamada al anfitrión
    simulate_call_to_host()

if __name__ == "__main__":
    main()
