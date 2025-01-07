import tkinter as tk
import time
from math import pi, sin, cos

def update_clock():
    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min
    hours = current_time.tm_hour

    if hours > 12:
        hours -= 12

    second_angle = pi/2 - 2*pi*(seconds/60)
    minute_angle = pi/2 - 2*pi*(minutes/60)
    hour_angle = pi/2 - 2*pi*((hours % 12 + minutes/60)/12)

    second_x = center_x + second_hand_length * cos(second_angle)
    second_y = center_y - second_hand_length * sin(second_angle)
    
    minute_x = center_x + minute_hand_length * cos(minute_angle)
    minute_y = center_y - minute_hand_length * sin(minute_angle)
    
    hour_x = center_x + hour_hand_length * cos(hour_angle)
    hour_y = center_y - hour_hand_length * sin(hour_angle)

    canvas.coords(second_hand, center_x, center_y, second_x, second_y)
    canvas.coords(minute_hand, center_x, center_y, minute_x, minute_y)
    canvas.coords(hour_hand, center_x, center_y, hour_x, hour_y)

    root.after(1000, update_clock)

# Create the main window
root = tk.Tk()
root.title("Clear Analog Clock with Numbers")

# Create a canvas to draw the clock
canvas = tk.Canvas(root, width=400, height=400, bg='white')
canvas.pack()

center_x, center_y = 200, 200
clock_radius = 180
second_hand_length = clock_radius * 0.9
minute_hand_length = clock_radius * 0.75
hour_hand_length = clock_radius * 0.6

# Draw clock face with a clear border
canvas.create_oval(center_x - clock_radius, center_y - clock_radius,
                   center_x + clock_radius, center_y + clock_radius,
                   outline='black', width=4, fill='white')

# Draw hour marks with numbers positioned correctly
for i in range(12):
    angle = pi/2 - 2*pi*(i/12)
    x_start = center_x + clock_radius * 0.85 * cos(angle)
    y_start = center_y - clock_radius * 0.85 * sin(angle)
    x_end = center_x + clock_radius * 0.95 * cos(angle)
    y_end = center_y - clock_radius * 0.95 * sin(angle)
    canvas.create_line(x_start, y_start, x_end, y_end, width=2, fill='black')
    
    # Calculate positions for the numbers (slightly further out)
    num_x = center_x + clock_radius * 0.70 * cos(angle)
    num_y = center_y - clock_radius * 0.70 * sin(angle)
    canvas.create_text(num_x, num_y, text=str(i+1), font=('Helvetica', 14, 'bold'), fill='black')

# Create hands with different colors
second_hand = canvas.create_line(center_x, center_y, center_x, center_y - second_hand_length, fill='red', width=2)
minute_hand = canvas.create_line(center_x, center_y, center_x, center_y - minute_hand_length, fill='blue', width=4)
hour_hand = canvas.create_line(center_x, center_y, center_x, center_y - hour_hand_length, fill='black', width=6)

# Draw center dot
canvas.create_oval(center_x - 5, center_y - 5, center_x + 5, center_y + 5, fill='black')

# Start the clock update
update_clock()

# Run the application
root.mainloop()
