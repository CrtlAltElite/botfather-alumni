import speech_recognition as sr
import builtins
from beepy import beep

def play_sound():
    beep(sound="coin")

class SpeechToTextInputer:
    def __init__(self):
        self.r = sr.Recognizer()
    
    def readLine(self, *args):
        while True:
            with sr.Microphone() as source:
                play_sound()
                audio = self.r.record(source, 3)
            
            try:
                text= self.r.recognize_google(audio)
                if text:
                    return text
            except sr.UnknownValueError:
                print("Speech recogniition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
            except Exception as e:
                print("I am sorry please Try again")

    def __enter__(self):
        self.original_input = builtins.input
        builtins.input = self.readLine

    def __exit__(self, exc_type, exc_value, trace):
        builtins.input = self.original_input
