'''
Afeef Mohammed
pgrm Animation_car
'''
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import sys
import random
from pygame import mixer

#mixer.init()
#plays=mixer.Sound('horn.wav')

x=0
y=0
t=0
yr=100
tr=1

def init():
  glClearColor(0,0,0,1)
  gluOrtho2D(-500,500,-500,500)

def drawcir(q):
  glColor3f(0,1,1)
  glLineWidth(2)
  glBegin(GL_TRIANGLE_FAN)
  glVertex2f(q,0)
  for i in range(0,361,1):
    glVertex2f(q+20*math.cos(math.pi*i/180),20*math.sin(math.pi*i/180))
  glEnd()
  glColor3f(0,0,0)
  glBegin(GL_LINES)
  glVertex2f(q+20*math.cos(t)-(0)*math.sin(t),20*math.sin(t)+(0)*math.cos(t))
  glVertex2f(q-20*math.cos(t)-(0)*math.sin(t),-20*math.sin(t)+(0)*math.cos(t))
  glEnd()
  glBegin(GL_LINES)  
  glVertex2f(q+0*math.cos(t)-(20)*math.sin(t),0+0*math.sin(t)+(20)*math.cos(t))
  glVertex2f(q+0*math.cos(t)-(-20)*math.sin(t),0+0*math.sin(t)+(-20)*math.cos(t))
  glEnd()

def draw():
  global x,y
  glClear(GL_COLOR_BUFFER_BIT)
  glColor3f(1,0,0)
  glBegin(GL_QUADS)
  glVertex2f(x,y)
  glVertex2f(x+200,y)
  glVertex2f(x+160,y+40)
  glVertex2f(x,y+40)
  glEnd()
  glBegin(GL_QUADS)
  glVertex2f(x+10,y+40)
  glVertex2f(x+10,y+80)
  glVertex2f(x+155,y+80)
  glVertex2f(x+155,y+40)
  glEnd()
  drawcir(x+25)
  drawcir(x+155)
  glutSwapBuffers()

def animate(value):
  global x,y,t,tr,yr
  if tr==1:
    if x<500:
      x=x+1
    else:
      x=-500
    if t>-math.radians(360):
      t-=0.01
    else:
      t=0.00
  elif tr==0:
    if x>-500:
      x=x-1
    else:
      x=500
    if t<math.radians(360):
      t+=0.01
    else:
      t=0.00
  elif tr==-1:
    pass
  glutPostRedisplay()
  glutTimerFunc(yr,animate,yr) 

def keyboard(key,x,y):
  global tr,yr
  key=key.decode()
  if key=='f':
    tr=1
  elif key=='b':
    tr=0
  elif key=='w':
    if yr!=0:
      yr-=5
  elif key=='s':
    yr+=10
    if yr==200:
      tr=-1
  elif key=='h':
    plays.play() 
     
def main():
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_RGBA)
  glutInitWindowSize(500,500)
  glutInitWindowPosition(600,0)
  glutCreateWindow("CAR")
  glutDisplayFunc(lambda : draw()) 
  glutTimerFunc(0,animate,0)
  glutKeyboardFunc(keyboard)
  init()
  glutMainLoop()
main()
  
