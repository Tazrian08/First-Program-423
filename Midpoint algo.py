from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def WritePixel(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()



def findZone(x, y):
    # Find the zone based on the octant
    zone = 0
    dx = abs(x[1] - x[0])
    dy = abs(y[1] - y[0])

    if dx >= dy:
        if x[0] <= x[1]:
            if y[0] <= y[1]:
                zone = 0
            else:
                zone = 7
        else:
            if y[0] <= y[1]:
                zone = 3
            else:
                zone = 4
    else:
        if y[0] <= y[1]:
            if x[0] <= x[1]:
                zone = 1
            else:
                zone = 2
        else:
            if x[0] <= x[1]:
                zone = 6
            else:
                zone = 5
    return zone


def convertToZone0(x, y, zone):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return y, -x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return -y, x
    elif zone == 7:
        return x, -y


def convertFromZone0(x, y, zone):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return -y, x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return y, -x
    elif zone == 7:
        return x, -y


def midpointLineDrawing(x1, y1, x2, y2):
    zone = findZone((x1, x2), (y1, y2))
    x1, y1 = convertToZone0(x1, y1, zone)
    x2, y2 = convertToZone0(x2, y2, zone)

    dx = x2 - x1
    dy = y2 - y1
    d = 2 * dy - dx
    incE = 2 * dy
    incNE = 2 * (dy - dx)
    y = y1

    for x in range(x1, x2 + 1):
        x_orig, y_orig = convertFromZone0(x, y, zone)
        WritePixel(x_orig, y_orig)
        if d > 0:
            d = d + incNE
            y = y + 1
        else:
            d = d + incE
catcher_position=250
def draw_catcher():
    global catcher_position
    # Define catcher dimensions
    catcher_width = 60
    catcher_height = 10
    catcher_x = int(catcher_position - catcher_width / 2)
    catcher_y = 10  # You can adjust the y-coordinate as needed

    # Draw catcher bowl using midpoint line drawing algorithm
    # Bottom line
    midpointLineDrawing(catcher_x, catcher_y, catcher_x + catcher_width, catcher_y)
    # Left side line
    midpointLineDrawing(catcher_x, catcher_y, catcher_x-10, catcher_y + catcher_height)
    # Right side line
    midpointLineDrawing(catcher_x + catcher_width, catcher_y, catcher_x + catcher_width+10, catcher_y + catcher_height)
    # Top line
    midpointLineDrawing(catcher_x-10, catcher_y + catcher_height, catcher_x + catcher_width+10, catcher_y + catcher_height)

def specialKeyListener(key, x, y):
    global catcher_position
    if catcher_position+60+5<=500: #Width of catcher is 60, +10 for the extion of the top line
        if key==GLUT_KEY_RIGHT:
            catcher_position += 10
            print("Move Left")
    if catcher_position-70 >= 0:
        if key== GLUT_KEY_LEFT:
            catcher_position -= 10
            print("Move Right")
    glutPostRedisplay()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(1.0)
    draw_catcher()  # Example line from (0,0) to (250,250)
    glutSwapBuffers()


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(0, 500, 0, 500)



glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"Midpoint Line Drawing")
glutDisplayFunc(display)
glutSpecialFunc(specialKeyListener)
init()
glutMainLoop()




