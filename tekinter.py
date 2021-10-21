from itertools import cycle
import tkinter as tk
colors = cycle(['red', 'green', 'blue', 'silver', 'purple', 'orange', 'white', 'black', 'gold'])
def change_color():
    root['bg'] = next(colors)
    root.after(1500, change_color)
root = tk.Tk()
root.title("HELL")
root.geometry("800x800+0+0")
change_color()
root.mainloop()