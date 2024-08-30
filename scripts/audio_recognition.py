# scripts/audio_recognition.py

import speech_recognition as sr

def recognize_audio():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Ajustando el micrófono...")  # Mensaje de ajuste
        recognizer.adjust_for_ambient_noise(source, duration=5)  # Ajustar para el ruido ambiental
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=10)  # Tiempo de espera para la captura
            text = recognizer.recognize_google(audio)
            return text
        except sr.WaitTimeoutError:
            return "El tiempo de espera para la captura de audio se agotó."
        except sr.UnknownValueError:
            return "Lo siento, no pude entender el audio."
        except sr.RequestError:
            return "Lo siento, hubo un error con la solicitud."
