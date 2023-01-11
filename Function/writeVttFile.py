from stratTimeEndTime import getStartTime,getEndTime

def getWriteVttFile(m,text,videoDuration,videoTimeDiff,saveFileName):
    try:
        if text is None:
            print("Cannot Write")
        else:
            startTime = getStartTime(m)
            endTime = getEndTime(m, videoTimeDiff)
            empolyee_file = open(f"{saveFileName}.vtt", "a",encoding='utf8')
            empolyee_file.write(f"{startTime} --> {endTime}")
            empolyee_file.write(f"\n{text}")
            empolyee_file.write("\n")
            empolyee_file.write("\n")
            empolyee_file.close()
    except:
        print("error")