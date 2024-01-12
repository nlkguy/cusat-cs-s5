from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
WINDOWSIZE=500
x=0
y=0
radius=70
angle=0
dir=0

def Init():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-WINDOWSIZE,WINDOWSIZE,-WINDOWSIZE,WINDOWSIZE)

def body():
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_POLYGON)
    glVertex2f(x-100,y)
    glVertex2f(x+100,y)
    glVertex2f(x+90,y-40)
    glVertex2f(x-90,y-40)
    glEnd()
    
    glColor3f(0.0,0.0,0.0)
    glBegin(GL_POLYGON)
    glVertex(x+10,y+50)
    glVertex(x-10,y+50)
    glVertex(x-30,y)
    glVertex(x+30,y)
    glEnd()
    glPointSize(10)
    glBegin(GL_POINTS)
    glVertex2f(x,y+80)
    glEnd()
    
    glColor3f(0.1,0.7,1.0)
    glBegin(GL_POLYGON)
    glVertex2f(-500,-40)
    glVertex2f(-500,-500)
    glVertex2f(500,-500)
    glVertex2f(500,-40)
    glEnd()
    
def hand():
    glColor3f(0.0,1.0,0.0)
    glLineWidth(5)
    glBegin(GL_LINES)
    glVertex2f(x,y)
    x1=(-70)*math.cos(math.radians(angle))+(-70)*math.sin(math.radians(angle))+x
    y1=-(-70)*math.sin(math.radians(angle))+(-70)*math.cos(math.radians(angle))+y
    glVertex2f(x1,y1)
    glEnd()
    
def drawBoat():
    glClear(GL_COLOR_BUFFER_BIT)
    body()
    hand()
    glutSwapBuffers()

def animate(temp):
    global x,y,angle,dir
    glutPostRedisplay()
    glutTimerFunc(int(1000/60),animate,int(0))
    if angle>30:
        dir=1
    if angle<-90:
        dir=0

    if(dir==1):
        angle=angle-1
    else:
        angle=angle+1
    x=x-1
    if x==(-WINDOWSIZE+100):
        x=400


def main():
    glutInit(sys.argv)
    glutInitWindowSize(WINDOWSIZE,WINDOWSIZE)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGBA)
    glutCreateWindow("Boat")
    glutDisplayFunc(drawBoat)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(drawBoat)
    Init()
    glutMainLoop()

main()
