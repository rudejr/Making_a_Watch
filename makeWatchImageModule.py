## makeWatchImageModule
import turtle as t

# 기본 설정
radius = 200
def default_setting():
    t.hideturtle()
    t.bgcolor("black")
    t.pencolor("white")
    t.pensize(3)
    t.speed(100)

# 원점으로 이동
def gotoHome():
    t.penup()
    t.home()
    t.pendown()

# 시계 틀 만들기( 반지름 200, 원점 (0, 0) )
def drawCircle():
    t.right(90)
    t.penup()
    t.forward(radius)
    t.left(90)
    t.pendown()
    t.circle(radius)

# 시계 디자인
def drawHome():
    gotoHome()
    t.fillcolor("white")
    t.begin_fill()
    t.right(90)
    t.penup()
    t.forward(5)
    t.left(90)
    t.circle(5)
    t.end_fill()
def drawInsideLine():
    t.penup()
    t.forward(40)
    t.pendown()
    t.forward(10)
def drawMinuteLine():
    minute = 30 / 5
    for i in range(1, 61):
        gotoHome()
        t.left(90)
        t.right(minute)
        t.penup()
        t.forward(radius - 8)
        t.pendown()
        t.forward(8)
        minute += 30 / 5

def timeDraw():
    t.color("orange")
    for i in range(1, 13):
        gotoHome()
        t.penup()
        t.goto(-7, -9)
        t.left(90)
        t.right(30 * i)
        t.forward(radius + 30)
        t.pendown()
        t.write(i, font = ("", 18))
    t.color("white")

# 시계그리기
def drawWatch():
    drawCircle()
    drawHome()
    largeLine = 30
    for i in range(12):
        gotoHome()
        t.left(90)
        t.right(largeLine)
        drawInsideLine()
        t.penup()
        t.forward(radius - 75)
        t.pendown()
        t.forward(25)
        largeLine += 30
    drawMinuteLine()
    timeDraw()
