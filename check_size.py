from datetime import datetime
import os

def str_to_date(str):
    t  = str.split('-')
    year = int('20'+t[2])
    month = int(t[1])
    day = int(t[0])
    hour = int(t[3][0:2])
    minute = int(t[3][2:4])
    second = int(t[3][4:6])
    date = datetime(year, month, day,hour, minute, second)
    return date


dirs = os.listdir ("pcaps/")
cnt = 0.0
total = 0.0
for dir in dirs:
    try:
        current_date = str_to_date(dir)
        if(current_date>datetime(2021,01,28,22,0,0)):
            for file in os.listdir('pcaps/'+dir+'/'):
                file_stats = os.stat('pcaps/'+dir+'/'+file)
                total += 1
                if(file_stats.st_size>2048):
                    cnt += 1
    except:
        continue
print(cnt)
print(total)
print(cnt/total)

