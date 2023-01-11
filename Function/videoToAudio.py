import moviepy.editor
from tkinter.filedialog import *

video = askopenfilename()
video = moviepy.editor.VideoFileClip(video)
video_duration = video.duration
audio = video.audio
loop = round((video_duration/5) + (video_duration%5))

kaung = video_duration%5

def getVideoToAudio():
    if kaung == 0:
        for m in range(loop - 2):
            if kaung == 0:
                start = m * 5
                end = (m * 5) + 5
                subClip = audio.subclip(start, end)
                subClip.write_audiofile(f"{m}.wav")
    else:
        for m in range(loop - 1):
            start = m * 5
            end = (m * 5) + (video_duration % 5)
            subClip = audio.subclip(start, end)
            subClip.write_audiofile(f"{m}.wav")

def getVideoDuration():
    return video_duration

def getLoop():
    return loop

def getKaung():
    return kaung