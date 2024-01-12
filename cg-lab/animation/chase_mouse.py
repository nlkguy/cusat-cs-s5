#MUHMMED JASIR P T
#ANIMATION


from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
global x
global y
global m
global n
global window
global flag
global flag1
flag1=0
flag=0
window=500
x=-5
y=-5
m=-5
n=-5
def myinit():
    glClearColor(0,0,0,1)
    gluOrtho2D(-50,350,-50,450)
def draw():
    global m
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glColor3f(1,1,1)
    #dog body
    if(flag1==0):
        r=20
        b=2*3.14/20
        glBegin(GL_TRIANGLE_FAN)
        for i in range (0,20,1):
            glVertex2f(x+(r*math.cos(i*b)-180),y+(r*math.sin(i*b)+20))
        glEnd()
    else:
        r=20
        b=2*3.14/20
        glBegin(GL_TRIANGLE_FAN)
        for i in range (0,20,1):
            glVertex2f(x+(r*math.cos(i*b)-170),y+(r*math.sin(i*b)+30))
        glEnd()
    # dog head
    if (flag1==0):
        r=15
        b=2*3.14/20
        glBegin(GL_TRIANGLE_FAN)
        for i in range (0,20,1):
            glVertex2f(x+(r*math.cos(i*b)-150),y+(r*math.sin(i*b)+30))
        glEnd()
    else:
        r=15
        b=2*3.14/20
        glBegin(GL_TRIANGLE_FAN)
        for i in range (0,20,1):
            glVertex2f(x+(r*math.cos(i*b)-150),y+(r*math.sin(i*b)+50))
        glEnd()
    #cat body
    glColor3f(0.1,0.01,0.9)
    if(flag==0):
        r=10
        b=2*3.14/20
        glBegin(GL_TRIANGLE_FAN)
        for i in range (0,20,1):
            glVertex2f(m+(r*math.cos(i*b)-90),n+(r*math.sin(i*b)+20))
        glEnd()
    else:
        r=10
        b=2*3.14/20
        glBegin(GL_TRIANGLE_FAN)
        for i in range (0,20,1):
            glVertex2f(m+(r*math.cos(i*b)-70),n+(r*math.sin(i*b)+10))
        glEnd()
    #cat head
    if(flag==0):
        r=7
        b=2*3.14/20
        glBegin(GL_TRIANGLE_FAN)
        for i in range (0,20,1):
            glVertex2f(m+(r*math.cos(i*b)-75),n+(r*math.sin(i*b)+20))
        glEnd()
    else:
        r=7
        b=2*3.14/20
        glBegin(GL_TRIANGLE_FAN)
        for i in range (0,20,1):
            glVertex2f(m+(r*math.cos(i*b)-75),n+(r*math.sin(i*b)+20))
        glEnd()

    #tree trunk
    glColor3f(0.58,0.28,0)
    glBegin(GL_POLYGON)
    glVertex2f(150,0)
    glVertex2f(170,0)
    glVertex2f(170,260)
    glVertex2f(150,260)
    glEnd()
    
    #floor
    glColor3f(0.38,0.28,0)
    glBegin(GL_POLYGON)
    glVertex2f(-50,0)
    glVertex2f(-50,-10)
    glVertex2f(350,-10)
    glVertex2f(350,0)
    glEnd()

    # tree leaf
    glColor3f(0.0,1.0,0.0)
    p=155
    q=150+110
    r=45
    b=2*3.14/20
    glBegin(GL_TRIANGLE_FAN)
    for i in range (0,20,1):
        glVertex2f(p+(r*math.cos(i*b)),q+(r*math.sin(i*b)))
    glEnd()
    glFlush()

def animate(temp):
    global window
    global flag
    global flag1
    global x
    global y
    global m
    global n
    if(x-180<125 and m-90<125 and flag==0):          
        x=x+1
        m=m+1
    elif(m-90==125 and flag==0):
        flag=1
    elif((flag==1 and n<260) and (x-180<220 and flag1==0)): #or (x-180<160 and flag1==0)):
        n=n+1
        x=x+1
    #elif(x-180<120 and flag1==0):
    #    x=x+1
    elif(x-180==120 and flag1==0):
        flag1=1
    #elif(flag1==1 and y<70):
    #    y=y+1

    glutPostRedisplay()
    glutTimerFunc(10,animate,0)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(0,0)
    glutCreateWindow("OpenGL Prgm")
    myinit()
    glutDisplayFunc(draw)
    glutTimerFunc(1,animate,0)
    #glutIdleFunc(draw)

    glutMainLoop()
main()
