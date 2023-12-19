from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import cos, sin, radians as rad

window_size = 500


def plot_points(points=([.3, .3, -.3, -.3], [-.3, .3, .3, -0.3])):
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POLYGON)
    for x, y in zip(points[0], points[1]):
        glVertex2f(x, y)
    glEnd()
    glFlush()
    option = int(input("enter 1-translation 2-rotation 3-reflection 4-scaling 5-shearing"))
    if option == 1:
        x = int(input("enter x inc")) / window_size
        y = int(input("enter y inc")) / window_size
        for i in range(len(points[0])):
            points[0][i] += x
            points[1][i] += y
    elif option == 2:
        angle = float(input("enter angle"))
        for i in range(len(points[0])):
            points[0][i] = points[0][i] * cos(rad(angle)) + points[1][i] * sin(rad(angle))
            points[1][i] = points[1][i] * cos(rad(angle)) - points[0][i] * sin(rad(angle))
    elif option == 3:
        axes = input("enter x axis or y axis (x/y) :")
        for i in range(len(points[0])):
            if axes == "x":

                points[1][i] = -points[1][i]
            elif axes == "y":
                points[0][i] = -points[0][i]
    elif option == 4:
        x = int(input("enter x scale")) / window_size
        y = int(input("enter y scale")) / window_size
        for i in range(len(points[0])):
            points[0][i] *= x
            points[1][i] *= y
    elif option == 4:
        x = int(input("enter x scale")) / window_size
        y = int(input("enter y scale")) / window_size
        for i in range(len(points[0])):
            points[0][i] *= x
            points[1][i] *= y
    elif option == 5:
        axes = input("enter x shear or y shear (x/y) :")
        shear = float(input("Enter shear"))/window_size
        for i in range(len(points[0])):
            if axes == "y":
                points[0][i] = points[0][i] + shear * points[1][i]
            elif axes == "x":
                points[1][i] = points[1][i] + shear * points[0][i]


def main():
    glutInit()
    glutInitWindowSize(window_size, window_size)
    glutCreateWindow("transformations")
    glutIdleFunc(plot_points)
    glutMainLoop()


main()