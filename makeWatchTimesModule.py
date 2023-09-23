## makeWatchTimesModule
import turtle as t

t.shape("classic")
def gotoHome():
    t.penup()
    t.home()
    t.pendown()
    
# 시간
def initPreviousHour(ph):
    gotoHome()
    t.color("black")
    hourSize = 30
    t.left(90)
    t.right(hourSize * ph)
    t.forward(90)
    t.stamp()
    #지워진 InsideLine 다시 그리기
    gotoHome()
    t.left(90)
    t.right(hourSize * ph)
    t.penup()
    t.color("white")
    t.forward(40)
    t.pendown()
    t.forward(10)

def hourContents(h):
    t.color("pink")
    hourSize = 30
    t.left(90)
    t.right(hourSize * h)
    t.forward(90)
    t.stamp()

def makeHourTime(h):
    gotoHome()
    if(h == 1):
            hourContents(h)
    if(h == 2):
            hourContents(h)
    if(h == 3):
            hourContents(h)
    if(h == 4):
            hourContents(h)
    if(h == 5):
            hourContents(h)
    if(h == 6):
            hourContents(h)
    if(h == 7):
            hourContents(h)
    if(h == 8):
            hourContents(h)
    if(h == 9):
            hourContents(h)
    if(h == 10):
            hourContents(h)
    if(h == 11):
            hourContents(h)
    if(h == 0):
            hourContents(h)

# 분
def initPreviousMinute(pm):
    gotoHome()
    t.color("black")
    minuteSize = 30 / 5
    t.left(90)
    t.right(minuteSize * pm)
    t.forward(145)
    t.stamp()
    #지워진 InsideLine 다시 그리기
    if(pm % 5 == 0):
        gotoHome()
        t.left(90)
        t.right(minuteSize * pm)
        t.penup()
        t.color("white")
        t.forward(40)
        t.pendown()
        t.forward(10)

def minuteContents(m):
    t.color("pink")
    minuteSize = 30 / 5
    t.left(90)
    t.right(minuteSize * m)
    t.forward(145)
    t.stamp()

def makeMinuteTime(m):
    gotoHome()
    if(m == 1):
        minuteContents(m)
    if(m == 2):
        minuteContents(m)
    if(m == 3):
        minuteContents(m)
    if(m == 4):
        minuteContents(m)
    if(m == 5):
        minuteContents(m)
    if(m == 6):
        minuteContents(m)
    if(m == 7):
        minuteContents(m)
    if(m == 8):
        minuteContents(m)
    if(m == 9):
        minuteContents(m)
    if(m == 10):
        minuteContents(m)
    if(m == 11):
        minuteContents(m)
    if(m == 12):
        minuteContents(m)
    if(m == 13):
        minuteContents(m)
    if(m == 14):
        minuteContents(m)
    if(m == 15):
        minuteContents(m)
    if(m == 16):
        minuteContents(m)
    if(m == 17):
        minuteContents(m)
    if(m == 18):
        minuteContents(m)
    if(m == 19):
        minuteContents(m)
    if(m == 20):
        minuteContents(m)
    if(m == 21):
        minuteContents(m)
    if(m == 22):
        minuteContents(m)
    if(m == 23):
        minuteContents(m)
    if(m == 24):
        minuteContents(m)
    if(m == 25):
        minuteContents(m)
    if(m == 26):
        minuteContents(m)
    if(m == 27):
        minuteContents(m)
    if(m == 28):
        minuteContents(m)
    if(m == 29):
        minuteContents(m)
    if(m == 30):
        minuteContents(m)
    if(m == 31):
        minuteContents(m)
    if(m == 32):
        minuteContents(m)
    if(m == 33):
        minuteContents(m)
    if(m == 34):
        minuteContents(m)
    if(m == 35):
        minuteContents(m)
    if(m == 36):
        minuteContents(m)
    if(m == 37):
        minuteContents(m)
    if(m == 38):
        minuteContents(m)
    if(m == 39):
        minuteContents(m)
    if(m == 40):
        minuteContents(m)
    if(m == 41):
        minuteContents(m)
    if(m == 42):
        minuteContents(m)
    if(m == 43):
        minuteContents(m)
    if(m == 44):
        minuteContents(m)
    if(m == 45):
        minuteContents(m)
    if(m == 46):
        minuteContents(m)
    if(m == 47):
        minuteContents(m)
    if(m == 48):
        minuteContents(m)
    if(m == 49):
        minuteContents(m)
    if(m == 50):
        minuteContents(m)
    if(m == 51):
        minuteContents(m)
    if(m == 52):
        minuteContents(m)
    if(m == 53):
        minuteContents(m)
    if(m == 54):
        minuteContents(m)
    if(m == 55):
        minuteContents(m)
    if(m == 56):
        minuteContents(m)
    if(m == 57):
        minuteContents(m)
    if(m == 58):
        minuteContents(m)
    if(m == 59):
        minuteContents(m)
    if(m == 0):
        minuteContents(m)

