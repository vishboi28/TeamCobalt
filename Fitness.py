import tkinter as tk
import time
def march_on_the_spot(x,y):
    class A:
        def __init__(self, master):
            self.label=tk.Label(master)
            self.label.grid(row=0, column=0)
            self.label.configure(text='nothing')
            self.count = 0
            self.update_label()

        def update_label(self):
            if self.count < 60 :
                self.label.configure(text = 'count: {}'.format(self.count))
                self.label.after(1000, self.update_label) # call this method again in 1,000 milliseconds
                self.count += 1
            print(self.count)

    root = tk.Tk()
    root.title('FITNESS TEAM COBALT')
    root.geometry("1000x600")
    A(root)
    root.mainloop()    


march_on_the_spot(5,3)