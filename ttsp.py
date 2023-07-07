import pyttsx3
import sys

class TextToSpeechPrinter:
    def __init__(self):
        # Initialize pyttsx3
        self.engine = pyttsx3.init()
    
    def __enter__(self):
        # save the OG print function
        self.original_print = print

        # New print function that speaks
        def tts_print(*args, **kwargs):
            # Convert athe  *args to a string
            text = " ".join(str(arg) for arg in args)

            # speak that text use pyttsx3
            self.engine.say(text)
            self.engine.runAndWait()
        
        # set new print function as the way to print
        sys.stdout.write = tts_print

    def __exit__(self, exc_type, exc_value, trace):
        sys.stdout.write = self.original_print

            
           