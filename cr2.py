from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
WINDOWSIZE=500
import math
b1,b2,b3,b4=0,0,-0,0
len=-300

def Init():
    glClearColor(0.0,0.0,0.0,0.0)
    gluOrtho2D(-WINDOWSIZE,WINDOWSIZE,-WINDOWSIZE,WINDOWSIZE)


def bowl():
    glColor3f(0.5,0.5,0.5)
    glLineWidth(7)
    glBegin(GL_LINES)
    glVertex2f(0,-300)
    glVertex2f(0,-500)
    glVertex2f(150,-300)
    glVertex2f(150,-500)
    glVertex2f(0,-500)
    glVertex2f(150,-500)
    glEnd()


def water():
    glColor3f(0.2,0.5,1.0)
    glLineWidth(1)
    glBegin(GL_LINES)
    theta=0
    while theta<360:
        glVertex(75,b1)
        x1=10*math.cos(math.radians(theta))+75
        y1=10*math.sin(math.radians(theta))+b1
        glVertex2f(x1,y1)
        theta=theta+0.1
    glEnd()
    glBegin(GL_LINES)
    theta=0
    while theta<360:
        glVertex(75,b2)
        x1=10*math.cos(math.radians(theta))+75
        y1=10*math.sin(math.radians(theta))+b2
        glVertex2f(x1,y1)
        theta=theta+0.1
    glEnd()
    glBegin(GL_LINES)
    theta=0
    while theta<360:
        glVertex(75,b3)
        x1=10*math.cos(math.radians(theta))+75
        y1=10*math.sin(math.radians(theta))+b3
        glVertex2f(x1,y1)
        theta=theta+0.1
    glEnd()
    glBegin(GL_LINES)
    theta=0
    while theta<360:
        glVertex(75,b4)
        x1=10*math.cos(math.radians(theta))+75
        y1=10*math.sin(math.radians(theta))+b4
        glVertex2f(x1,y1)
        theta=theta+0.1
    glEnd()


def fill():
    glColor3f(0.2,0.5,1.0)
    glLineWidth(1)
    glBegin(GL_QUADS)
    glVertex2f(145,-490+len)
    glVertex2f(5,-490+len)
    glVertex2f(5,-490)
    glVertex2f(145,-490)
    glEnd()

def drawWaterPipe():
    glClear(GL_COLOR_BUFFER_BIT)
    bowl()
    water()
    fill()
    glutSwapBuffers()

def animate(temp):
    global b1,b2,b3,b4,len
    glutPostRedisplay()
    glutTimerFunc(int(1000/60),animate,int(0))
    
    if len<190:
        b1=b1-10
        b2=b2-10
        b3=b3-10
        b4=b4-10
        len=len+1
    if b1==-400:
        b1=40
    

def main():
    glutInit(sys.argv)
    glutInitWindowSize(WINDOWSIZE,WINDOWSIZE)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGBA)
    glutCreateWindow("Water filling")
    glutDisplayFunc(drawWaterPipe)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(drawWaterPipe)
    Init()
    glutMainLoop()

main()
