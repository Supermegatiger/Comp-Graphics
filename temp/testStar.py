from math import *

from OpenGL.GLUT import *
from OpenGL.GL import *

r = 0
WIDTH,HEIGHT = 900,600


def skeyboard(k,x,y):
    global r
    if k==GLUT_KEY_LEFT:
        if not r:
            r=8
        r -= 1
    elif k==GLUT_KEY_RIGHT:
        r+=1
    if abs(r)==8:
        r=0
    draw()
    # print(r)

def star():
    glBegin(GL_LINE_STRIP)
    for t in range(20):
        x = cos(t) + 2*(cos(2*t/3))
        y = sin(t) - 2*(sin(2*t/3))
        glVertex2f(x*50/WIDTH,y*50/HEIGHT)
    glEnd()


def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    glLoadIdentity()
    # glRotatef(-20,1,0,0)
    # glRotatef(45,0,1,0)
    
    # smth(0.4)
    glPushMatrix()
    glRotatef(360*r/8,0,0,1)
    star()
    glPopMatrix()
    
    glFlush()

def resize(w,h):
    global WIDTH,HEIGHT
    WIDTH = w
    HEIGHT = h
    glViewport(0,0,w,h)
    # glMatrixMode(GL_PROJECTION)
    # glLoadIdentity()
    # glMatrixMode(GL_MODELVIEW)
    # glLoadIdentity()


glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

glutInitWindowSize(WIDTH, HEIGHT)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"My OpenGL Program")
glutDisplayFunc(draw)
glutReshapeFunc(resize)
#glutIdleFunc(draw)

glutSpecialFunc(skeyboard)
# glutKeyboardFunc(keyboard)
# glutMouseFunc(mouse)

glutMainLoop()