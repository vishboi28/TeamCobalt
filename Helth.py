from tkinter import*
import time
def march_on_the_spot(x,y):

    root = Tk()
    root.title('March On The Spot')
    root.geometry("1000x600")

    def update(m,z):
        label2.config(text=0, m,:,z)

    label1= Label(root, text="Start off marching on the spot and then march forwards and backwards. Pump your arms up and down in rhythm with your steps, keeping the elbows bent and the fists soft.")
    label1.pack(pady=20)

    label2= Label(root,text=(0,0,':',0,0))
    for i in range(0,y):
        t=0
        while t<x:
            t +=1
            label2.after(1000, update(i,t))
    root.mainloop()

march_on_the_spot(5,2)