from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

x = 0
y = 0
ws = 500
point_size = 2
square_size = 300

def get_pixel(x, y):
    pixel = glReadPixels(x, ws - y, 1, 1, GL_RGB, GL_FLOAT)
    return pixel[0][0]

def set_pixel(x, y, fill_color=(0, 0, 0)):
    glColor3f(*fill_color)
    glPointSize(point_size)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()

def rectangle(vertices, color):
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_POLYGON)
    for vertex in vertices:
        glVertex2f(*vertex)
    glEnd()

def plot_rect():
    glClear(GL_COLOR_BUFFER_BIT)
    gluOrtho2D(0, ws, ws, 0)

    square_center = [ws / 2, ws / 2]

    square_vertices = [
        [square_center[0] - square_size / 2, square_center[1] - square_size / 2],
        [square_center[0] - square_size / 2, square_center[1] + square_size / 2],
        [square_center[0] + square_size / 2, square_center[1] + square_size / 2],
        [square_center[0] + square_size / 2, square_center[1] - square_size / 2]
    ]

    rectangle(square_vertices, [1, 1, 0])
    glFlush()

def scanline_fill(vertices, fill_color):
    min_y = min(vertices, key=lambda vertex: vertex[1])[1]
    max_y = max(vertices, key=lambda vertex: vertex[1])[1]

    for y in range(int(min_y), int(max_y) + 1):
        intersections = []
        for i in range(len(vertices)):
            x1, y1 = vertices[i]
            x2, y2 = vertices[(i + 1) % len(vertices)]
            if (y1 <= y <= y2) or (y1 >= y >= y2):
                if y2 - y1 != 0:
                    x = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
                    intersections.append(x)
        intersections.sort()
        for i in range(0, len(intersections), 2):
            for x in range(int(intersections[i]), int(intersections[i + 1]) + 1):
                set_pixel(x, y, fill_color)

def mouse_click(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        square_center = [ws / 2, ws / 2]
        square_vertices = [
            [square_center[0] - square_size / 2, square_center[1] - square_size / 2],
            [square_center[0] - square_size / 2, square_center[1] + square_size / 2],
            [square_center[0] + square_size / 2, square_center[1] + square_size / 2],
            [square_center[0] + square_size / 2, square_center[1] - square_size / 2]
        ]
        scanline_fill(square_vertices, [0, 1, 1])

glutInit()
glutInitWindowSize(ws, ws)
glutCreateWindow("Scanline Fill")
glutDisplayFunc(plot_rect)
glutMouseFunc(mouse_click)
glutMainLoop()
