#Deepesh U S

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

WINDOW_SIZE=600
ROTATE_X=[0,0,0]#s,m,h
ROTATE_Y=[350,300,200]
LENGTH=[350,300,200]
THETA=[0,0,0]
POINT_SIZE=5
def init():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)
def drawCircle(xc,yc,radius):
    theta=0.0
    glBegin(GL_POINTS)
    while theta<6.28:
        x=radius*math.cos(theta)+xc
        y=radius*math.sin(theta)+yc
        glVertex2f(x,y)
        theta+=0.01
    glEnd()
def drawHand(length,x,y):
    glLineWidth(POINT_SIZE)
    glColor3f(0,0,0)
    glBegin(GL_LINES)
    glVertex2f(0,0)
    glVertex2f(x,y)
    glEnd()

def drawClock():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(POINT_SIZE)
    glColor3f(0.46,0.27,0.18)
    drawCircle(0,0,400)
    for i in range(0,3):
        drawHand(LENGTH[i],ROTATE_X[i],ROTATE_Y[i])
    glutSwapBuffers()
def animate(value):
    glutPostRedisplay()
    glutTimerFunc(int(1000/60),animate,0)
    for i in range(0,3):
        ROTATE_X[i]=LENGTH[i]*math.sin(math.radians(THETA[i]))
        ROTATE_Y[i]=LENGTH[i]*math.cos(math.radians(THETA[i]))
    if(THETA[0]>=360):
        THETA[0]=0
        THETA[1]+=1
    else:
        THETA[0]+=0.098
    if(THETA[1]>=360):
        THETA[1]=0
        THETA[2]+=1
    if(THETA[2]>=360):
        THETA[2]=0
    
def main():
    glutInit(sys.argv)
    glutInitWindowPosition(0,0)
    glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("Clock")
    glutDisplayFunc(drawClock)
    glutTimerFunc(0,animate,0)
    init()
    glutMainLoop()
main()
