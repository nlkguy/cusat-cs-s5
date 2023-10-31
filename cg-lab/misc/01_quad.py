#1. Quadrilateral printing

import math
import time
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
X = 0
Y = 0
side = int(input("side length : "))

def init():
	glClearColor(0,0,0,1)
	gluOrtho2D(-300,300,-300,300)
def draw():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1,1,1)
	glLineWidth(1)
	glBegin(GL_QUADS)
	glVertex2f(X,Y)
	glVertex2f(X+side,Y)
	glVertex2f(X+side,Y+side)
	glVertex2f(X,Y+side)
	glEnd()
	glutSwapBuffers()


def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(1000,0)
	glutCreateWindow("SAMPLE")
	glutDisplayFunc(lambda: draw())

	init()
	glutMainLoop()
	
	
if __name__ == "__main__":
    main()

