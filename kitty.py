from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *

WIDTH,HEIGHT = 900,600
fovy = 120
#######################################
# push p to switch view (perspective) #
# click + to zoom in in p. mode       #
# click - to zoom out in p. mode      #
#######################################

p = False
rotate_y = 0
rotate_x = 0


def initLightning():
    glShadeModel(GL_SMOOTH)
    glEnable(GL_LIGHTING)
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, (0.5, 0.5, 0.5, 1))
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, (0, 1, -1 + p))


def drawCube2(a, mode):
    glBegin(mode)
    glVertex3f(a, a, a)
    glVertex3f(-a, a, a)
    glVertex3f(-a, -a, a)
    glVertex3f(a, -a, a)
    glEnd()
    glBegin(mode)
    glVertex3f(a, a, -a)
    glVertex3f(a, -a, -a)
    glVertex3f(-a, -a, -a),
    glVertex3f(-a, a,-a)
    glEnd()
    glBegin(mode)
    glVertex3f(-a, a, a)
    glVertex3f(-a, -a, a)
    glVertex3f(-a, -a, -a)
    glVertex3f(-a, a, -a)
    glEnd()
    glBegin(mode)
    glVertex3f(a, a, a)
    glVertex3f(a, -a, a)
    glVertex3f(a, -a, -a)
    glVertex3f(a, a,-a)
    glEnd()
    glBegin(mode)
    glVertex3f(-a, a, -a)
    glVertex3f(-a, a, a)
    glVertex3f(a, a, a)
    glVertex3f(a, a, -a)
    glEnd()
    glBegin(mode)
    glVertex3f(-a, -a, -a)
    glVertex3f(a, -a, -a)
    glVertex3f(a, -a, a)
    glVertex3f(-a, -a, a)
    glEnd() 

def ear(a):
    glRotatef(90, 1, 0, 0)
    glRotatef(180, 0, 1, 0)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (0.5, 0.2, 0.4, 0))
    glutSolidCone(0.11*a, 0.2*a, 10, 10)
    glTranslatef(0, 0.031*a, 0)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (0, 0, 0, 0))
    glutSolidCone(0.13*a, 0.3*a, 10, 10)

def temp(a):
    glBegin(GL_LINE_STRIP)
    glVertex3f(0, 0, -0.3)
    glVertex3f(a*0.01, -0.02, -0.3)
    glVertex3f(a*0.03, -0.03, -0.3)
    glEnd()

def display():
    # clear screen and Z-buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    # reset transformations
    glLoadIdentity()
    glRotatef(-20, 1, 0, 0)

    if p:
        # setting perspective view 
        # fovy (view angle) is 120 degrees here, but may be less
        gluPerspective(fovy, WIDTH/HEIGHT, 0.0001, 100)
        glTranslatef(0,0,-1) # moving away from the object
        glRotatef(180,0,1,0) # to front side 
        # end of setting 

    initLightning()
    
    # rotate when user changes rotate_x and rotate_y
    glRotatef(rotate_x, 1.0, 0.0, 0.0)
    glRotatef(rotate_y*(-1)**p, 0.0, 1.0, 0.0)

    # head
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (0, 0, 0, 1))
    gluSphere(gluNewQuadric(), 0.3, 20, 20)

    # eyes
    glPushMatrix()
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (0, 0.5, 0, 1))
    glTranslatef(-0.1,0.1,-0.11)
    gluSphere(gluNewQuadric(), 0.14, 10, 10)
    glTranslatef(0.2,0,0)
    gluSphere(gluNewQuadric(), 0.14, 10, 10)
    glPopMatrix()
    
    # pupils
    glPushMatrix()
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (0, 0, 0, 1))
    glRotatef(40, 1, 0, 0)
    glScale(1, 3, 1)
    glTranslatef(-0.15, 0.003, -0.261)
    gluSphere(gluNewQuadric(), 0.02, 10, 10)
    glTranslatef(0.3,0,0)
    gluSphere(gluNewQuadric(), 0.02, 10, 10)
    glPopMatrix()

    # ears   
    glPushMatrix()
    glTranslatef(-0.15, 0.19, 0.1)
    glRotatef(40, 0, 0, 1)
    glRotatef(35, 1, 0, 0)
    ear(0.9)
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(0.15, 0.19, 0.1)
    glRotatef(-40, 0, 0, 1)
    glRotatef(35, 1, 0, 0)
    ear(0.9)
    glPopMatrix()
    
    # nose
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (0.5, 0.2, 0.4, 0))
    glPushMatrix()
    glTranslatef(0, 0.1, -0.283)
    glRotatef(20, 1, 0, 0)
    k = 0.04
    glBegin(GL_POLYGON)
    glVertex3f(-k, 0, 0)
    glVertex3f(k, 0, 0)
    glVertex3f(0, -k, 0)
    glEnd()
    glPopMatrix()

    # mouth
    glEnable(GL_LINE_SMOOTH)
    glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)
    glPushMatrix()
    glBegin(GL_LINE_STRIP)
    glVertex3f(0, 0.01, -0.3)
    glVertex3f(0, 0, -0.3)
    glEnd()
    temp(1)
    temp(-1)
    glPopMatrix()

    glFlush()
    glutSwapBuffers()


def specialKeys(key, x, y):
    global rotate_x, rotate_y

    if key == GLUT_KEY_RIGHT:
        rotate_y += 5

    elif key == GLUT_KEY_LEFT:
        rotate_y -= 5

    elif key == GLUT_KEY_UP:
        rotate_x += 5

    elif key == GLUT_KEY_DOWN:
        rotate_x -= 5

    glutPostRedisplay()


def keyboard(key, x, y):
    global p,fovy
    if key == b'p':
        p = not p
    elif key == b'+':
        fovy -= 10
    elif key == b'-':
        fovy += 10
    glutPostRedisplay()

def resize(w,h):
    global WIDTH,HEIGHT
    WIDTH = w
    HEIGHT = h
    glViewport(0,0,w,h)
    display()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(WIDTH, HEIGHT)

    glutCreateWindow(b"Kitty")
    # glClearColor(1,1,1,1)

    # Enable Z-buffer depth test
    glEnable(GL_DEPTH_TEST)
    glutDisplayFunc(display)
    glutReshapeFunc(resize)
    glutSpecialFunc(specialKeys)
    glutKeyboardFunc(keyboard)

    glutMainLoop()

# Run the main function
if __name__ == "__main__":
    main()
