# from math import *
# import pygame
# from pygame.locals import *
# from OpenGL.GL import *
# from OpenGL.GLU import *

# vertices = ((-1, -1, -1), (-1, 1, -1), (-1, 1, 1), (-1, -1, 1), (1, -1, -1), (1, 1, -1), (1, 1, 1), (1, -1, 1))
# edges = ((0, 1), (0, 3), (0, 4), (1, 2), (1, 5), (2, 3), (2, 6), (3, 7), (4, 5), (4, 7), (5, 6), (6, 7))
# faces = ((0, 1, 2 , 3),(4,  5, 6, 7),(0, 4, 7, 3),(1, 5, 6, 2),(2, 6, 7, 3),(1, 5, 4, 0))

# # =============================================================================
# # vertices = ((1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1), (1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1))
# # edges = ((0, 1), (0, 3), (0, 4), (2, 1), (2, 3), (2, 7), (6, 3), (6, 4), (6, 7), (5, 1), (5, 4), (5, 7))
# # =============================================================================

# def tri(x,y,a,r):
#     glColor3f(1,1,1)
#     c,s = cos(r),sin(r)
#     # def rot(x1,y1):
#     #     return x1*c-y1*s,x1*s+y1*c
#     def rot(x1,y1):
#         # x_rotated = c * (x1) - s * (y1)
#         # y_rotated = s * (x1) + c * (y1)
#         return x1,y1
#     glBegin(GL_POLYGON)
#     glVertex2f(*rot(x,y))
#     glVertex2f(*rot(x-a,y+a))
#     glVertex2f(*rot(x+a,y+a))
#     glEnd()
#     glBegin(GL_POLYGON)
#     glVertex2f(*rot(x,y+2*a))
#     glVertex2f(*rot(x-a*2/3,y-a*2/3))
#     glVertex2f(*rot(x,y))
#     glVertex2f(*rot(x+a*2/3,y-a*2/3))
#     glEnd()

# def draw():
#     glClear(GL_COLOR_BUFFER_BIT)

#     glColor3f(0.8,0.7,0)
#     glBegin(GL_QUADS)
#     glVertex2f(-1,1)
#     glVertex2f(1,1)
#     glVertex2f(1,1/3)
#     glVertex2f(-1,1/3)
#     glEnd()
       
#     glColor3f(0,0,0.8)
#     glBegin(GL_QUADS)
#     glVertex2f(-1,1/3)
#     glVertex2f(1,1/3)
#     glVertex2f(1,-1/3)
#     glVertex2f(-1,-1/3)
#     glEnd()
    
#     glColor3f(0.8,0,0)
#     glBegin(GL_QUADS)
#     glVertex2f(-1,-1/3)
#     glVertex2f(1,-1/3)
#     glVertex2f(1,-1)
#     glVertex2f(-1,-1)
#     glEnd()

#     x = -0.08
#     y = 0.18
#     for i in range(4):
#         glPushMatrix()
#         glRotatef((i+1)*5,0,0,1)
#         tri(x-0.08*i,y-i*0.15,0.05,-(i+1)*22.5)
#         glPopMatrix()
#         glPushMatrix()
#         glRotatef(-(i+1)*5,0,0,1)
#         tri(-x+0.08*i,y-i*0.15,0.05,(i+1)*22.5)
#         glPopMatrix()



#     glFlush

# def Cube():
#     glBegin(GL_QUADS)
#     verts = [(-1, -1, -1), (-1, 1, -1), (-1, 1, 1), (-1, -1, 1)]
#     for vertex in verts:
#         glColor3fv((1, 0, 1))
#         glVertex3fv(vertex)
#     glEnd()

#     # glBegin(GL_LINES)
#     # glColor3fv((1,1,1))
#     # for edge in edges:
#     #     for vertex in edge:
#     #         glVertex3fv(vertices[vertex])
#     # glEnd()

# def Main():
#     pygame.init()
#     screen = (800,600)
#     display = pygame.display.set_mode(screen, DOUBLEBUF|OPENGL)
#     glMatrixMode(GL_PROJECTION)
#     gluPerspective(45, (screen[0] / screen[1]), 0.1, 500)
#     button_down = False

#     glMatrixMode(GL_MODELVIEW)  
#     modelMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

#     while True:
#         glPushMatrix()
#         glLoadIdentity()

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#             # if event.type == pygame.KEYDOWN:
#             #     if event.key == pygame.K_LEFT:
#             #         glTranslatef(-1, 0, 0)
#             #     if event.key == pygame.K_RIGHT:
#             #         glTranslatef(1, 0, 0)
#             #     if event.key == pygame.K_UP:
#             #         glTranslatef(0, 1, 0)
#             #     if event.key == pygame.K_DOWN:
#             #         glTranslatef(0, -1, 0)
#             # if event.type == pygame.MOUSEMOTION:
#             #     if button_down == True:
#             #         glRotatef(event.rel[1], 1, 0, 0)
#             #         glRotatef(event.rel[0], 0, 1, 0)
#                 # print(event.rel)

#         for event in pygame.mouse.get_pressed():
#             # print(pygame.mouse.get_pressed())
#             if pygame.mouse.get_pressed()[0] == 1:
#                 button_down = True
#             elif pygame.mouse.get_pressed()[0] == 0:
#                 button_down = False

#         glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

#         glMultMatrixf(modelMatrix)
#         modelMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

#         glLoadIdentity()
#         glTranslatef(0, 0, -5)
#         glMultMatrixf(modelMatrix)

#         draw()

#         glPopMatrix()
#         pygame.display.flip()
#         pygame.time.wait(10)

# Main()


from math import *

from OpenGL.GLUT import *
from OpenGL.GL import *


def star(a):
    glColor3f(1,1,1)

    glBegin(GL_POLYGON)
    glVertex2f(-a,a)
    glVertex2f(a,a)    
    glVertex2f(0,0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0,0)
    glVertex2f(-a*0.6,-a*0.6)
    glVertex2f(0,2*a)
    glVertex2f(a*0.6,-a*0.6)    
    glEnd()

def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1,0.8,0)
    glBegin(GL_QUADS)
    glVertex2f(-1,1)
    glVertex2f(1,1)
    glVertex2f(1,1/3)
    glVertex2f(-1,1/3)
    glEnd()

    glColor3f(0,0.13,0.45)
    glBegin(GL_QUADS)
    glVertex2f(-1,1/3)
    glVertex2f(1,1/3)
    glVertex2f(1,-1/3)
    glVertex2f(-1,-1/3)
    glEnd()
    
    glColor3f(0.8,0,0)
    glBegin(GL_QUADS)
    glVertex2f(-1,-1/3)
    glVertex2f(1,-1/3)
    glVertex2f(1,-1)
    glVertex2f(-1,-1)
    glEnd()

    x = 0.08
    y = 0.18
    coords = [(0.07,0.16),(0.18,0.08),(0.26,-0.04),(0.35,-0.22)]
    angles = [10,36,62,-1]
    for i in range(4):
        glLoadIdentity()
        glPushMatrix()
        x,y = coords[i]
        glTranslatef(x,y,0)
        glRotatef(-angles[i],0,0,1)
        star(0.06)
        glPopMatrix()
        glPushMatrix()
        glTranslatef(-x,y,0)
        glRotatef(angles[i],0,0,1)
        star(0.06)
        glPopMatrix()


    glFlush()


glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(900, 600)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"My OpenGL Program")
glutDisplayFunc(draw)
glutMainLoop()