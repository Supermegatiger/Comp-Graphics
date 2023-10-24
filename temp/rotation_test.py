from math import *

from OpenGL.GLUT import *
from OpenGL.GL import *



r = 0
c = 0
f = True
def keyboard(k,x,y):
    global r
    if k==GLUT_KEY_LEFT:
        r -= 1
    elif k==GLUT_KEY_RIGHT:
        r+=1
    if abs(r)==20:
        r=0
    print(r)

def smth():
    glBegin(GL_POLYGON)
    for i in range(5):
        # print(0.5 *cos (2 * pi * i / 6), 0.5 * sin (2 * pi *i/6))
        glVertex2f(0.5 *cos (2*pi * i / 5), 0.5 * sin (2*pi *i/5))
    glEnd()
    glColor3f(0,0,0)
    glPointSize(4)
    glBegin(GL_POINTS)
    glVertex2f(-0.2,0)
    glEnd()

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    global c,f
    if c % 2:
        glColor3f(0.5,0,0)
    else:
        glColor3f(0,0.5,0)
    if r%10==5:
        if f:
            c+=1
            f = False
    else:
        f = True

    glLoadIdentity()
    glRotatef(r*18,0,1,0)
    
    smth()

    
    glFlush()


glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

glutInitWindowSize(900, 600)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"My OpenGL Program")
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutSpecialFunc(keyboard)
glutMainLoop()