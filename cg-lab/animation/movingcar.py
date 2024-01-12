#Dhanush P K
#

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
from playsound import playsound

GLOBAL_X=0
GLOBAL_Y=0
ROTATE_X=0
ROTATE_Y=0
WINDOW_SIZE=1000
POINT_SIZE=10
DIR=1
THETA=0.0
BOB_RADIUS=40
def init():
   glClearColor(1.0,1.0,1.0,1.0)
   gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)
def drawCircle(x,y,s):
   if s==0:
      x=x-150
      y=y-100
   elif s==1:
      x=x+150
      y=y-100
   glColor3f(0,0,0)
   glBegin(GL_TRIANGLE_FAN)
   glVertex2f(x,y)
   for i in range(0,360,1):
      glVertex2f(BOB_RADIUS*math.cos(math.pi*i/180)+x,BOB_RADIUS*math.sin(math.pi*i/180)+y)
   glEnd()
def drawSpoke(x,y,s):
   if s==0:
      x=x-150
      y=y-100
   elif s==1:
      x=x+150
      y=y-100
   glColor3f(1,1,1)
   glLineWidth(5)
   glBegin(GL_LINES)
   glVertex2f(x,y)
   glVertex2f(x+ROTATE_X,y+ROTATE_Y)
   glEnd()

def drawRectangle(x,y):
   glBegin(GL_QUADS)
   glVertex2f(x-250,y-100)
   glVertex2f(x-250,y+50)
   glVertex2f(x+250,y+50)
   glVertex2f(x+250,y-100)
   glEnd()
def drawCar():
   glClear(GL_COLOR_BUFFER_BIT)
   glColor3f(1.0,0,0)
   glLineWidth(POINT_SIZE)
   drawRectangle(GLOBAL_X,GLOBAL_Y)
   drawCircle(GLOBAL_X,GLOBAL_Y,0)
   drawCircle(GLOBAL_X,GLOBAL_Y,1)
   drawSpoke(GLOBAL_X,GLOBAL_Y,0)
   drawSpoke(GLOBAL_X,GLOBAL_Y,1)
   glFlush()
   glutSwapBuffers()

def keyboard(key,x,y):
   key=key.decode()
   i=0
   if key=='d':
      i=i+1
      animate(i)
   elif key=='a':
      i=i-1
      animate(i)
      
   elif key=='s':
      i=0
      animate(0)
   elif key=='h':
      animate(i)
      playsound('/home/users/20221034/Desktop/Dhanush/bushorn.wav')
      


def animate(speed):
   global GLOBAL_X
   global GLOBAL_Y
   global DIR
   global THETA
   global ROTATE_Y
   global ROTATE_X
  
   glutPostRedisplay()
   if(speed==0):
      return
   glutTimerFunc(int(1000/60),animate,speed)
   GLOBAL_X=GLOBAL_X+speed
   ROTATE_X=(BOB_RADIUS)*math.cos(math.radians(THETA))
   ROTATE_Y=-(BOB_RADIUS)*math.sin(math.radians(THETA))
   if( THETA==360):
      THETA=0
   THETA=THETA+speed
   


def main():
   glutInit(sys.argv)
   glutInitWindowPosition(0,0)
   glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
   glutInitDisplayMode(GLUT_RGB)
   glutCreateWindow("movingcar")
   glutDisplayFunc(drawCar)
   glutIdleFunc(drawCar)
   glutKeyboardFunc(keyboard)
   init()
   glutMainLoop()
main()
