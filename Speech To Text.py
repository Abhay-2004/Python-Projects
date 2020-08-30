import speech_recognition as sr

def main():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        r.adjust_for_ambient_noise(source)

        print("Start Speeking")
        audio = r.listen(source)
        print("Recognizing Now: ")

        try:
            print("You Spoke : " + r.recognize_google(audio))
            print("Recorded Successfully")

        except Exception as e:
            print("Error :  " + str(e))

        with open("recorded.wav", "wb") as f:
            f.write(audio.get_wav_data())

if __name__ == "__main__":
    main()
