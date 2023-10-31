from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def init():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Midpoint Ellipse Algorithm")
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-250, 250, -250, 250)

def plot_points(x, y, xc, yc):
    glBegin(GL_POINTS)
    glVertex2f(xc + x, yc + y)
    glVertex2f(xc - x, yc + y)
    glVertex2f(xc + x, yc - y)
    glVertex2f(xc - x, yc - y)
    glEnd()

def midpoint_ellipse(a, b, xc, yc):
    x = 0
    y = b
    p = (b * b) - (a * a) * b + 0.25 * (a * a)

    plot_points(x, y, xc, yc)

    while (2.0 * (b * b) * x) < (2.0 * (a * a) * y):
        x += 1
        if p < 0:
            p += (b * b) * (2 * x + 1)
        else:
            y -= 1
            p += (b * b) * (2 * x + 1) - (a * a) * (2 * y - 1)
        plot_points(x, y, xc, yc)

    p = (b * b) * (x + 0.5) ** 2 + (a * a) * (y - 1) ** 2 - (a * a) * (b * b)

    while y > 0:
        y -= 1
        if p > 0:
            p += (a * a) * (1 - 2 * y)
        else:
            x += 1
            p += (b * b) * (2 * x + 1) + (a * a) * (1 - 2 * y)
        plot_points(x, y, xc, yc)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    midpoint_ellipse(150, 100, 0, 0) # rx,xy,xc,yc
    glFlush()

def main():
    glutInit(sys.argv)
    init()
    glutDisplayFunc(display)
    glutMainLoop()

main()