from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random as rand

import math


freeze=False
W_Width, W_Height = 500, 500



class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.z = 0
        self.size=7
        self.speedx=rand.choice([-0.01,0.01])
        self.speedy = rand.choice([-0.01, 0.01])
        self.color=(rand.uniform(0.0,1.0),rand.uniform(0.0,1.0),rand.uniform(0.0,1.0))

points=[]



def convert_coordinate(x, y):
    global W_Width, W_Height
    a = x - (W_Width / 2)
    b = (W_Height / 2) - y
    return a, b


def draw_points(x, y, s,c):
    glPointSize(s)  # pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glColor3f(c[0], c[1], c[2])
    glVertex2f(x, y)  # jekhane show korbe pixel
    glEnd()








def specialKeyListener(key, x, y):
    global speed
    if key == 'w':
        print(1)
    if key == GLUT_KEY_UP:
        speed *= 2
        print("Speed Increased")
    if key == GLUT_KEY_DOWN:  # // up arrow key
        speed /= 2
        print("Speed Decreased")
    glutPostRedisplay()

original_colors = []

def mouseListener(button, state, x, y):  # /#/x, y is the x-y of the screen (2D)
    global points, original_colors
    if button == GLUT_LEFT_BUTTON:
        if (state == GLUT_DOWN):
            original_colors = [i.color for i in points]
            for i in points:
                i.color=(0.0,0.0,0.0)
            glutPostRedisplay()
        if (state == GLUT_UP):
            for i, j in zip(points, original_colors):
                i.color=j
            glutPostRedisplay()



    if button == GLUT_RIGHT_BUTTON:
        if state == GLUT_DOWN:
            print(x, y)
            c_X, c_y = convert_coordinate(x, y)
            new_p=point(c_X,c_y)
            points+=[new_p]

    # case GLUT_MIDDLE_BUTTON:
    #     //........

    glutPostRedisplay()


def display():
    # //clear the display
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0, 0, 0, 0);  # //color black
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # //load the correct matrix -- MODEL-VIEW matrix
    glMatrixMode(GL_MODELVIEW)
    # //initialize the matrix
    glLoadIdentity()
    # //now give three info
    # //1. where is the camera (viewer)?
    # //2. where is the camera looking?
    # //3. Which direction is the camera's UP direction?
    gluLookAt(0, 0, 200, 0, 0, 0, 0, 1, 0)
    glMatrixMode(GL_MODELVIEW)
    global points
    for i in points:
        draw_points(i.x, i.y, i.size,i.color)

    glutSwapBuffers()

def animate():
    # //codes for any changes in Models, Camera
    if freeze==False:
        glutPostRedisplay()
        global points, speed
        for i in points:
            x,y=convert_coordinate(i.x, i.y)
            if y>480 or y< 30:
                i.speedy=i.speedy*(-1)
            if i.x>240 or i.x < -240:
                i.speedx = i.speedx * (-1)
            i.x = (i.x + i.speedx)
            i.y = (i.y + i.speedy)


def init():
    # //clear the screen
    glClearColor(0, 0, 0, 0)
    # //load the PROJECTION matrix
    glMatrixMode(GL_PROJECTION)
    # //initialize the matrix
    glLoadIdentity()
    # //give PERSPECTIVE parameters
    gluPerspective(104, 1, 1, 1000.0)
    # **(important)**aspect ratio that determines the field of view in the X direction (horizontally). The bigger this angle is, the more you can see of the world - but at the same time, the objects you can see will become smaller.
    # //near distance
    # //far distance
def specialKeyListener(key, x, y):
    global points

    if key==GLUT_KEY_UP:
        for i in points:
            i.speedx *= 2
            i.speedy *= 2
            print("Speed Increased")
    if key== GLUT_KEY_DOWN:
        for i in points:
            i.speedx /= 2
            i.speedy /= 2
            print("Speed Decreased")
    glutPostRedisplay()

def keyboardListener(key, x, y):

    global freeze
    if key==b' ':
        if freeze==False:
            freeze=True
        else:
            freeze=False





glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)  # //Depth, Double buffer, RGB color

# glutCreateWindow("My OpenGL Program")
wind = glutCreateWindow(b"OpenGL Coding Practice")
init()

glutDisplayFunc(display)  # display callback function
glutIdleFunc(animate)  # what you want to do in the idle time (when no drawing is occuring)

glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)

glutMainLoop()  # The main loop of OpenGL
