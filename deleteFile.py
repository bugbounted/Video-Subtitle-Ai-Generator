import os

def getDeleteFile(number):
    for d in range(number):
        if os.path.exists(f"{d}.wav"):
            os.remove(f"{d}.wav")
        else:
            print("The file does not exist")