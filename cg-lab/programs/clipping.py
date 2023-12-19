from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import math , time

WINDOWSIZE=1000
    

def main():
    glutInit(sys.argv)
    glutInitWindowSize(WINDOWSIZE,WINDOWSIZE)
    glutInitDisplayMode(GLUT_RGBA)
    glutCreateWindow("anime tion")

    glutDisplayFunc(drawWaterPipe)
    glutTimerFunc(0,animate,0)
    
    glutIdleFunc(drawWaterPipe)

    glClearColor(0.0,0.0,0.0,0.0)
    gluOrtho2D(-WINDOWSIZE,WINDOWSIZE,-WINDOWSIZE,WINDOWSIZE)

    glutMainLoop()

main()


