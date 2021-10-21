#from tkinter import *  
#from tkinter.ttk import Combobox   
#window = Tk()  
#window.title("Добро пожаловать в приложение PythonRu")  
#window.geometry('400x250')  
#combo = Combobox(window)  
#combo['values'] = (1, 2, 3, 4, 5, "Текст")  
#combo.current(1)  # установите вариант по умолчанию  
#combo.grid(column=0, row=0)  
#window.mainloop()

#from tkinter import *  
#from tkinter.ttk import Radiobutton  
#def clicked():  
    #lbl.configure(text=selected.get())   
#window = Tk()  
#window.title("Добро пожаловать в приложение PythonRu")  
#window.geometry('400x250')  
#selected = IntVar()  
#rad1 = Radiobutton(window,text='Первый', value=1, variable=selected)  
#rad2 = Radiobutton(window,text='Второй', value=2, variable=selected)  
#rad3 = Radiobutton(window,text='Третий', value=3, variable=selected)  
#btn = Button(window, text="Клик", command=clicked)  
#lbl = Label(window)  
#rad1.grid(column=0, row=0)  
#rad2.grid(column=1, row=0)  
#rad3.grid(column=2, row=0)  
#btn.grid(column=3, row=0)  
#lbl.grid(column=0, row=1)  
#window.mainloop()

#from tkinter import *  
#from tkinter import scrolledtext  
#window = Tk()  
#window.title("Добро пожаловать в приложение PythonRu")  
#window.geometry('400x250')  
#txt = scrolledtext.ScrolledText(window, width=40, height=10)  
#txt.grid(column=0, row=0)  
#window.mainloop()

#from tkinter import *  
#from tkinter import messagebox  
#def clicked():  
    #messagebox.showinfo('Заголовок', 'Текст')  
#window = Tk()  
#window.title("Добро пожаловать в приложение PythonRu")  
#window.geometry('400x250')  
#btn = Button(window, text='Клик', command=clicked)  
#btn.grid(column=0, row=0)  
#window.mainloop()

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