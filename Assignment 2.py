from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random




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

    x1,x2=int(x1),int(x2)
    for x in range(x1, x2 + 1):
        x_orig, y_orig = convertFromZone0(x, y, zone)
        WritePixel(x_orig, y_orig)
        if d > 0:
            d = d + incNE
            y = y + 1
        else:
            d = d + incE

score=0
over=False
catcher_position=250
dm_pos=random.randint(100,450)
dm_vert=500
catcher_color=(1.0, 1.0, 1.0)
dm_color=(random.uniform(0.5, 1.0), random.uniform(0.5, 1.0), random.uniform(0.5, 1.0))





def draw_catcher():
    global catcher_position, catcher_color
    # Define catcher dimensions
    catcher_width = 60
    catcher_height = 10
    catcher_x = int(catcher_position - catcher_width / 2)
    catcher_y = 10  # You can adjust the y-coordinate as needed

    glColor3f(catcher_color[0],catcher_color[1],catcher_color[2])

    # Draw catcher bowl using midpoint line drawing algorithm
    # Bottom line
    midpointLineDrawing(catcher_x, catcher_y, catcher_x + catcher_width, catcher_y)
    # Left side line
    midpointLineDrawing(catcher_x, catcher_y, catcher_x-10, catcher_y + catcher_height)
    # Right side line
    midpointLineDrawing(catcher_x + catcher_width, catcher_y, catcher_x + catcher_width+10, catcher_y + catcher_height)
    # Top line
    midpointLineDrawing(catcher_x-10, catcher_y + catcher_height, catcher_x + catcher_width+10, catcher_y + catcher_height)



def draw_diamond():
    global dm_pos
    global dm_vert
    # Define catcher dimensions
    dm_width = 10
    dm_height = 5
    dm_x = int(dm_pos - dm_width / 2)
    dm_y = dm_vert  # You can adjust the y-coordinate as needed


    # Draw catcher bowl using midpoint line drawing algorithm
    # Bottom line
    midpointLineDrawing(dm_x, dm_y, dm_x + dm_width//2, dm_y+dm_height)
    # Left side line
    midpointLineDrawing(dm_x + dm_width//2, dm_y+dm_height, dm_x+dm_width, dm_y)
    # Right side line
    midpointLineDrawing(dm_x+dm_width, dm_y, dm_x + dm_width//2, dm_y-dm_height)
    # Top line
    midpointLineDrawing(dm_x + dm_width//2, dm_y-dm_height, dm_x, dm_y)

def specialKeyListener(key, x, y):
    global catcher_position, over
    if over==False:
        if catcher_position+60+5<=500: #Width of catcher is 60, +5 for the extension of the top line
            if key==GLUT_KEY_RIGHT:
                catcher_position += 10
        if catcher_position-70 >= 0:
            if key== GLUT_KEY_LEFT:
                catcher_position -= 10
        glutPostRedisplay()

def animate():

    #//codes for any changes in Models, Camera
    global dm_vert, dm_pos, catcher_position, dm_color, catcher_color, score, over

    if over==False:
        glutPostRedisplay()
        dm_vert-=0.1
        if dm_vert<=20 and catcher_position-40<=dm_pos<=catcher_position+40:
            score+=1
            print(f"Score: {score}")
            dm_pos=random.randint(100,450)
            dm_vert=500
            dm_color = (random.uniform(0.5, 1.0), random.uniform(0.5, 1.0), random.uniform(0.5, 1.0))
        elif dm_vert<=0:
            catcher_color = (1.0, 0.0, 0.0)
            over=True
            print(f"Game Over! Score {score}")




def display():
    global dm_color
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(1.0)
    draw_catcher()  # Example line from (0,0) to (250,250)
    glColor3f(dm_color[0], dm_color[1], dm_color[2])
    draw_diamond()
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
glutIdleFunc(animate)
init()
glutMainLoop()



