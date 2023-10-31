from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def init():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Midpoint Circle Algorithm")
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-250, 250, -250, 250)

def plot_point(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def midpoint_circle(r):
    x = 0
    y = r
    p = 1 - r 
    while x <= y:
        plot_point(x, y)
        x += 1
        if p <= 0:
            p = p + 2 * x + 1
        else:
            y -= 1
            p = p + 2 * x - 2 * y + 1

        plot_point(x, -y)
        plot_point(-x, y)
        plot_point(-x, -y)
        plot_point(y, x)
        plot_point(-y, x)
        plot_point(y, -x)
        plot_point(-y, -x)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    midpoint_circle(200)
    glFlush()

def main():
    glutInit(sys.argv)
    init()
    glutDisplayFunc(display)
    glutMainLoop()

main()