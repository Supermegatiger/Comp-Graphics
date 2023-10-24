from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *

WIDTH,HEIGHT = 900,600

rotate_y = 0
rotate_x = 0
cube = [(-0.5, -0.5, -0.5), (-0.5, 0.5, -0.5), (0.5, 0.5, -0.5), (0.5, -0.5, -0.5), 's', (0.5, -0.5, 0.5), (0.5, 0.5, 0.5), (-0.5, 0.5, 0.5), (-0.5, -0.5, 0.5), 's', (0.5, -0.5, -0.5), (0.5, 0.5, -0.5), (0.5, 0.5, 0.5), (0.5, -0.5, 0.5), 's', (-0.5, -0.5, 0.5), (-0.5, 0.5, 0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5), 's', (0.5, 0.5, 0.5), (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5), (-0.5, 0.5, 0.5), 's', (0.5, -0.5, -0.5), (0.5, -0.5, 0.5), (-0.5, -0.5, 0.5), (-0.5, -0.5, -0.5)]


def circle(k,x0,y0,z0):
    glColor(0,0,0)
    glBegin(GL_POLYGON)
    for i in range(301):
        angle = 2 * pi * i / 300
        x = cos(angle)
        y = sin(angle)
        glVertex3f(x*k+x0,y*k+y0,z0)
    glEnd()

def drawCube(k,y0,mode):
    if mode == GL_POLYGON:
        glColor3f(1,1,1)
    else:
        glColor3f(0,0,0)
    glBegin(mode)
    for i in cube:
        if i == 's':
            glEnd()
            glBegin(mode)
        else:
            glVertex3f(i[0]*k,i[1]*k+y0,i[2]*k)
    glEnd()

def display():
    
    # clear screen and Z-buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    # reset transformations
    glLoadIdentity()

    # setting perspective view 
    # view angle is 120 degrees, but may be less
    gluPerspective(120, WIDTH/HEIGHT, 0.0001, 100)
    glTranslatef(0,0,-1) # moving away from the object
    glRotatef(180,0,1,0) # to front side 
    # end of setting 


    # rotate when user changes rotate_x and rotate_y
    glRotatef(rotate_x, 1.0, 0.0, 0.0)
    glRotatef(rotate_y, 0.0, 1.0, 0.0)

    # bottom cube
    drawCube(0.5,-0.3,GL_LINE_LOOP)
    drawCube(0.5,-0.3,GL_POLYGON)

    # middle cube
    drawCube(0.4,0.15,GL_LINE_LOOP)
    drawCube(0.4,0.15,GL_POLYGON)

    # top cube
    drawCube(0.3,0.5,GL_LINE_LOOP)
    drawCube(0.3,0.5,GL_POLYGON)

    # eyes
    circle(0.05,0.1,0.52,-0.51*0.3)
    circle(0.05,-0.1,0.52,-0.51*0.3)
    
    # buttons
    circle(0.05,0,0.25,-0.51*0.4)
    circle(0.05,0,0.1,-0.51*0.4)
    circle(0.05,0,-0.15,-0.51*0.5)
    circle(0.05,0,-0.3,-0.51*0.5)
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

    glutCreateWindow(b"Snowman")

    # Enable Z-buffer depth test
    glEnable(GL_DEPTH_TEST)

    glutDisplayFunc(display)
    glutReshapeFunc(resize)
    glutSpecialFunc(specialKeys)

    glutMainLoop()

# Run the main function
if __name__ == "__main__":
    main()
