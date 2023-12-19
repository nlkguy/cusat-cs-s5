from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import sys

x1, y1, x2, y2 = 100, 100, 100, 300

def init():
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(0, 500, 0, 500)

def plot_pixel(x, y):
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()

def dda_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)

    x_increment = dx / float(steps)
    y_increment = dy / float(steps)

    x = x1
    y = y1

    plot_pixel(round(x), round(y))

    for _ in range(steps):
        x += x_increment
        y += y_increment
        plot_pixel(round(x), round(y))

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 0, 1)
    dda_line(x1, y1, x2, y2)
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(600, 0)
    glutCreateWindow("DDA Line Drawing")
    glutDisplayFunc(draw)
    init()
    glutMainLoop()

if __name__ == "__main__":
    main()
