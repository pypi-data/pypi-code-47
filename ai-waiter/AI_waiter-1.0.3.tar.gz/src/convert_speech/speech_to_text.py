"""
Code that convert speech to text
"""


import speech_recognition as sr

def SpeechConvert(file_name, recognizer):
    audio_file = sr.AudioFile(file_name)
    with audio_file as source:
        recognizer.adjust_for_ambient_noise(source, duration = .1)
        audio = recognizer.record(source)

    try:
        print(recognizer.recognize_google(audio))
    except sr.UnknownValueError:
        print("I'm sorry, I cannot understand you. Please try again.")
        sys.exit()
        return
    except sr.RequestError:
        print("Could not request results")
        sys.exit()
        return
        
    return audio


    