import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def init():
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(-300, 300, -300, 300)

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 0, 1)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0, 0)
    for angle in range(0, 360):
        x = 50 * math.cos(math.radians(angle))
        y = 50 * math.sin(math.radians(angle))
        glVertex2f(x, y)
    glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500, 500)
    glutCreateWindow("SAMPLE")
    glutDisplayFunc(draw)
    init()
    glutMainLoop()

if __name__ == "__main__":
    main()
