from writeVttFile import getWriteVttFile
from googletrans import Translator
translator = Translator()

def getTranslateText(text,outputlan):
    hello = translator.translate(text, dest=outputlan)
    return hello.text