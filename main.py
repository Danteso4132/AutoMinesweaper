import tkinter as tk
import random

"""
def create_grid(event=None):
    w = c.winfo_width() # Get current width of canvas
    h = c.winfo_height() # Get current height of canvas
    c.delete('grid_line') # Will only remove the grid_line
    # Creates all vertical lines at intevals of 53
    for i in range(0, w, 53):
        c.create_line([(i, 0), (i, h)], tag='grid_line')
    # Creates all horizontal lines at intevals of 53
    for i in range(0, h, 53):
        c.create_line([(0, i), (w, i)], tag='grid_line')
"""

"""
c = tk.Canvas(root, height=636, width=636, bg='white')
c.pack(fill=tk.BOTH, expand=True)
c.bind('<Configure>', create_grid)
w = tk.Frame (c)
"""
colours = ['red', 'blue', 'green', 'yellow']

"""
for i in range(12):
    for j in range(12):
        colour = colours[random.randint(0,3)]
        clear = tk.Button(root, bg=colour, height=2, width=4)
        clear.grid(row=i, column=j)
    """


def gen_set():
    for i in range(24):
        for j in range(24):

            colour = colours[random.randint(0, 3)]
            tk.Label(root, bg=colour).place(x=i * 21, y=j * 21, width=21, height=21)
    # root.quit()
    return


def generate():
    #print('1')
    gen_set()
    return
def clear_s():
    tk.Label(root, bg='red').place(x=0, y=0, width=504, height=504)


root = tk.Tk()
root.title("Сетка")
root.geometry("504x504")
root.wm_attributes('-transparentcolor', 'red')
root.wm_attributes('-topmost', '1')
root.wm_attributes('-alpha', 0.3)

control = tk.Tk()
control.title("COntrol")
control.wm_attributes('-topmost', '1')
control.wm_attributes('-transparentcolor', 'red')
tk.Label(control, bg='red').place(x=0, y=0, width=504, height=504)
control.geometry("200x100")

btn_gen = tk.Button(control, text="Generate", command=generate).place(x=10, y=10)
btn_clear = tk.Button(control, text='Clear', command=clear_s).place(x=80, y=10)

root.mainloop()
