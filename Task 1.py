from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random as rand


def draw_points(x, y):
    glPointSize(5)  # pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x, y)  # jekhane show korbe pixel
    glEnd()



b_color=1.0
h_color=0.0




def draw_house():
    # Roof
    glBegin(GL_TRIANGLES)
    glColor3f(h_color, h_color, h_color)
    glVertex2f(30, 250)
    glVertex2f(250, 350)
    glVertex2f(470, 250)
    glEnd()

    # Roof inside roof
    glBegin(GL_TRIANGLES)
    glColor3f(b_color, b_color, b_color)
    glVertex2f(70, 260)
    glVertex2f(250, 340)
    glVertex2f(430, 260)
    glEnd()

    #House
    glLineWidth(15)
    glBegin(GL_LINES)
    glColor3f(h_color, h_color, h_color)
    glVertex2f(70, 250)  # Left side of house
    glVertex2f(70, 25)
    glVertex2f(430, 250)  # Right side of house
    glVertex2f(430, 25)
    glVertex2f(70, 30)  # Bottom side of the house
    glVertex2f(430, 30)
    glEnd()

    # House
    glLineWidth(2)
    glBegin(GL_LINES)
    glColor3f(h_color, h_color, h_color)
    glVertex2f(120, 30)  # Door
    glVertex2f(120, 150)
    glVertex2f(120, 150)
    glVertex2f(170, 150)
    glVertex2f(170, 150)
    glVertex2f(170, 30)
    glVertex2f(410, 210)  # Window TOP
    glVertex2f(350, 210)
    glVertex2f(350, 210)  # Window LEFT
    glVertex2f(350, 150)
    glVertex2f(350, 150)  # Window Right
    glVertex2f(410, 150)
    glVertex2f(410, 150)  # Window Bottom
    glVertex2f(410, 210)
    glVertex2f(380, 210)  # Window vertical cross
    glVertex2f(380, 150)
    glVertex2f(350, 180)  # Window Horizontal cross
    glVertex2f(410, 180)
    glEnd()

slant=0
def draw_rain(slant):
    for i in range(0, 500, 10):
        x=rand.randint(-70,-40)  # Step skip for random rain
        for j in range(500, 250, x):
            glLineWidth(2)
            glBegin(GL_LINES)
            glColor3f(h_color, h_color, h_color)
            glVertex2f(i, j)
            glVertex2f(i+slant, j+(abs(x+5)))  # Creating separation between 2 rains
            glEnd()




def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClearColor(b_color, b_color, b_color, b_color)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0)  # konokichur color set (RGB)
    # call the draw methods here
    # draw_points(250, 250)
    draw_rain(slant)
    draw_house()
    draw_points(160, 85)

    glutSwapBuffers()


def specialKeyListener(key, x, y):
    global slant
    if key==GLUT_KEY_RIGHT:
        slant += 1
    if key== GLUT_KEY_LEFT:		#// up arrow key
        slant -=1
    glutPostRedisplay()


def keyboardListener(key, x, y):

    global b_color
    global h_color
    if key==b'w':
        if 0.0 < b_color and h_color<1.0:
            b_color -= 0.1
            h_color += 0.1
            glutPostRedisplay()
            print(b_color)
    if key==b's':
        if b_color < 1.0 and 0 < h_color :
            b_color += 0.1
            h_color -= 0.1
            glutPostRedisplay()
            print(b_color)

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)  # window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice")  # window name
glutSpecialFunc(specialKeyListener)
glutKeyboardFunc(keyboardListener)
glutDisplayFunc(showScreen)

glutMainLoop()