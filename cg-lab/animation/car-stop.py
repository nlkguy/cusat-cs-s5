from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
sys.setrecursionlimit(100000)
WS = 900
x,y=0,0
ps = 5
fillcolor = [1,0,0]

tx,ty=0,0

def getpixel(x,y):
    return glReadPixels(x,y,1,1,GL_RGB,GL_FLOAT,None)[0][0]

def setpixel(x,y,fillcolor):
    glColor3f(*fillcolor)
    glPointSize(ps)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()
    glFlush()



def flood(x,y,fillcolor,oldcolor):
    if all (getpixel(x,y)==oldcolor):
        setpixel(x,y,fillcolor)
        flood(x+ps,y,fillcolor,oldcolor)
        flood(x,y+ps,fillcolor,oldcolor)
        flood(x-ps,y,fillcolor,oldcolor)
        flood(x,y-ps,fillcolor,oldcolor)




def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    print("draw func")
    glColor3f(0,1,0)
    glLineWidth(1)
    glBegin(GL_POLYGON)
    glVertex2f(100+tx,400+ty)
    glVertex2f(300+tx,500+ty)
    glVertex2f(550+tx,400+ty)
    glVertex2f(550+tx,350+ty)
    glVertex2f(150+tx,350+ty)
    glEnd()
    glFlush()

          

def animate(temp):
    global tx,ty
    print("animate func")
    glutPostRedisplay()
    glutTimerFunc(1000,animate,0)
    tx+=10
    ty+=0

def click(button,state,x,y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        flood(x,y,fillcolor,getpixel(x,y))

def main():
    glutInit(sys.argv)
    glutInitWindowSize(WS,WS)
    glutCreateWindow("car stop")
    gluOrtho2D(0,WS,0,WS)

    glutDisplayFunc(draw)
    glutMouseFunc(click)
    glutTimerFunc(0,animate,0)
    glutMainLoop()

main()
