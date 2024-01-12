##STANZIN RABYANG
#  
# CS_B
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
window=200
x=0
y=0
m=0
n=0
def myinit():
    glClearColor(0,0,0,2)
    gluOrtho2D(-window,window,-window,window)
def draw():
    global m
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glColor3f(0.6,0.8,1.2)
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
    glColor3f(0.77,0.30,0)
    glBegin(GL_POLYGON)
    glVertex2f(150,0)
    glVertex2f(170,0)
    glVertex2f(170,150)
    glVertex2f(150,150)
    glEnd()

    # tree leaf
    glColor3f(0.5,1.5,0.5)
    p=155
    q=150
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
    elif((flag==1 and n<160) and (x-180<120 and flag1==0)): #or (x-180<160 and flag1==0)):
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
