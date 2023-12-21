from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import math, random, sys
"""
# road (tarred and rubberized)
#   - straight (add bumps,hill later)
# bicycle (with two tires ofc)
#   - tires with spokes,spins and moves
#   - handle,light n other doodads
"""
WINDOWSIZE_X = 1600
WINDOWSIZE_Y = 900
GRID = True
ROAD_Y = 150
timer = 0

disp = 0

tireFX,tireFY = 300,300 # front tire center
tireBX,tireBY = 850,300 # back tire center
tireR = 150

tireAngle = 0.0
spoX,spoY =0,0

mark = 0 # road marking

treeX,treeY=0,0

def grid(offset=50,GRID=True):
    if GRID:
        glColor3f(0.5,0.5,0.5)
        glLineWidth(1)
        glBegin(GL_LINES)
        for i in range(0,WINDOWSIZE_X,offset):
            glVertex2f(0+i,0)
            glVertex2f(0+i,WINDOWSIZE_Y)
            glVertex2f(0,0+i)
            glVertex2f(WINDOWSIZE_X,0+i)
        glEnd()

def road():
    glColor3f(0.4,0.4,0.2)
    glLineWidth(100)
    glBegin(GL_LINES)
    glVertex2f(0,ROAD_Y)
    glVertex2f(WINDOWSIZE_X,ROAD_Y)
    glEnd()

    glColor3f(1,1,1)
    glLineWidth(10)
    glBegin(GL_LINES)
    glVertex2f(0,ROAD_Y)
    glVertex2f(WINDOWSIZE_X,ROAD_Y)
    glEnd()

    for i in range(0,WINDOWSIZE_X,100):
        glColor3f(0,0,0)
        glLineWidth(10)
        glBegin(GL_LINES)
        glVertex2f(i+mark,ROAD_Y)
        glVertex2f(i+mark+50,ROAD_Y)
        glEnd()


def cycle_frame():
    glColor3f(0.8,0.8,0.8)
    glLineWidth(20)
    glBegin(GL_LINES)
    # front rod
    glVertex2f(750,600)
    glVertex2f(850,300) #front tire center
    # back rod
    glVertex2f(475,600)
    glVertex2f(550,250) #chain sprocket center

    glVertex2f(550,250)
    glVertex2f(300,300)

    glVertex2f(300,300)
    glVertex2f(500,500)

    glVertex2f(500,500)
    glVertex2f(750,600)

    glVertex2f(775,650)
    glVertex2f(550,250)

    glVertex2f(425,625)
    glVertex2f(500,600)

    glVertex2f(750,675)
    glVertex2f(800,625)
    glEnd()

    # middle chain sprocket
    glColor3f(1,1,0) #red color
    glLineWidth(1)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(550,250)
    for i in range(0,361,1):
        glVertex2f(50*math.cos(math.pi*i/180)+550,
                   50*math.sin(math.pi*i/180)+250)
    glEnd()
    # back tire center disc 
    glColor3f(0,1,0) #red color
    glLineWidth(1)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(300,300)
    for i in range(0,361,1):
        glVertex2f(30*math.cos(math.pi*i/180)+300,
                   30*math.sin(math.pi*i/180)+300)
    glEnd()
    #front tire center disc
    glColor3f(0,1,0) #red color
    glLineWidth(1)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(850,300)
    for i in range(0,361,1):
        glVertex2f(30*math.cos(math.pi*i/180)+850,
                   30*math.sin(math.pi*i/180)+300)
    glEnd()

def spocks():
    global disp
    #back wheel spocks
    glColor3f(1,1,1)
    glLineWidth(3)
    glBegin(GL_LINES)
    for i in range(0-disp,361-disp,30):
        glVertex2f(300,300)
        glVertex2f((130)*math.cos(math.pi*i/180)+300,
                   (130)*math.sin(math.pi*i/180)+300)
    glEnd()
    # front wheel spocks
    glColor3f(1,1,1)
    glLineWidth(3)
    glBegin(GL_LINES)
    for i in range(0-disp,361-disp,30):
        glVertex2f(850,300)
        glVertex2f((130)*math.cos(math.pi*i/180)+850,
                   (130)*math.sin(math.pi*i/180)+300)
    glEnd()

def tires():
    # tire Front
    glColor3f(1,1,1) #red color
    glLineWidth(1)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(tireFX,tireFY)
    for i in range(0,361,1):
        glVertex2f(tireR*math.cos(math.pi*i/180)+tireFX,
                   tireR*math.sin(math.pi*i/180)+tireFY)
    glEnd()

    # front tire inner circle
    glColor3f(0,0,0) #red color
    glLineWidth(1)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(tireFX,tireFY)
    for i in range(0,361,1):
        glVertex2f((tireR-15)*math.cos(math.pi*i/180)+tireFX,
                   (tireR-15)*math.sin(math.pi*i/180)+tireFY)
    glEnd()
    # -------------------------------------------------------
    # tire Back
    glColor3f(1,1,1) #red color
    glLineWidth(1)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(tireBX,tireBY)
    for i in range(0,361,1):
        glVertex2f(tireR*math.cos(math.pi*i/180)+tireBX,
                   tireR*math.sin(math.pi*i/180)+tireBY)
    glEnd()
    # back tire inner circle
    glColor3f(0,0,0) #red color
    glLineWidth(1)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(tireBX,tireBY)
    for i in range(0,361,1):
        glVertex2f((tireR-15)*math.cos(math.pi*i/180)+tireBX,
                   (tireR-15)*math.sin(math.pi*i/180)+tireBY)
    glEnd()
    


def tree(height,treWhy):
    # tree trunk 
    # tree canopy
    global treeX,treeY

    treeY = treWhy
    glColor3f(0.6,0.4,0.4)
    glLineWidth(height/10)
    glBegin(GL_LINES)
    # front rod
    glVertex2f(treeX,treeY)
    glVertex2f(treeX,treeY+height)
    glEnd()
    glColor3f(1,1,0)
    glLineWidth(2)
    glBegin(GL_POLYGON)
    glVertex2f(treeX+100,treeY+height)
    glVertex2f(treeX+100,treeY+height+100)
    glVertex2f(treeX-100,treeY+height+100)
    glVertex2f(treeX-100,treeY+height)
    glEnd()

#def sign_board():
    # rectangle square 

#def side_road()

def animate(temp):

    global timer,disp,mark
    global treeX,treeY
    glutPostRedisplay()
    glutTimerFunc(int(10000/60),animate,int(0))

    timer+=1
    print(timer)

    # tire spock displacement , for rotation
    if disp>360:
        disp = 0 
    else:
        disp+=10

    #alternate markings in the road
    if timer%2==0:
        mark=50
    else:
        mark=0
    
    if treeX<0:
        treeX=WINDOWSIZE_X
    else:
        treeX-=30


    
def drawFunction():
    glClear(GL_COLOR_BUFFER_BIT)
    grid()
    road()
    tree(300,200)
    tires()
    spocks()
    cycle_frame()
    
    glutSwapBuffers()



def main():
    glutInit(sys.argv)
    glutInitWindowSize(WINDOWSIZE_X,WINDOWSIZE_Y)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGBA)
    glutCreateWindow("Road-eo loode low cyclo poye")

    glutDisplayFunc(drawFunction)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(drawFunction)

    glClearColor(0.0,0.0,0.0,0.0)
    gluOrtho2D(0,WINDOWSIZE_X,0,WINDOWSIZE_Y)
    glutMainLoop()

main()


