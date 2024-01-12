'''
Afeef Mohammed

pgrm Animation_pendulum
'''

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import sys

x=0
y=0
t=0.00
a=1

def init():
  glClear(GL_COLOR_BUFFER_BIT)
  gluOrtho2D(-500,500,-500,500)

def draw():
  global x,y,t
  glClear(GL_COLOR_BUFFER_BIT)
  glColor3f(1,1,1)
  glLineWidth(2)
  glBegin(GL_LINES)
  glVertex2f(0,0)
  glVertex2f(0*math.cos(t)-(-200)*math.sin(t),0*math.sin(t)+(-200)*math.cos(t))
  glEnd()
  glColor3f(1,1,1)
  glLineWidth(2)
  glBegin(GL_POINTS)
  theta=0.0
  while theta<=6.28:
    x=float(50)*math.cos(theta)
    y=-250+float(50)*math.sin(theta)
    glVertex2f(x*math.cos(t)-y*math.sin(t),x*math.sin(t)+y*math.cos(t))
    theta+=0.001
  glEnd()
  glutSwapBuffers()
  

def animate(temp):
  global t,a
  if a==1:
    if(t>(-1)):
      t-=0.01
    else:
      a=2
  if a==2:
    if t<1:
      t+=0.01
    else:
      a=1   
  glutPostRedisplay()
  glutTimerFunc(50,animate,50)

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

