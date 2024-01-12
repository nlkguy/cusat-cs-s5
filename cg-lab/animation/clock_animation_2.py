'''
###########################################
###########################################
####                                   ####
####     NAME :ANGELO ANTU             ####
####     CLASS : CSA                   ####
####     EXPERIMENT NO: 16             ####
####    EXPERIMENT NAME: CLOCK         ####
####                                   ####
###########################################
###########################################

'''

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import sys

h=0
m=0
s=0

def init():
  gluOrtho2D(-500,500,-500,500)

def draw():
  glClear(GL_COLOR_BUFFER_BIT)
  glColor3f(1,1,0.1)
  glLineWidth(5)
  glBegin(GL_POINTS)
  theta=0.0
  while theta<=6.28:
    x=float(200)*math.cos(theta)
    y=float(200)*math.sin(theta)
    glVertex2f(x,y)
    theta+=0.001
  glEnd()
  glColor3f(0.8,0.8,1)
  glLineWidth(5)
  glBegin(GL_LINES)
  glVertex2f(0,0)
  glVertex2f(-200*math.sin(s),200*math.cos(s))
  glEnd()
  glColor3f(0.7,0.7,1)
  glLineWidth(5)
  glBegin(GL_LINES)
  glVertex2f(0,0)
  glVertex2f(-150*math.sin(m),150*math.cos(m))
  glEnd()
  glColor3f(0.5,0.5,1)
  glLineWidth(4)
  glBegin(GL_LINES)
  glVertex2f(0,0)
  glVertex2f(-100*math.sin(h),100*math.cos(h))
  glEnd()
  glutSwapBuffers()  


def animate(temp):
  global h,m,s
  if s>-6.2832:
    s-=0.01
  else:
    s=0.00
    m-=0.01472
  if m<-6.2832:
    m=0.00
    h-=0.01472
  if h<-6.2832:
    h=0.00
  glutPostRedisplay()
  glutTimerFunc(10,animate,10)

def main():
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_RGBA)
  glutInitWindowSize(500,500)
  glutInitWindowPosition(600,0)
  glutCreateWindow("SAMPLE")
  glutDisplayFunc(lambda : draw())
  glutTimerFunc(0,animate,0)
  init()
  glutMainLoop()
main()



