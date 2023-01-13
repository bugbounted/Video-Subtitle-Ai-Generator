from videoToAudio import getVideoToAudio,getVideoDuration,getLoop,getKaung,getWriteVttFileIntro
from deleteFile import getDeleteFile
from audioToText import getAudioToText
from translate import getTranslateText
from writeVttFile import getWriteVttFile
import googletrans
inputLangauge = input("Please Enter Input Language: ").lower()
outputLangauge = input("Please Enter Output Language: ").lower()
saveFileName = input("Save The File As: ")
my_map = googletrans.LANGUAGES
my_map['my'] = 'myanmar'
inv_map = {v: k for k, v in my_map.items()}
inputlan = inv_map[inputLangauge]
outputlan = inv_map[outputLangauge]
getVideoToAudio()
videoDuration = getVideoDuration()
videoTimeDiff = 5
kaung = getKaung()
loop = getLoop()
getWriteVttFileIntro(saveFileName,outputlan)

try:
    if kaung == 0:
        for m in range(loop - 2):
            number = loop - 2
            text = getAudioToText(m, inputlan)
            translated_text = getTranslateText(text, outputlan)
            getWriteVttFile(m, translated_text, videoDuration, videoTimeDiff, saveFileName)
            print(f"Original:{text},Translated:{translated_text}")
        print("Done")
    else:
        for m in range(loop - 1):
            number = loop - 1
            text = getAudioToText(m, inputlan)
            translated_text = getTranslateText(text, outputlan)
            getWriteVttFile(m, translated_text, videoDuration, videoTimeDiff, saveFileName)
            print(f"Original:{text},Translated:{translated_text}")

    if kaung == 0:
        number = loop - 2
    else:
        number = loop - 1
    getDeleteFile(number)

except:
    print("Try again And Check The Network")
    if kaung == 0:
        number = loop - 2
    else:
        number = loop - 1
    getDeleteFile(number)
