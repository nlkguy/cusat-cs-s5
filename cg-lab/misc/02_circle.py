#2.circle drawing

import math
import time
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def init():
	glClearColor(0,0,0,1)
	gluOrtho2D(-300,300,-300,300)

def ploat():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1,0,1)
	glLineWidth(2)
	glBegin(GL_TRIANGLE_FAN)
	glVertex2f(0,0)
	for i in range(0,361,1):
		glVertex2f(50*math.cos(math.pi*i/180),50*math.sin(math.pi*i/180))
	glEnd()
	glFlush()
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(600,0)
	glutCreateWindow("SAMPLE")
	glutDisplayFunc(lambda: ploat())
	init()
	glutMainLoop()

if __name__ == "__main__":
    main()

