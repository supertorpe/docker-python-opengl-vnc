from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def init_gl():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b'Example')
    glClearColor(1.0, 1.0, 1.0, 1.0);
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(-10, 10, -10, 10)

def square():
    glBegin(GL_POLYGON)
    glColor3f(195/255, 195/255, 195/255)
    glVertex2f(-2, 2)
    glVertex2f(2, 2)
    glVertex2f(2, -2)
    glVertex2f(-2, -2)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    square()
    glFlush()

def main():
    init_gl()
    glutDisplayFunc(display)
    glutMainLoop()

main()
