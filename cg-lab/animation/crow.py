from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

window_size = 800
x_ref = 0
y_ref = 0


def clear_screen():
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(-window_size, window_size, -window_size, window_size)
    # glClear(GL_COLOR_BUFFER_BIT)


def circle(x, y, r):
    glColor3f(1, 1, 0)
    glPointSize(1)
    glBegin(GL_LINES)
    for i in range(0, 360, 1):
        glVertex2f(x, y)
        glVertex2f(x + r * math.cos(math.radians(i)), y + r * math.sin(math.radians(i)))
    glEnd()


def hand():
    global x_ref, y_ref
    glLineWidth(5)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 1, 0)
    x = 200 + 200 * abs(math.cos(math.radians(x_ref)))
    y = 300 * math.sin(math.radians(x_ref))

    glBegin(GL_LINES)
    glVertex2f(0, 0)
    glVertex2f(x, y)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(0, 0)
    glVertex2f(-x, y)
    glEnd()
    
    circle(x, y, 20)
    circle(-x, y, 20)


def man():
    hand()


def display():
    global x_ref, y_ref
    x_ref += .05
    man()

    glFlush()


def main():
    glutInit()
    glutInitWindowSize(window_size, window_size)
    glutCreateWindow("Point")
    glutDisplayFunc(display)
    glutIdleFunc(display)
    clear_screen()
    glutMainLoop()


if __name__ == '__main__':
    main()