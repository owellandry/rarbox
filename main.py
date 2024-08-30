from scripts.motion_simulator import simulate_motion_detection
from scripts.visitor_handler import register_visitor
from scripts.voice_recognition import recognize_speech

def main():
    # Simular detección de movimiento
    simulate_motion_detection()
    
    # Registro de visitante
    visitor_name = input("Enter visitor's name: ")
    visitor_relation = input("Enter visitor's relation: ")
    register_visitor(visitor_name, visitor_relation)
    
    # Reconocimiento de voz
    speech_text = recognize_speech()
    if speech_text:
        print(f"Visitor said: {speech_text}")

if __name__ == "__main__":
    main()