# 초
def initPreviousSecond(ps):
    gotoHome()
    t.color("black")
    secondSize = 30 / 5
    t.left(90)
    t.right(secondSize * ps)
    t.forward(172)
    #지워진 InsideLine 다시 그리기
    if(ps % 5 == 0):
        gotoHome()
        t.left(90)
        t.right(secondSize * ps)
        t.color("white")
        t.dot()
        t.penup()
        t.forward(40)
        t.pendown()
        t.forward(10)

def  secondContents(s):
    t.color("blue")
    secondSize = 30 / 5
    t.left(90)
    t.right(secondSize * s)
    t.forward(172)

def makeSecondTime(s):
    gotoHome()
    if(s == 1):
        secondContents(s)
    if(s == 2):
        secondContents(s)
    if(s == 3):
        secondContents(s)
    if(s == 4):
        secondContents(s)
    if(s == 5):
        secondContents(s)
    if(s == 6):
        secondContents(s)
    if(s == 7):
        secondContents(s)
    if(s == 8):
        secondContents(s)
    if(s == 9):
        secondContents(s)
    if(s == 10):
        secondContents(s)
    if(s == 11):
        secondContents(s)
    if(s == 12):
        secondContents(s)
    if(s == 13):
        secondContents(s)
    if(s == 14):
        secondContents(s)
    if(s == 15):
        secondContents(s)
    if(s == 16):
        secondContents(s)
    if(s == 17):
        secondContents(s)
    if(s == 18):
        secondContents(s)
    if(s == 19):
        secondContents(s)
    if(s == 20):
        secondContents(s)
    if(s == 21):
        secondContents(s)
    if(s == 22):
        secondContents(s)
    if(s == 23):
        secondContents(s)
    if(s == 24):
        secondContents(s)
    if(s == 25):
        secondContents(s)
    if(s == 26):
        secondContents(s)
    if(s == 27):
        secondContents(s)
    if(s == 28):
        secondContents(s)
    if(s == 29):
        secondContents(s)
    if(s == 30):
        secondContents(s)
    if(s == 31):
        secondContents(s)
    if(s == 32):
        secondContents(s)
    if(s == 33):
        secondContents(s)
    if(s == 34):
        secondContents(s)
    if(s == 35):
        secondContents(s)
    if(s == 36):
        secondContents(s)
    if(s == 37):
        secondContents(s)
    if(s == 38):
        secondContents(s)
    if(s == 39):
        secondContents(s)
    if(s == 40):
        secondContents(s)
    if(s == 41):
        secondContents(s)
    if(s == 42):
        secondContents(s)
    if(s == 43):
        secondContents(s)
    if(s == 44):
        secondContents(s)
    if(s == 45):
        secondContents(s)
    if(s == 46):
        secondContents(s)
    if(s == 47):
        secondContents(s)
    if(s == 48):
        secondContents(s)
    if(s == 49):
        secondContents(s)
    if(s == 50):
        secondContents(s)
    if(s == 51):
        secondContents(s)
    if(s == 52):
        secondContents(s)
    if(s == 53):
        secondContents(s)
    if(s == 54):
        secondContents(s)
    if(s == 55):
        secondContents(s)
    if(s == 56):
        secondContents(s)
    if(s == 57):
        secondContents(s)
    if(s == 58):
        secondContents(s)
    if(s == 59):
        secondContents(s)
    if(s == 0):
        secondContents(s)

