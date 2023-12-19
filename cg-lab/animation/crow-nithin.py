from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import time
ref_x = 0
ref_y =0

def beak():
    global ref
    glColor3f(1,.5,0)
    glBegin(GL_TRIANGLES)
    glVertex2f(22,2)
    glVertex2f(22,-2)
    glVertex2f(26,0)  
    glEnd()
def filling(y):
    glColor3f(0,.3,.8)
    glBegin(GL_POLYGON)
    glVertex2f(12,y)
    glVertex2f(12,-58)
    glVertex2f(47,-58)
    glVertex2f(47,y)
    glEnd()
def stones(y):
    glColor3f(.8,0,0)
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(26,y)  
    glEnd() 
def bird():
    global ref_x,ref_y
    glColor(0,.8,.2)
    glBegin(GL_TRIANGLE_FAN)#body
    for i in range(0,360,1):
        theta = math.pi * (i/180)
        x = ref_x+3 + 20*math.cos(theta)
        y =  ref_y +10 * math.sin(theta)
        glVertex2f(x,y)
    glEnd()
    glColor3f(0,0,0)
    glPointSize(5)
    glBegin(GL_POINTS)#eyes
    glVertex2f(ref_x+15,ref_y+2)
    glEnd()
    beak()
    jar()
     
def jar():#jar
    glColor3f(.8,.3,0)
    glBegin(GL_POLYGON)
    glVertex2f(10,-10)
    glVertex2f(10,-60)
    glVertex2f(50,-60)
    glVertex2f(50,-10)
    glEnd()
def animate():
    
    for i in range(-58,-11,1):
        glClear(GL_COLOR_BUFFER_BIT)
        stones(-i-60)
        stones(-i-58)
        stones(-i-62)
        bird()
        filling(i)
        stones(-i-60)
        stones(-i-58)
        stones(-i-62)
        glFlush()
        time.sleep(0.07)
def clearScreen():
    gluOrtho2D(-100, 100, -100, 100)
    glClearColor(0.0, 0.0, 0.0, 1.0)
def main():
    glutInit()
    glutInitWindowSize(750, 750)
    glutCreateWindow("Bird")
    glutInitWindowPosition(1000, 1000)
    glutDisplayFunc(animate)

    clearScreen()
    glutMainLoop()


main()