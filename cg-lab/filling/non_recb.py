#lekshmeeka p a
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from queue import LifoQueue

ws = 800
point_size = 2
filclr = [1, 0, 0]

def get_pixel(x, y):
    data = glReadPixels(x, ws - y, 1, 1, GL_RGB, GL_FLOAT)
    return [round(x, 1) for x in data[0][0]]

def set_pixel(x, y, fill_color=(0, 0, 0)):
    glColor3f(*fill_color)
    glPointSize(point_size)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()

def plot_rect():
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    gluOrtho2D(0, ws, ws, 0)
    glColor3f(1, 0, 0)
    glLineWidth(point_size)
    
    sqrsize = 200
    xc = ws / 2
    yc = ws / 2
    hf = sqrsize / 2
    
    glBegin(GL_POLYGON)
    glVertex2f(xc - hf, yc - hf)
    glVertex2f(xc + hf, yc - hf)
    glVertex2f(xc + hf, yc + hf)
    glVertex2f(xc - hf, yc + hf)
    glEnd()
    glFlush()

def boundary_fill(x, y, fill_color, boundary_color):
    if fill_color == boundary_color:
        return
    
    stack = LifoQueue()
    stack.put((x, y))
    
    while not stack.empty():
        current_x, current_y = stack.get()
        color = get_pixel(current_x, current_y)
        
        if color != fill_color and color != boundary_color:
            set_pixel(current_x, current_y, fill_color)
            
            if current_y - point_size >= 0:
                stack.put((current_x, current_y - point_size))
            if current_x + point_size < ws:
                stack.put((current_x + point_size, current_y))
            if current_y + point_size < ws:
                stack.put((current_x, current_y + point_size))
            if current_x - point_size >= 0:
                stack.put((current_x - point_size, current_y))

def mouse_click(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        boundary_fill(x, y, [0, 0, 1], filclr)

glutInit()
glutInitWindowSize(ws, ws)
glutCreateWindow("boundary-fill")
glutDisplayFunc(plot_rect)
glutMouseFunc(mouse_click)
glutMainLoop()

