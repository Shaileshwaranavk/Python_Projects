import tkinter as tk

root = tk.Tk()
root.title("Manual Traffic Light")
root.geometry("500x500")
root.config(bg="blue")
root.resizable(False, False)

def reset_circles():
    canvas.itemconfig(red_circle, fill="white")
    canvas.itemconfig(yellow_circle, fill="white")
    canvas.itemconfig(green_circle, fill="white")

def set_color(color):
    reset_circles()
    if color == "Red":
        canvas.itemconfig(red_circle, fill="red")
    elif color == "Yellow":
        canvas.itemconfig(yellow_circle, fill="yellow")
    elif color == "Green":
        canvas.itemconfig(green_circle, fill="green")

# Frame for buttons
button_frame = tk.Frame(root, bg="blue")
button_frame.pack(side="left", padx=40, pady=20)

red_button = tk.Button(button_frame, text="Red", width=12, height=2, bg="red", fg="white", font=("Helvetica", 14),
                       command=lambda: set_color("Red"))
red_button.pack(pady=20)

yellow_button = tk.Button(button_frame, text="Yellow", width=12, height=2, bg="yellow", font=("Helvetica", 14),
                          command=lambda: set_color("Yellow"))
yellow_button.pack(pady=20)

green_button = tk.Button(button_frame, text="Green", width=12, height=2, bg="green", fg="white", font=("Helvetica", 14),
                         command=lambda: set_color("Green"))
green_button.pack(pady=20)

# Canvas for traffic light circles
canvas_frame = tk.Frame(root, bg="black", borderwidth=2, relief="solid")
canvas_frame.pack(side="right", padx=60, pady=20)

canvas = tk.Canvas(canvas_frame, width=120, height=400, bg="black", highlightthickness=0)
canvas.pack()

red_circle = canvas.create_oval(10, 20, 110, 120, outline="black", fill="white", width=2)
yellow_circle = canvas.create_oval(10, 140, 110, 240, outline="black", fill="white", width=2)
green_circle = canvas.create_oval(10, 260, 110, 360, outline="black", fill="white", width=2)

root.mainloop()
