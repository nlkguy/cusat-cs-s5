from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import math , time

WINDOWSIZE=1000
    
tx = 1
ty = 1
timer = 1
waterlvl = 1
stonelvl = 300
stone2lvl = 300
stone3lvl = 300

stoneradius = 50
stone2radius = 50
stone3radius = 50
    
def bowl():
    glColor3f(0.5,0.5,0.5)
    glLineWidth(7)
    glBegin(GL_LINES)

    glVertex2f(-100,0)
    glVertex2f(-100,-500)

    glVertex2f(100,0)
    glVertex2f(100,-500)

    glVertex2f(-100,-500)
    glVertex2f(100,-500)
    glEnd()

def crow():
   
    glColor3f(1.0,0.9,0.1)
    glBegin(GL_TRIANGLES)
    glVertex2f(300-tx,400-ty)
    glVertex2f(300-tx,500-ty)
    glVertex2f(150-tx,450-ty)
    glEnd()
    glColor3f(1.0,0.9,0.1)
    glBegin(GL_TRIANGLES)
    glVertex2f(350-tx,300-ty)
    glVertex2f(450-tx,300-ty)
    glVertex2f(450-tx,200-ty)
    glEnd()
    glColor3f(1.0,0.9,0.1)
    glBegin(GL_TRIANGLES)
    glVertex2f(450-tx,300-ty)
    glVertex2f(550-tx,300-ty)
    glVertex2f(450-tx,400-ty)
    glEnd()
    glColor3f(1.0,0.9,0.1)
    glBegin(GL_TRIANGLES)
    glVertex2f(500-tx,100-ty)
    glVertex2f(600-tx,100-ty)
    glVertex2f(550-tx,200-ty)
    glEnd()
    glColor3f(1,0,1)
    glLineWidth(2)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(350-tx,450-ty)
    for i in range(0,361,1):
        glVertex2f(75*math.cos(math.pi*i/180)+350-tx,75*math.sin(math.pi*i/180)+450-ty)
    glEnd()

def fillhalf():
   
    glColor3f(0.2,0.5,1.0)
    glBegin(GL_POLYGON)
    glVertex2f(100,-350)
    glVertex2f(-100,-350)
    glVertex2f(-100,-500)
    glVertex2f(100,-500)
    glEnd()

def fill():
    glColor3f(0.2,0.5,1.0)
    glLineWidth(1)
    glBegin(GL_QUADS)
    glVertex2f(100,-500+waterlvl)
    glVertex2f(-100,-500+waterlvl)
    glVertex2f(-100,-500)
    glVertex2f(100,-500)
    glEnd()

def stone(shift=0):
    glColor3f(0.5,0.5,0.5)
    glLineWidth(1)
    glBegin(GL_LINES)
    theta=0
    while theta<360:
        glVertex(50+shift,stonelvl)
        x1=(stoneradius)*math.cos(math.radians(theta))+50+shift
        y1=(stoneradius)*math.sin(math.radians(theta))+stonelvl
        glVertex2f(x1,y1)
        theta=theta+0.1
    glEnd()
    
def stone2(shift=0):
    glColor3f(0.5,0.5,0.5)
    glLineWidth(1)
    glBegin(GL_LINES)
    theta=0
    while theta<360:
        glVertex(50+shift,stone2lvl)
        x1=(stone2radius)*math.cos(math.radians(theta))+50+shift
        y1=(stone2radius)*math.sin(math.radians(theta))+stone2lvl
        glVertex2f(x1,y1)
        theta=theta+0.1
    glEnd()
    
    
def stone3(shift=0):
    glColor3f(0.5,0.5,0.5)
    glLineWidth(1)
    glBegin(GL_LINES)
    theta=0
    while theta<360:
        glVertex(50+shift,stone3lvl)
        x1=(stone3radius)*math.cos(math.radians(theta))+50+shift
        y1=(stone3radius)*math.sin(math.radians(theta))+stone3lvl
        glVertex2f(x1,y1)
        theta=theta+0.1
    glEnd()
    

def animate(temp):
    global tx,ty,timer,waterlvl,stonelvl,stone2lvl,stone3lvl
    global stoneradius,stone2radius,stone3radius

    glutPostRedisplay()
    glutTimerFunc(int(5000/60),animate,int(0))
    timer+=1
    print(timer)

    if tx<200:
        tx+=10
    elif ty<100:
        ty+=10
    
    if(timer>40 and waterlvl<200):
        waterlvl+=5
        stonelvl-=50
    if(timer>80 and waterlvl<300):
        waterlvl+=5
        stone2lvl-=100
    if(timer>120 and waterlvl<500 and timer<190 ):
        waterlvl+=5
        stone3lvl-=50
        stone2lvl-=50
    

    if(stonelvl==-400):
        stonelvl=0
        stoneradius=0

    if(stone2lvl==-400):
        stone2lvl=0
        stone2radius=0
        
    if(stone3lvl==-400):
        stone3lvl=0
        stone3radius=0

    if(timer<175 and timer>140):
        ty+=10
    if(timer>174 and timer<190):
        waterlvl-=10
def drawWaterPipe():
    glClear(GL_COLOR_BUFFER_BIT)
    crow()
    bowl()
    fillhalf()
    fill()
    stone()
    stone2(-50)
    stone3(-100)
    glutSwapBuffers()



def main():
    glutInit(sys.argv)
    glutInitWindowSize(WINDOWSIZE,WINDOWSIZE)
    glutInitDisplayMode(GLUT_RGBA)
    glutCreateWindow("anime tion")

    glutDisplayFunc(drawWaterPipe)
    glutTimerFunc(0,animate,0)
    
    glutIdleFunc(drawWaterPipe)

    glClearColor(0.0,0.0,0.0,0.0)
    gluOrtho2D(-WINDOWSIZE,WINDOWSIZE,-WINDOWSIZE,WINDOWSIZE)

    glutMainLoop()

main()


