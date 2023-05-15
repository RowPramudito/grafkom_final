from tkinter import *
from tkinter import ttk, messagebox
import turtle
from turtle import TurtleScreen, RawTurtle


# membuat kotak2 pixel
def draw_rectangle(t, x, y):
    angle = 90
    t.penup()
    t.goto(x, y)
    t.pendown()
    for i in range(4):
        t.forward(1)
        t.left(angle)

    t.penup()

def DDA(x1,y1,x2,y2):
	
    points = []
        
    dx = abs(x2-x1)
    dy = abs(y2-y1)
    length = max(dx,dy) 
    
    dx = (x2-x1)/length
    dy = (y2-y1)/length
        
    x=x1
    y=y1

    for i in range(length+1):
        # print(round(x),round(y))
        points.append((x, y))
        x = x+dx
        y = y+dy
    
    print(points)
    return points
	

def bresenham(x1,y1,x2,y2):
    points = []
    dx = abs(x2-x1)
    dy = abs(y2-y1)

    if x1 > x2:
        x = x2
        y = y2
        xEnd = x1
    else:
        x = x1
        y = y1
        xEnd = x2

    P = 2*dy-dx

    while x < xEnd:
        if P<0:
            P = P+2*dy
            x = x+1
        else:
            P = P+2*dy-2*dx
            x = x+1
            y = y+1

        points.append((x, y))
    
    print(points)
    return points


def mid_point_circle(origin_x, origin_y, radius, step=10):
    points = []
    full_circle = []

    x = 0
    y = radius
    points.append((x + origin_x, y + origin_y))
    p = step - radius

    while x < y:
        if p < 0:
            x = x + step
            p = p + (2 * x) + step
        else:
            x = x + step
            y = y - step
            p = p - (2 * y) + (2 * x) + step
        points.append((x + origin_x, y + origin_x))

    full_circle.extend(points)
    full_circle.extend([(b, a) for (a, b) in points])
    full_circle.extend([(b, -a) for (a, b) in points])
    full_circle.extend([(a, -b) for (a, b) in points])
    full_circle.extend([(-a, -b) for (a, b) in points])
    full_circle.extend([(-b, -a) for (a, b) in points])
    full_circle.extend([(-b, a) for (a, b) in points])
    full_circle.extend([(-a, b) for (a, b) in points])
    return full_circle

# membuat lingkaran
def draw_circle(radius):
    for x, y in mid_point_circle(0, 0, radius, 1):
        draw_rectangle(ttl, x, y)

#membuat garis
def draw_line():
    for x, y in DDA(0, 0, 0, 100):
        draw_rectangle(ttl, x, y)

def draw_triangle():
    points = []

    ground = DDA(0, 0, 100, 0)
    points.extend(ground)

    side1 = DDA(0, 0, 50, 87)
    points.extend(side1)

    side2 = DDA(50, 87, 100, 0)
    points.extend(side2)

    print(points)

    for x, y in points:
        draw_rectangle(ttl, x, y)

def draw_box():
    points = []

    ground = DDA(0, 0, 100, 0)
    points.extend(ground)

    side1 = DDA(0, 0, 0, 100)
    points.extend(side1)
    
    side2 = DDA(100, 0, 100, 100)
    points.extend(side2)

    top = DDA(0, 100, 100, 100)
    points.extend(top)

    for x, y in points:
        draw_rectangle(ttl, x, y)


if __name__ == '__main__':

    #setup window
    root = Tk()
    root.geometry('840x560')
    root.title('Program Grafika')
    root['background']='#d9d9d9'

    #setup canvas
    canvas = Canvas(root, width=480, height=360)
    canvas.grid(row=0, column=1, columnspan=6, pady=20, padx=20)

    #set turtle di canvas
    screen = TurtleScreen(canvas)
    ttl = RawTurtle(screen, visible=FALSE)
    screen.tracer(0)

    btn_style = ttk.Style()
    btn_style.configure('TButton', background='white')

    # menu membuat buat objek
    label_make = Label(root, 
                       text='Buat Objek', 
                       background='#d9d9d9',
                       font=('Arial', 14)).place(x=520, y=60)
    button_lingkaran = ttk.Button(root, text='lingkaran', style='TButton', width=20, 
                                  command=lambda: draw_circle(100)).place(x=520, y=100)
    button_persegi = ttk.Button(root, text='persegi', style='TButton', width=20,
                                command=lambda: draw_box()).place(x=660, y=100)
    button_segitiga = ttk.Button(root, text='segitiga', style='TButton', width=20,
                                 command=lambda: draw_triangle()).place(x=520, y=130)
    button_garis = ttk.Button(root, text='garis', style='TButton', width=20, 
                              command=lambda: draw_line()).place(x=660, y=130)
    button_hapus = ttk.Button(root, text='Hapus Objek', style='TButton', width=20, 
                              command=lambda: ttl.clear()).place(x=660, y=180)


    root.mainloop()