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


def translate(points, x, y):
    for i in range(len(points[0])):
        points[0][i] += x
        points[1][i] += y


def rotate(points, angle):
    for i in range(len(points[0])):
        points[0][i] = points[0][i] * cos(rad(angle)) + points[1][i] * sin(rad(angle))
        points[1][i] = points[1][i] * cos(rad(angle)) - points[0][i] * sin(rad(angle))


def reflect(points, axes):
    for i in range(len(points[0])):
        if axes == "x":
            points[1][i] = -points[1][i]
        elif axes == "y":
            points[0][i] = -points[0][i]


def scale(points, x, y):
    for i in range(len(points[0])):
        points[0][i] *= x
        points[1][i] *= y


def shear(points, axes, shear):
    shear /= window_size
    for i in range(len(points[0])):
        if axes == "y":
            points[0][i] = points[0][i] + shear * points[1][i]
        elif axes == "x":
            points[1][i] = points[1][i] + shear * points[0][i]


def composite_transform(points):
    while True:
        option = int(input("Enter transformation type (1-Translate, 2-Rotate, 3-Reflect, 4-Scale, 5-Shear, 0-Exit): "))
        if option == 0:
            break
        elif option == 1:
            x = int(input("Enter X translation: "))
            y = int(input("Enter Y translation: "))
            translate(points, x / window_size, y / window_size)
        elif option == 2:
            angle = float(input("Enter angle: "))
            rotate(points, angle)
        elif option == 3:
            axes = input("Enter reflection axes (x/y): ")
            reflect(points, axes)
        elif option == 4:
            x = int(input("Enter X scale: "))
            y = int(input("Enter Y scale: "))
            scale(points, x / window_size, y / window_size)
        elif option == 5:
            axes = input("Enter shear axes (x/y): ")
            shear_factor = float(input("Enter shear factor: "))
            shear(points, axes, shear_factor)

        plot_points(points)


def main():
    glutInit()
    glutInitWindowSize(window_size, window_size)
    glutCreateWindow("Transformations")
    glutIdleFunc(lambda: plot_points())
    points = ([0.3, 0.3, -0.3, -0.3], [-0.3, 0.3, 0.3, -0.3])  # Default polygon
    composite_transform(points)
    glutMainLoop()


main()
