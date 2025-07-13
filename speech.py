import speech_recognition as sr

def listen_and_convert():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("🎙 Speak something...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source)
    except Exception as e:
        print("❌ Microphone error:", e)
        return

    try:
        text = recognizer.recognize_google(audio)
        print("📝 You said:", text)
    except sr.UnknownValueError:
        print("😕 Sorry, could not understand your voice.")
    except sr.RequestError as e:
        print("⚠ Google API error:", e)

listen_and_convert()
