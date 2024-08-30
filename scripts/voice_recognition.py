import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    # Especifica el índice del dispositivo que encontraste en la lista (generalmente será 0)
    with sr.Microphone(device_index=0) as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print("You said: " + text)
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

recognize_speech()
