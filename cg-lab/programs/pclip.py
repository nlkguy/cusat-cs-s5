
# NANDULAL KRISHNA
# POLYGON CLIPPING
# 20221097

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time

MAX_POINTS = 20

def x_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    num = (x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)
    den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    return int(num / den)

def y_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    num = (x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)
    den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    return int(num / den)

def clip(poly_points, clipper_points):
    new_points = []
    new_poly_size = 0

    for i in range(len(poly_points)):
        k = (i + 1) % len(poly_points)
        ix, iy = poly_points[i]
        kx, ky = poly_points[k]

        i_pos = (clipper_points[1][0] - clipper_points[0][0]) * (iy - clipper_points[0][1]) - (
                clipper_points[1][1] - clipper_points[0][1]) * (ix - clipper_points[0][0])

        k_pos = (clipper_points[1][0] - clipper_points[0][0]) * (ky - clipper_points[0][1]) - (
                clipper_points[1][1] - clipper_points[0][1]) * (kx - clipper_points[0][0])

        if i_pos < 0 and k_pos < 0:
            new_points.append([kx, ky])
            new_poly_size += 1
        elif i_pos >= 0 and k_pos < 0:
            new_points.append([x_intersect(clipper_points[0][0], clipper_points[0][1], clipper_points[1][0],
                                            clipper_points[1][1], ix, iy, kx, ky),
                               y_intersect(clipper_points[0][0], clipper_points[0][1], clipper_points[1][0],
                                           clipper_points[1][1], ix, iy, kx, ky)])
            new_poly_size += 1
            new_points.append([kx, ky])
            new_poly_size += 1
        elif i_pos < 0 and k_pos >= 0:
            new_points.append([x_intersect(clipper_points[0][0], clipper_points[0][1], clipper_points[1][0],
                                            clipper_points[1][1], ix, iy, kx, ky),
                               y_intersect(clipper_points[0][0], clipper_points[0][1], clipper_points[1][0],
                                           clipper_points[1][1], ix, iy, kx, ky)])
            new_poly_size += 1

    return new_points

def suthHodgClip(poly_points, clipper_points):
    global clip_done
    if not clip_done:
        glColor3f(1.0, 1.0, 1.0)
        glBegin(GL_LINE_LOOP)
        for point in clipper_points:
            glVertex2f(point[0], point[1])
        glEnd()

        glColor3f(1.0, 1.0, 1.0)
        glBegin(GL_LINE_LOOP)
        for point in poly_points:
            glVertex2f(point[0], point[1])
        glEnd()

        glColor3f(1.0, 1.0, 1.0)
        glBegin(GL_LINE_LOOP)
        for i in range(len(clipper_points)):
            k = (i + 1) % len(clipper_points)
            x1, y1 = clipper_points[i]
            x2, y2 = clipper_points[k]
            glVertex2f(x1, y1)
            glVertex2f(x2, y2)
        glEnd()

        for i in range(len(clipper_points)):
            k = (i + 1) % len(clipper_points)
            poly_points = clip(poly_points, [clipper_points[i], clipper_points[k]])

        glColor3f(0.0, 1.0, 0.0)
        glBegin(GL_LINE_LOOP)
        for point in poly_points:
            glVertex2f(point[0], point[1])
        glEnd()

        glutSwapBuffers()
        time.sleep(2) 
        clip_done = True

   
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 1.0, 0.0)  
    glBegin(GL_LINE_LOOP)
    for point in poly_points:
        glVertex2f(point[0], point[1])
    glEnd()

    glutSwapBuffers()

def display():
    glClear(GL_COLOR_BUFFER_BIT)

   
    poly_size = 4
    poly_points = [[100,100], [400, 100], [400, 400],[100,400]]

 
    clipper_size = 4
    clipper_points = [[50, 250], [250, 450], [450,250], [250,50]]

    suthHodgClip(poly_points, clipper_points)

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0,500,0,500)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b'PC')
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glutMainLoop()

if __name__ == "__main__":
    clip_done = False
    main()

