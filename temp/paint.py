from math import *

from OpenGL.GLUT import *
from OpenGL.GL import *


# по нажатию лкм рисуются линии
# нажмите s чтобы оборвать ломаную
# нажмите z чтобы отменить последнее действие
# нажмите p чтобы вывести в консоль рисунок

WIDTH,HEIGHT = 900,600
r = 0
points = []

def keyboard(k,x,y):
    global points
    if k==b's':
        if points and points[-1] != 's':
            points.append('s')
    elif k == b'p' and points:
        print(points)
    elif k == b'z' and points:
        points.pop()
    draw()

def skeyboard(k,x,y):
    global r
    if k==GLUT_KEY_LEFT:
        r -= 1
    elif k==GLUT_KEY_RIGHT:
        r+=1
    if abs(r)==4:
        r=0
    draw()
    # print(r)
def mouse(b,state,x,y):
    global points
    if b == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            if not points or points[-1] != (x,y):
                x = x / (WIDTH/2) - 1.0
                y = -1 * (y / (HEIGHT/2) - 1.0)
                points.append((x,y))
                # print(x,y)
    draw()

def resize(w,h):
    global WIDTH,HEIGHT
    WIDTH = w
    HEIGHT = h
    glViewport(0,0,w,h)
    draw()
    # glMatrixMode(GL_PROJECTION)
    # glLoadIdentity()
    # glMatrixMode(GL_MODELVIEW)
    # glLoadIdentity()

def smth(a):
    glColor3f(0,1,0)
    match r:
        case 0:
            glBegin(GL_LINE_STRIP)
            glVertex2f(-a,-a)
            glVertex2f(-a,a*2/3)
            glVertex2f(0,a*1.5)
            glVertex2f(a,a*2/3)
            glVertex2f(a,-a)
            glVertex2f(-a,-a)
            glEnd()
            glBegin(GL_LINE_STRIP)
            glVertex2f(-a,a*2/3)
            glVertex2f(a,a*2/3)
            glEnd()

def paint():
    glColor3f(0,1,0)
    glBegin(GL_LINE_STRIP)
    for i in points:
        if i == 's':
            glEnd()
            glBegin(GL_LINE_STRIP)
        else:
            glVertex2f(i[0],i[1])
    glEnd()
    

def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    # glLoadIdentity()
    # glRotatef(-20,1,0,0)
    # glRotatef(45,0,1,0)
    
    # smth(0.4)
    paint()

    glFlush()


glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

glutInitWindowSize(WIDTH, HEIGHT)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"My OpenGL Program")
glutDisplayFunc(draw)
glutReshapeFunc(resize)
# glutIdleFunc(draw)

glutSpecialFunc(skeyboard)
glutKeyboardFunc(keyboard)
glutMouseFunc(mouse)

glutMainLoop()