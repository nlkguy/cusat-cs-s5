from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys,math,random
sys.setrecursionlimit(100000)

WS = 900 # window size
timer = 1
# egg
# crack
# fragments
# hatchling

eggX,eggY = 300,300
eggR = 100
cY,cX = 0,0

frag = False

x,y=0,0
fragColor = [1,1,0.7]

lineW = 1
crackX,crackY = 0,0


chickX,chickY = 0,0


def egg():
	glColor3f(1,1,1)
	glPointSize(2)
	glLineWidth(2)
	glBegin(GL_TRIANGLE_FAN)
	glVertex2f(eggX,eggY)
	for i in range(0,361,1):
		glVertex2f(eggR*math.cos(3.14*i/180)+eggX,
		eggR*math.sin(3.14*i/180)+eggY)
	glEnd()
	"""
	glColor3f(1,1,0.7)
	glPointSize(2)
	glLineWidth(2)
	glBegin(GL_TRIANGLE_FAN)
	glVertex2f(eggX,eggY)
	for i in range(0,361,1):
		glVertex2f(98*math.cos(3.14*i/180)+eggX,
		98*math.sin(3.14*i/180)+eggY)
	glEnd()"""
	
	
def fragments(fA1,fB1,fA2,fB2,fA3,fB3):
	glColor3f(*fragColor) # note : eggish hue color
	glPointSize(2)
	glLineWidth(2)
	glBegin(GL_TRIANGLES)
	glVertex2f(fA1,fB1)
	
	glVertex2f(fA2,fB2)
	glVertex2f(fA3,fB3)
	glEnd()
	
def crack(): #crA1,crB1,crA1,crB2
	glColor3f(0,0,0)
	glPointSize(2)
	glLineWidth(int(lineW))
	glBegin(GL_LINES)
	#glVertex2f(crA1,crB1)
	#glVertex2f(crA2,crB2)
	glVertex2f(300,400)
	glVertex2f(250,350)
	
	glVertex2f(250,350)
	glVertex2f(300,300)
	
	
	glVertex2f(300,300)
	glVertex2f(250,250)
	
	glVertex2f(250,250)
	glVertex2f(300,200)
	
	glEnd()

def chick():
	#head circle
	#body circle
	#limbs lines
	#beak triangle
	
	#body
	bodyX = eggX+cX
	bodyY = eggY-20+cY
	glColor3f(1,1,0.6)
	glPointSize(2)
	glLineWidth(2)
	glBegin(GL_TRIANGLE_FAN)
	glVertex2f(bodyX,bodyY)
	for i in range(0,361,1):
		glVertex2f((50)*math.cos(3.14*i/180)+bodyX,
		(50)*math.sin(3.14*i/180)+bodyY)
	glEnd()
	
	# head
	headX = eggX+cX
	headY = eggY+30+cY
	glColor3f(1,1,0.3)
	glPointSize(2)
	glLineWidth(2)
	glBegin(GL_TRIANGLE_FAN)
	glVertex2f(headX,headY)
	for i in range(0,361,1):
		glVertex2f((30)*math.cos(3.14*i/180)+headX,
		(30)*math.sin(3.14*i/180)+headY)
	glEnd()
	
	#limbs
	
	
	# beak
	
	
	
	glColor3f(1,0,0)
	glPointSize(2)
	glLineWidth(2)
	glBegin(GL_TRIANGLES)
	glVertex2f(headX+30+cX,headY+10+cY)
	glVertex2f(headX+30+cX,headY-10+cY)
	glVertex2f(headX+40+cX,headY-5+cY)
	glEnd()
	
	

def getPixel(x,y):
	clr = glReadPixels(x,y,1,1,GL_RGB,GL_FLOAT,None)[0][0]
	print(f"get pixel color {clr}")
	return clr
	
	
def setPixel(x,y,fillcolor):
	glColor3f(*fillcolor)
	glPointSize(2)
	glLineWidth(2)
	glBegin(GL_POINTS)
	glVertex2f(x,y)
	glEnd()
	
def boundaryfill(x,y,fillcolor,boundarycolor):
	print("inside bfil func")
	currentcolor = getPixel(x,y)
	print(f"curr_color {currentcolor}")
	if all (currentcolor != fillcolor) :
		print("inside if 1")
		if all (currentcolor != boundarycolor):
			print("inside if 2")
			setPixel(x,y,fillcolor)
			boundaryfill(x+2,y,fillcolor,boundarycolor)
			boundaryfill(x,y+2,fillcolor,boundarycolor)
			boundaryfill(x-2,y,fillcolor,boundarycolor)
			boundaryfill(x,y-2,fillcolor,boundarycolor)

def boundaryfillx(x,y,fillcolor,oldcolor):
	print("inside bfil XXX func")
	currentcolor = getPixel(x,y)
	print(f"curr_color {currentcolor}")
	if all (currentcolor == oldcolor) :
		print("inside if 2")
		setPixel(x,y,fillcolor)
		boundaryfill(x+2,y,fillcolor,oldcolor)
		boundaryfill(x,y+2,fillcolor,oldcolor)
		boundaryfill(x-2,y,fillcolor,oldcolor)
		boundaryfill(x,y-2,fillcolor,oldcolor)


def click(button,state,x,y):
	if button==GLUT_LEFT_BUTTON and state == GLUT_DOWN:
		boundaryfillx(300,300,[0.,0.,1.],[1.,1.,0.69803923])
		#boundaryfill(x,y,[0,0,1],[1,1,1])

def draw():
	glClear(GL_COLOR_BUFFER_BIT)
	chick()
	egg()
	crack()
	if frag:
		fragments(100,100,150,150,200,100)
		fragments(150,100,200,130,230,110)
		fragments(90,90,150,100,200,50)
	
	
	glutSwapBuffers()
	
	
def animate(temp):
	global timer,lineW,cY,cX,frag
	print(f"ref timer: {timer}")
	timer+=1
	
	if timer>3:
		lineW+=10
	if timer>6 and timer<12:
		cY+=50
		frag = True
		
	if timer>12 and timer<17:
		cX+=100
	if timer>17 and timer<20:
		cY-=50
		cX-=100

	glutPostRedisplay()
	glutTimerFunc(1000,animate,0)
	
	

def main():
	glutInit(sys.argv)
	glutInitWindowSize(WS,WS)
	glutCreateWindow("eggilicious")
	gluOrtho2D(0,WS,0,WS)
	glutDisplayFunc(draw)
	glutTimerFunc(0,animate,0)
	glutMouseFunc(click)
	glutMainLoop()
	
main()
