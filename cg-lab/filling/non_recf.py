#lekshmeeka p a
#
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from queue import Queue
import numpy as np

x = 0
y = 0
ws = 500
point_size = 2

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
    square_size = 200

    square_vertices = [
        [square_center[0] - square_size / 2, square_center[1] - square_size / 2],
        [square_center[0] - square_size / 2, square_center[1] + square_size / 2],
        [square_center[0] + square_size / 2, square_center[1] + square_size / 2],
        [square_center[0] + square_size / 2, square_center[1] - square_size / 2]
    ]

    rectangle(square_vertices, [1, 0, 0])

    glFlush()

def flood_fill(x, y, new_color, old_color):
    if np.all(new_color == old_color) or not np.all(get_pixel(x, y) == old_color):
        return

    queue = Queue()
    queue.put((x, y))

    while not queue.empty():
        current_x, current_y = queue.get()
        if np.all(get_pixel(current_x, current_y) == old_color):
            set_pixel(current_x, current_y, new_color)
            queue.put((current_x + point_size, current_y))
            queue.put((current_x, current_y + point_size))
            queue.put((current_x - point_size, current_y))
            queue.put((current_x, current_y - point_size))

def mouse_click(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        flood_fill(x, y, [0, 0, 1], get_pixel(x, y))

glutInit()
glutInitWindowSize(ws, ws)
glutCreateWindow("flood fill")
glutDisplayFunc(plot_rect)
glutMouseFunc(mouse_click)
glutMainLoop()

