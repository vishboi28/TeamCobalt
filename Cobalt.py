from tkinter import*
import time

root = Tk()
root.title('FITNESS TEAM COBALT')
root.geometry("1000x600")

def update():
    my_label.config(text="New Text")

my_label= Label (root, text="Old")
my_label.pack(pady=20)

my_label.after(2000, update)




root.mainloop()