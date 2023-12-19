from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


# Window dimensions
width, height = 800, 600

def draw_line(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    x_increment = 1 if x0 < x1 else -1
    y_increment = 1 if y0 < y1 else -1
    p = 2 * dy - dx

    x, y = x0, y0

    glBegin(GL_POINTS)
    while x != x1:
        glVertex2f(x, y)
        if p >= 0:
            y += y_increment
            p -= 2 * dx
        x += x_increment
        p += 2 * dy
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)  # Set color to white
    glPointSize(1.0)  # Set point size

    draw_line(100, 100, 700, 500)  # Example line coordinates

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutCreateWindow("Bresenham's Line Drawing Algorithm")

    glClearColor(0.0, 0.0, 0.0, 0.0)  # Set background color to black
    gluOrtho2D(0, width, 0, height)
    glutDisplayFunc(display)
    
    glutMainLoop()

if __name__ == "__main__":
    main()
