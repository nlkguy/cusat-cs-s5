from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
sys.setrecursionlimit(100000)

x = 0
y = 0
ws= 500
point_size = 2



def get_pixel(x, y):
    pixel = glReadPixels(x, ws -y, 1, 1, GL_RGB, GL_FLOAT)
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


""" def plot_rect():
    glClear(GL_COLOR_BUFFER_BIT)
    # for shifting coordinate from ordinary to first quadrant with x and y maximum is window size
    gluOrtho2D(0, ws, ws, 0)
    rectangle(
        [[-ws/2, -ws/2],[-ws/2, ws/2],[ws/2, ws/2],[ws/2, -ws/2]],
        [1, 1, 0]
    )
    glFlush() 
"""

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
    
    rectangle(square_vertices, [1, 1, 0])
    
    glFlush()



def flood_fill(x, y, new_color, old_color):
    color = get_pixel(x, y)
    if all(color == old_color):
        set_pixel(x, y, new_color)
        flood_fill(x + point_size, y, new_color, old_color)
        flood_fill(x, y + point_size, new_color, old_color)
        flood_fill(x - point_size, y, new_color, old_color)
        flood_fill(x, y - point_size, new_color, old_color)


def mouse_click(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        flood_fill(x, y, [0, 1, 1], get_pixel(x, y))




glutInit()
glutInitWindowSize(ws, ws)
glutCreateWindow("fahad fasil")
glutDisplayFunc(plot_rect)
glutMouseFunc(mouse_click)
glutMainLoop()


