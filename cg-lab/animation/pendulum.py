"""
PENDULUM

ABHINAND D MANOJ

"""
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Global variables
width, height = 800, 600
angle = 0.0
direction = 1.0

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-2.0, 2.0, -2.0, 2.0)

def draw_pendulum():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glColor3f(1.0, 1.0, 1.0)
    
    # Draw the fixed point
    glPointSize(5.0)
    glBegin(GL_POINTS)
    glVertex2f(0.0, 1.0)
    glEnd()
    
    # Draw the pendulum rod
    glLineWidth(2.0)
    glBegin(GL_LINES)
    glVertex2f(0.0, 1.0)
    glVertex2f(math.sin(angle), 1.0 - math.cos(angle))
    glEnd()
    
    # Draw the pendulum bob
    glTranslatef(math.sin(angle), 1.0 - math.cos(angle), 0)
    glColor3f(0, 0, 1)
    glutSolidSphere(0.1, 20, 20)
    
    glFlush()

def update(value):
    global angle, direction
    angle += 0.01 * direction
    
    if angle >= (math.pi/2-math.pi/4):
        direction = -1.0
    elif angle <= -(math.pi/2-math.pi/4):
        direction = 1.0
    
    glutPostRedisplay()
    glutTimerFunc(10, update, 0)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutCreateWindow("Pendulum Simulation")
    
    init()
    
    glutDisplayFunc(draw_pendulum)
    glutTimerFunc(10, update, 0)
    
    glutMainLoop()

if __name__ == '__main__':
    main()
