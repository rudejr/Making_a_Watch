import turtle as t
from datetime import  datetime
import time

# myModules
import makeWatchTimesModule as mWT
import makeWatchImageModule as mWI

def currentTime():
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second
    return hour, minute, second

## 시간그리기
def drawTimeStart():
    limit = 130
    cnt = 0
    start_h, start_m, start_s = currentTime()
    mWT.makeMinuteTime(start_m)
    mWT.makeHourTime(start_h)
    while(limit > cnt):
        h, m, s = currentTime()
        if(h >= 12):
            h -= 12
        # 그렸던 시간, 분, 초 지우기
        if(start_h < h or h == 0):
            mWT.initPreviousHour(start_h)
            start_h = h

        if(start_m < m or m == 0):
            mWT.initPreviousMinute(start_m)
            start_m = m
                
        # 가끔 2초씩 뛰어넘을 때 대비
        if(start_s < s or s == 0 or s == 1 or s == 2):
            mWT.initPreviousSecond(start_s)
            start_s = s
            if(s == 0 or s == 1 or s == 2):
                mWT.makeMinuteTime(m)
        # 시간, 분, 초 그리기
        mWT.makeSecondTime(s)
        if(s  == m + 1 or s == m + 2):
            mWT.makeMinuteTime(m)
        mWT.makeHourTime(h)
        cnt += 1

while(True):
    choice = t.textinput("project_20201049_안경덕", "시계를 사용하겠습니까? (yes/no) : ")
    if(choice == 'yes'):
        t.reset()
        mWI.default_setting()
        mWI.drawWatch()
        drawTimeStart()
    elif(choice == 'no'):
        break

t.done()
