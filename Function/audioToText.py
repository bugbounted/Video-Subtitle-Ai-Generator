import pyaudio
import speech_recognition
from deleteFile import getDeleteFile

def getAudioToText(m,inputlan):
    recognizer = speech_recognition.Recognizer()
    audio_file = f"{m}.wav"
    try:
        audio_file = speech_recognition.AudioFile(audio_file)
        with audio_file as source:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio,language=inputlan)
            text = text.lower()
            return text
    except speech_recognition.UnknownValueError:
        print("Can't Read The File")
    # except:
    #     getDeleteFile(number)
    #     print("error")