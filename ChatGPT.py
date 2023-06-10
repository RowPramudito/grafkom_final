import turtle
import tkinter as tk

# Fungsi untuk menggambar persegi
def draw_square():
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.end_fill()

# Fungsi untuk menggambar lingkaran
def draw_circle():
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

# Fungsi untuk menggambar segitiga
def draw_triangle():
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(100)
        turtle.right(120)
    turtle.end_fill()

# Fungsi untuk mengisi warna pada bangun datar
def fill_shape():
    color = color_entry.get()
    turtle.fillcolor(color)

# Fungsi untuk melakukan translasi pada bangun datar
def translate_shape():
    x = int(translate_x_entry.get())
    y = int(translate_y_entry.get())
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

# Fungsi untuk melakukan rotasi pada bangun datar
def rotate_shape():
    angle = int(rotate_entry.get())
    turtle.right(angle)

# Membuat jendela utama
window = tk.Tk()
window.title("Shape Drawer")

# Frame untuk tombol dan input
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

# Tombol untuk menggambar persegi
square_button = tk.Button(button_frame, text="Persegi", command=draw_square)
square_button.grid(row=0, column=0, padx=10)

# Tombol untuk menggambar lingkaran
circle_button = tk.Button(button_frame, text="Lingkaran", command=draw_circle)
circle_button.grid(row=0, column=1, padx=10)

# Tombol untuk menggambar segitiga
triangle_button = tk.Button(button_frame, text="Segitiga", command=draw_triangle)
triangle_button.grid(row=0, column=2, padx=10)

# Frame untuk mengisi warna
color_frame = tk.Frame(window)
color_frame.pack(pady=10)

# Label dan input untuk warna
color_label = tk.Label(color_frame, text="Warna: ")
color_label.grid(row=0, column=0)

color_entry = tk.Entry(color_frame)
color_entry.grid(row=0, column=1)

fill_button = tk.Button(color_frame, text="Isi Warna", command=fill_shape)
fill_button.grid(row=0, column=2, padx=10)

# Frame untuk translasi
translate_frame = tk.Frame(window)
translate_frame.pack(pady=10)

# Label dan input untuk translasi
translate_x_label = tk.Label(translate_frame, text="Translasi X: ")
translate_x_label.grid(row=0, column=0)

translate_x_entry = tk.Entry(translate_frame)
translate_x_entry.grid(row=0, column=1)

translate_y_label = tk.Label(translate_frame, text="Translasi Y: ")
translate_y_label.grid(row=0, column=2)

translate_y_entry = tk.Entry(translate_frame)
translate_y_entry.grid(row=0, column=3)

translate_button = tk.Button(translate_frame, text="Translasi", command=translate_shape)
translate_button.grid(row=0, column=4, padx=10)

# Frame untuk rotasi
rotate_frame = tk.Frame(window)
rotate_frame.pack(pady=10)

# Label dan input untuk rotasi
rotate_label = tk.Label(rotate_frame, text="Rotasi (derajat): ")
rotate_label.grid(row=0, column=0)

rotate_entry = tk.Entry(rotate_frame)
rotate_entry.grid(row=0, column=1)

rotate_button = tk.Button(rotate_frame, text="Rotasi", command=rotate_shape)
rotate_button.grid(row=0, column=2, padx=10)

# Set up the turtle
turtle.speed(2)  # Kecepatan gambar (1 = paling lambat, 10 = paling cepat)
turtle.penup()  # Mengangkat pena agar tidak menggambar garis yang tidak perlu
turtle.goto(-200, 0)  # Posisikan turtle di sisi kiri

# Membuat screen untuk turtle
screen = turtle.Screen()

# Menjalankan event loop tkinter
window.mainloop()

# Mengakhiri program ketika jendela turtle ditutup
screen.bye()
