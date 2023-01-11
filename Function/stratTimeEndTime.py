def getStartTime(m):
    start_second_input = m
    start_hour = start_second_input // 3600
    start_hour1 = start_second_input % 3600
    start_minute = start_hour1 // 60
    start_second = start_hour1 % 60
    subtitle_start_time = f"{start_hour}:{start_minute}:{start_second}"
    return subtitle_start_time

def getEndTime(m,time_diff):
    end_second_input = m + time_diff
    end_hour = end_second_input // 3600
    end_hour1 = end_second_input % 3600
    end_minute = end_hour1 // 60
    end_second = end_hour1 % 60
    subtitle_end_time = f"{end_hour}:{end_minute}:{end_second}"
    return subtitle_end_time