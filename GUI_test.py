from tkinter import *
import tkinter.messagebox as messagebox
import time
import random


class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        v = StringVar()
        self.e = Label(frame, textvariable=v, font=("Helvetica", 50))
        v.set('')
        self.v = v
        self.e.grid(row=0,columnspan=2)

        item_lab = StringVar()
        self.lab1 = Label(frame, textvariable=item_lab, bd='5',font=("Helvetica", 20))
        item_lab.set('项目')
        self.item_lab = item_lab
        self.lab1.grid(row=1, column=0)

        content = StringVar()
        self.content = content
        content.set("1,2,3,4,5")
        self.entry1 = Entry(frame, textvariable=content, bd='5',state="normal",font=("Helvetica", 20))
        self.entry1.grid(row=1, column=1)

        time_lab = StringVar()
        self.lab2 = Label(frame, textvariable=time_lab, bd='5',font=("Helvetica", 20))
        time_lab.set('时间(秒)')
        self.time_lab = time_lab
        self.lab2.grid(row=2, column=0)

        time_update = StringVar()
        time_update.set("0.01")
        self.time_update = time_update
        self.entry2 = Entry(frame, textvariable=time_update, bd='5',state="normal",font=("Helvetica", 20))
        self.entry2.grid(row=2, column=1)

        self.button1 = Button(frame, text='start', fg='red', command=self.start_hi,font=("Helvetica", 20))
        self.button1.grid(row=3, column=0)

        self.button2 = Button(frame, text='stop', fg='blue', command=self.say_stop,font=("Helvetica", 20))
        self.button2.grid(row=3, column=1)
        self.root = master
        self.stop = 0

    def list_star(self):
        star = []
        content = self.content.get()
        star = content.split(",")
        if len(star) >= 2:
            return star
        else:
            self.item_error()

    def start_hi(self):
        self.stop = 0
        star = self.list_star()
        time_update = float(self.time_update.get())
        self.update_clock(star, time_update)

    def say_stop(self):
        self.stop = 1

    def update_clock(self, star, time_update):
        b = random.choice(star)
        self.v.set(b)
        this_time = time_update
        if self.stop == 1:
            return
        try:
            self.root.after(int(this_time * 1000), self.update_clock,star,this_time)
        except:
            self.time_error()

    def item_error(self):
        messagebox.showinfo('Message', '项目输入有误，使用半角逗号隔开')

    def time_error(self):
        messagebox.showinfo('Message', '时间输入有误，单位是秒')


root = Tk()
root.geometry('500x300+500+200')
app = App(root)
root.mainloop()
