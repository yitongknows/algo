def solution(time_pair):
    start_time = int(encode(time_pair[0]))
    end_time = int(encode(time_pair[1]))

    output = []
    i = start_time
    while i <= end_time:
        output.append(str(i))
        i = valid(i+5)
    return output

def encode(timeStr):
    timeList = timeStr.split(" ")
    #encode date
    day_dict = {"mon": 1, "tue": 2, "wed":3,"thur":4,"fri":5, "sat":6, "sun":7}
    day = day_dict[timeList[0].lower()]
    day_prefix = 0
    
    #encode time
    hour_prefix = 0
    if timeList[2] == "pm":
        hour_prefix += 12
    
    hour_min = timeList[1].split(":")
    #determine minitue,consider round up
    m = int(hour_min[1])
    if m % 5 > 2:
        m += 5 - m%5
    else:
        m -= m%5
    if m >= 60:
        hour_prefix += m // 60
        m = m % 60
    
    #determine hour
    hour = int(hour_min[0])
    hour += hour_prefix

    if hour >= 24:
        day_prefix += hour // 24
        hour = hour % 24
        
    #determine day
    day += day_prefix
    if day > 7 :
        day -= 7
    
    encoded = str(day)
    if len(str(hour)) <= 1:
        encoded = encoded + "0" + str(hour)
    else:
        encoded = encoded + str(hour)
    if len(str(m)) <= 1:
        encoded = encoded + "0" + str(m)
    else:
        encoded = encoded + str(m)
    return encoded

def valid(num):
    num = str(num)
    day = int(num[0])
    hour = int(num[1:3])
    m = int(num[3:])
    day_prefix = 0
    hour_prefix = 0

    if m >= 60:
        hour_prefix += 1
        m = m % 60

    hour += hour_prefix
    if hour >= 24:
        day_prefix += 1
        hour = hour % 24
    
    #determine day
    day += day_prefix
    if day > 7 :
        day -= 7

    encoded = str(day)
    if len(str(hour)) <= 1:
        encoded = encoded + "0" + str(hour)
    else:
        encoded = encoded + str(hour)
    if len(str(m)) <= 1:
        encoded = encoded + "0" + str(m)
    else:
        encoded = encoded + str(m)
    return int(encoded)

