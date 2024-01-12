import math
import time
from OpenGL.GL import*
from OpenGL.GLU import *
from OpenGL.GLUT import *
from random import randint
from pygame import mixer

#mixer.init()
#plays=mixer.Sound('hello.wav')


snows = []
for i in range(-300, 320, 10):
	speed = randint(1,10)	
	snows.append([i,300+randint(1,10), speed])
direction = 1
theta = 0
suntheta = 0
star = 1

      
def init():
  glClearColor(0.678,0.847,0.902,1)
  gluOrtho2D(-300,300,-300,300)
 
 
def circle(x,y,r, color=[1,1,1]):

	glColor3f(color[0],color[1],color[2])
	glLineWidth(2)
	glBegin(GL_TRIANGLE_FAN)
	glVertex2f(x,y)
	for i in range(0,361,1):
		glVertex2f(x+ r*math.cos(math.pi*i/180),y+ r*math.sin(math.pi*i/180))
	glEnd()
	
def poly(coordinate_list, color=[1,1,1]):
  glColor3f(color[0],color[1],color[2])
  glLineWidth(2)
  glBegin(GL_POLYGON)
  for i in coordinate_list:
    glVertex2fv(i)
  glEnd()
  
def line(coordinate_list, color=[1,1,1]):
  glColor3f(color[0],color[1],color[2])
  glLineWidth(5)
  glBegin(GL_LINES)
  glVertex2fv(coordinate_list[0])
  glVertex2fv(coordinate_list[1])
  glEnd()
	
def animate(temp):
  global snows, theta, direction, suntheta, star
  for x in snows:
  	x[1] = x[1] - x[2]
  	if x[1] < -300:
  		x[1] = 300
  		x[2] = randint(1,10)	
  		
  
  theta = theta+0.05*(direction)
  if theta > 0.3:
  	plays.play()
  	direction = -direction
  elif theta < -0.3:
  	direction = -direction
  	
  suntheta = suntheta-0.01
  print(suntheta)
  if suntheta < -0.7:
  	suntheta = 0.1
  	star = -star
  
  glutPostRedisplay()
  glutTimerFunc(100,animate,0)
	
def rotate(x, y, theta, xc=75, yc=65):
	return [(x - xc)*math.cos(theta) - (y-yc)*math.sin(theta) + xc, (x - xc)*math.sin(theta) + (y-yc)*math.cos(theta) + yc]
	
def Man():
	xc = 75
	yc = 65
	global theta, suntheta,star
	
	
	
	glClear(GL_COLOR_BUFFER_BIT)
	circle(0,0,100)
	circle(0,120,60)
	circle(-25,135,5, [0,0,0])
	circle(+25,135,5, [0,0,0])
	poly([(0,115),(0,105),(20,110)], [1,0.647,0])
	circle(0,110,5, [1,0.647,0])
	
	line([rotate(75,65,theta),rotate(130,95,theta)],[0.345,0.223,0.153])
	line([rotate(130,95,theta),rotate(150,70,theta)],[0.345,0.223,0.153])
	line([rotate(130,95,theta),rotate(140,110,theta)],[0.345,0.223,0.153])
	
	line([rotate(-75,65,theta,xc=-75,yc=65),rotate(-130,95,theta,xc=-75,yc=65)],[0.345,0.223,0.153])
	line([rotate(-130,95,theta,xc=-75,yc=65),rotate(-150,70,theta,xc=-75,yc=65)],[0.345,0.223,0.153])
	line([rotate(-130,95,theta,xc=-75,yc=65),rotate(-140,110,theta,xc=-75,yc=65)],[0.345,0.223,0.153])
	
	x = rotate(-300,200,suntheta, xc=0, yc= -700)
	if star==1:
		circle(x[0],x[1],50, [0.082,0.133,0.219])
		circle(x[0]+20,x[1],45, [0.678,0.847,0.902])
	else:
		circle(x[0],x[1],50, [1,0.765,0.043])
	
	for x in snows:
		circle(x[0],x[1],2)
		
	poly([(-300, -90), (300,-90), (300,-300), (-300,-300)], [1,1,1])
	
	glFlush()

	
def main():
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_RGBA)
  glutInitWindowSize(500,500)
  glutInitWindowPosition(600,0)
  glutCreateWindow("SAMPLE")
  glutDisplayFunc(lambda:Man())
  glutTimerFunc(0,animate,0)

  init()
  glutMainLoop()

main()
