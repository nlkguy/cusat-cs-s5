#Harikrishnan Aneesh
#
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

WINDOW_SIZE=500
GLOBAL_X=0.0
GLOBAL_Y=0.0
FPS=60
DIR=1

PEND_LENGTH=float(int(input("Length of the Pendulum: ")))
BOB_RADIUS=float(int(input("Bob Radius: ")))
MAX_THETA=float(int(input("Maxim angle of swing: ")))
THETA=0.0

def init():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)

def drawCircle(x,y):
    i=0.0
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x,y)
    for i in range(0,360,1):
        glVertex2f(BOB_RADIUS*math.cos(math.pi*i/180.0)+x,BOB_RADIUS*math.sin(math.pi*i/180.0)+y)
    glEnd()

def drawPendulum():
    global MAX_THETA
    global GLOBAL_X
    global GLOBAL_Y
    global THETA
    global DIR
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,1.0,1.0)
    glLineWidth(5)
    glBegin(GL_LINES)
    glVertex2f(0,0)
    glVertex2f(GLOBAL_X,GLOBAL_Y)
    glEnd()
    drawCircle(GLOBAL_X,GLOBAL_Y)
    glutSwapBuffers()

def animate(temp):
    global MAX_THETA
    global GLOBAL_X
    global GLOBAL_Y
    global THETA
    global DIR
    glutPostRedisplay()
    glutTimerFunc(int(1200/FPS),animate,int(0))
    if DIR==1:
        if(THETA<MAX_THETA):
            THETA=THETA+1.0
        else:
            DIR=0
    elif DIR==0:
        if(THETA>=-MAX_THETA):
            THETA=THETA-1.0
        else:
            DIR=1
    GLOBAL_X=PEND_LENGTH*math.sin(math.radians(THETA))
    GLOBAL_Y=-PEND_LENGTH*math.cos(math.radians(THETA))



def main():
    glutInit(sys.argv)
    glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("Pendulum")
    glutDisplayFunc(drawPendulum)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(drawPendulum)
    init()
    glutMainLoop()

main()
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

WINDOW_SIZE=500
GLOBAL_X=0.0
GLOBAL_Y=0.0
FPS=60
DIR=1

PEND_LENGTH=float(int(input("Length of the Pendulum: ")))
BOB_RADIUS=float(int(input("Bob Radius: ")))
MAX_THETA=float(int(input("Maxim angle of swing: ")))
THETA=0.0

def init():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)

def drawCircle(x,y):
    i=0.0
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x,y)
    for i in range(0,360,1):
        glVertex2f(BOB_RADIUS*math.cos(math.pi*i/180.0)+x,BOB_RADIUS*math.sin(math.pi*i/180.0)+y)
    glEnd()

def drawPendulum():
    global MAX_THETA
    global GLOBAL_X
    global GLOBAL_Y
    global THETA
    global DIR
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,1.0,0.0)
    glLineWidth(5)
    glBegin(GL_LINES)
    glVertex2f(0,0)
    glVertex2f(GLOBAL_X,GLOBAL_Y)
    glEnd()
    drawCircle(GLOBAL_X,GLOBAL_Y)
    glutSwapBuffers()

def animate(temp):
    global MAX_THETA
    global GLOBAL_X
    global GLOBAL_Y
    global THETA
    global DIR
    glutPostRedisplay()
    glutTimerFunc(int(1000/FPS),animate,int(0))
    if DIR==1:
        if(THETA<MAX_THETA):
            THETA=THETA+1.0
        else:
            DIR=0
    elif DIR==0:
        if(THETA>=-MAX_THETA):
            THETA=THETA-1.0
        else:
            DIR=1
    GLOBAL_X=PEND_LENGTH*math.sin(math.radians(THETA))
    GLOBAL_Y=-PEND_LENGTH*math.cos(math.radians(THETA))



def main():
    glutInit(sys.argv)
    glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("Pendulum")
    glutDisplayFunc(drawPendulum)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(drawPendulum)
    init()
    glutMainLoop()

main()
