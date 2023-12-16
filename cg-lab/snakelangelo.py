from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import math , time , random

WINDOWSIZE=1000

timer = 1

appleX , appleY , appleR = 0,0,50
eaten = False # F - not eaten, T - eaten


snakeX,snakeY = 0,0 # snake coordinates
snakeSeg = 1 # number of segments of snake
snakeSize   

"""
    - random apple(a single lonely one) appear on screen in (appleX,appleY) coordinates
    - snake boi is in an arbitrary position (snakeX,snakeY) coordinates
    - function finds a way to go eat the apple
    - no.of segments in the snake increase
    - new apple (still single and lonely) appears
"""
    
def grid(WINDOWSIZE=1000,offset=100):
    glColor3f(0.5,0.5,0.5)
    glLineWidth(1)
    glBegin(GL_LINES)

    for i in range(0,WINDOWSIZE,offset):
        glVertex2f(0+i,WINDOWSIZE)
        glVertex2f(0+i,-WINDOWSIZE)
        glVertex2f(0-i,WINDOWSIZE)
        glVertex2f(0-i,-WINDOWSIZE)
        glVertex2f(WINDOWSIZE,0+i)
        glVertex2f(-WINDOWSIZE,0+i)
        glVertex2f(WINDOWSIZE,0-i)
        glVertex2f(-WINDOWSIZE,0-i)

    glEnd()


def apple_coordinates():
    global appleX,appleY
    # get random apple coordinates
    # getting a random x,y between -900 and +900
    appleX = random.randint(-9, 9) * 100
    appleY = random.randint(-9, 9) * 100
    print(f"random apple coords ({appleX},{appleY})")

def apple_putter():
    #put apple in the coordinates 
    glColor3f(1,0,0) #red color
    glLineWidth(1)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(appleX,appleY)
    for i in range(0,361,1):
        glVertex2f(appleR*math.cos(math.pi*i/180)+appleX,
                   appleR*math.sin(math.pi*i/180)+appleY)
    glEnd()







def animate(temp):

    global timer
    global appleX,appleY,appleR,eaten

    glutPostRedisplay()
    glutTimerFunc(int(5000/60),animate,int(0))

    timer+=1
    print(timer)

    if eaten:
        apple_coordinates()
    

    

    
def drawFunction():
    glClear(GL_COLOR_BUFFER_BIT)
    grid()
    apple_putter()

    glutSwapBuffers()



def main():
    glutInit(sys.argv)
    glutInitWindowSize(WINDOWSIZE,WINDOWSIZE)
    glutInitDisplayMode(GLUT_RGBA)
    glutCreateWindow("Snake'l'Angleo - the game satan introduced to Adam and Eve")

    glutDisplayFunc(drawFunction)
    glutTimerFunc(0,animate,0)
    
    glutIdleFunc(drawFunction)

    glClearColor(0.0,0.0,0.0,0.0)
    gluOrtho2D(-WINDOWSIZE,WINDOWSIZE,-WINDOWSIZE,WINDOWSIZE)

    glutMainLoop()

main()


