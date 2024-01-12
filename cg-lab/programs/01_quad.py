#1. Quadrilateral printing

import math
import time,sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

sys.setrecursionlimit(10000)

WS = 900

X = 200
Y = 200
side = 300
x,y=0,0
p = 2

def getpixel(x,y):
	return glReadPixels(x,y,1,1,GL_RGB,GL_FLOAT,None)[0][0]

def setpixel(x,y,fillcolor):
	glColor3f(*fillcolor)
	glPointSize(p)
	glBegin(GL_POINTS)
	glVertex2f(x,y)
	glEnd()
	glFlush()

def floodfill(x,y,fillcolor,oldcolor):
	current_color = getpixel(x,y)
	if all (current_color == oldcolor):
		setpixel(x,y,fillcolor)
		floodfill(x-p,y,fillcolor,oldcolor)
		floodfill(x,y-p,fillcolor,oldcolor)
		floodfill(x,y+p,fillcolor,oldcolor)
		floodfill(x+p,y,fillcolor,oldcolor)



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
	floodfill(300,300,[1,0,1],[1,1,1])
	glutSwapBuffers()


def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA)
	glutInitWindowSize(WS,WS)
	glutInitWindowPosition(1000,0)
	glutCreateWindow("SAMPLE")
	glutDisplayFunc(draw)

	glClearColor(0,0,0,1)
	gluOrtho2D(0,WS,0,WS)
	glutMainLoop()
	
	
main()
