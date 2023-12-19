from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import math , random
"""
    - random apple(a single lonely one) appear on screen in (appleX,appleY) coordinates
    - snake boi is in an arbitrary position (snakeX,snakeY) coordinates
    - function finds a way to go eat the apple
    - no.of segments in the snake increase
    - new apple (still single and lonely) appears
"""
WINDOWSIZE=1000 # window size 
timer = 1 # reference timer

appleX , appleY , appleR = 0,0,50
eaten = False # F - not eaten, T - eaten

"""
    ------ ------
    |     |     |
    |  2  |  1  |
    ------ ------
    |     |     |
    |  3  |  4  |
    ------ ------
"""
SnakeQuadrant = 1
appleQuadrant = 1


snakeX,snakeY = -900,-900 # snake coordinates
tailX,tailY = 0,0 # tail coordinates
snakeSegCount = 1 # number of segments of snake
snakeSize = 50 # snake size
direction = 0 # snake direction
"""
                              -----
1 - Up                        |   |
2 - Down                      | 1 |
                        -----------------
3 - Right               |   | |   | |   |
4 - Left                | 4 | | 2 | | 3 |
                        -----------------
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
    global appleX,appleY,eaten
    # get random apple coordinates
    # getting a random x,y between -900 and +900
    appleX = random.randint(-9, 9) * 100
    appleY = random.randint(-9, 9) * 100
    print(f"random apple coords ({appleX},{appleY})")
    eaten = False

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
    #print(f"put-ed apple at ({appleX},{appleY})")


def find_apple_quadrant():
    global appleX,appleY,snakeX,snakeY
    global SnakeQuadrant,appleQuadrant

    if appleX>0:
        if appleY>0:
            appleQuadrant = 1
        elif appleY<0:
            appleQuadrant = 4
    if appleX<0:
        if appleY>0:
            appleQuadrant = 2
        elif appleY<0:
            appleQuadrant = 3
    
    print(f"apple at quadrant ({appleQuadrant})")
    print(f"\t\t snake direction ({direction})")



def snake():
    global tailX,tailY
    glColor3f(0.1,1,1) #magenta? violet? idk 
    glPointSize(snakeSize)
    glBegin(GL_POINTS)
    glVertex2f(snakeX,snakeY)
    glEnd()
    tailX=snakeX
    tailY=snakeY 
    
    for i in range(1,snakeSegCount):
        glColor3f(0.1,1,0) #magenta? violet? idk 
        glPointSize(snakeSize)
        glBegin(GL_POINTS)
        #print(f"snake at ({snakeX},{snakeY})")
        #glVertex2f(tailX-(i*110),tailY)
        if direction == 1:
            glVertex2f(tailX,tailY-(i*110))
        elif direction == 2:
            glVertex2f(tailX,tailY+(i*110))
        elif direction == 3:
            glVertex2f(tailX-(i*110),tailY)
        elif direction == 4:
            glVertex2f(tailX+(i*110),tailY)
        glEnd()





def animate(temp):

    global timer
    global appleX,appleY,appleR,eaten
    global snakeX,snakeY,snakeSegCount,snakeSize
    global tailX,tailY,oldX,oldY,direction

    

    glutPostRedisplay()
    glutTimerFunc(int(50000/60),animate,int(0))

    timer+=1
    print(timer)

    

    if eaten:
        apple_coordinates()
        find_apple_quadrant()

    if snakeX<appleX:
        oldX = snakeX
        snakeX+=100
        direction = 3        
    elif snakeX>appleX:
        oldX = snakeX
        snakeX-=100
        direction = 4    
    elif snakeX==appleX:
        if snakeY<appleY:
            oldY = snakeY
            snakeY+=100
            direction = 1
            
        elif snakeY>appleY:
            oldY = snakeY
            snakeY-=100
            direction = 2
            
        elif snakeY==appleY:
            eaten = True
            snakeSegCount+=1
            print(f"\t\tsnake segment count ({snakeSegCount})")
            print(f"\t\tapple at quadrant ({appleQuadrant})")
    print(f"direction : {direction}") 



    

    
def drawFunction():
    glClear(GL_COLOR_BUFFER_BIT)
    grid()
    apple_putter()
    snake()

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


