import Tkinter as tk
from PIL import ImageTk, Image
import os

class Timer:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1600x900")
        self.master.title("Pomodoro Timer")
        self.myColor = '#%02x%02x%02x' % (127, 127, 127)
        self.master.configure(bg=self.myColor)
        self.state = False
        self.minutes = 30
        self.seconds = 0

        self.mins = 30
        self.secs = 0
        self.lab1 = tk.Label(self.master, width=40,bg=self.myColor).grid(row=0, column=0)
        self.lab2 = tk.Label(self.master, width=40,bg=self.myColor).grid(row=0, column=1)
        # self.lab3 = tk.Label(self.master, width=40,bg=self.myColor).grid(row=0, column=0)

        self.display = tk.Label(self.master, height=5, width=10, textvariable="", bg=self.myColor)
        self.display.config(text="00:00")
        self.display.config(font=("Courier", 32))
        self.display.grid(row=0, column=2)

        self.rect = ImageTk.PhotoImage(Image.open("rect.png"), width=1, height=3)
        self.screw = ImageTk.PhotoImage(Image.open("screw.png"), width=1, height=3)
        self.heart  = ImageTk.PhotoImage(Image.open("heart.png"), width=1, height=3)

        #Displaying it
        self.imglabel1 = tk.Label(self.master, image=self.rect,bg=self.myColor)
        self.imglabel1.grid(row=1, column=1)
        self.imglabel2 = tk.Label(self.master, image=self.screw,bg=self.myColor)
        self.imglabel2.grid(row=1, column=2)
        self.imglabel3 = tk.Label(self.master, image=self.heart,bg=self.myColor)
        self.imglabel3.grid(row=1, column=3)

        self.textBox1 = tk.Text(self.master, height=1, width=40, padx=2)
        self.textBox1.grid(row=2,column=1, sticky=tk.E+tk.W)
        self.textBox2 = tk.Text(self.master, height=1, width=40, padx=2)
        self.textBox2.grid(row=2,column=2, sticky=tk.E+tk.W)
        self.textBox3 = tk.Text(self.master, height=1, width=40, padx=2)
        self.textBox3.grid(row=2,column=3, sticky=tk.E+tk.W)
        self.lab2 = tk.Label(self.master, width=40,bg=self.myColor).grid(row=3, column=2)

        self.buttonCommit = tk.Button(self.master, height=1, width=10, text="Enter code", command=self.checkCode)
        self.buttonCommit.grid(row=4,column=2,sticky=tk.E+tk.W)

        self.start()

        self.countdown()

    def checkCode(self):
        # code1 = self.textBox1.get("1.0",'end-1c')
        # code2 = self.textBox2.get("1.0",'end-1c')
        # code3 = self.textBox3.get("1.0",'end-1c')
        #
        # if str(code1) == '7' and str(code2) == '12' and str(code3) == '3':
        self.textBox1.grid_remove()
        self.textBox2.grid_remove()
        self.textBox3.grid_remove()
        self.imglabel1.grid_remove()
        self.imglabel2.grid_remove()
        self.imglabel3.grid_remove()
        self.buttonCommit.grid_remove()

        self.showMap()

    def showMap(self):
        self.map = ImageTk.PhotoImage(Image.open("map.png"), width=800, height=400)
        self.maplabel = tk.Label(self.master, image=self.map,bg=self.myColor)
        self.maplabel.grid(row=1, column=1, columnspan=10)


    def countdown(self):
        """Displays a clock starting at min:sec to 00:00, ex: 25:00 -> 00:00"""

        if self.state == True:
            if self.secs < 10:
                if self.mins < 10:
                    self.display.config(text="0%d : 0%d" % (self.mins, self.secs))
                else:
                    self.display.config(text="%d : 0%d" % (self.mins, self.secs))
            else:
                if self.mins < 10:
                    self.display.config(text="0%d : %d" % (self.mins, self.secs))
                else:
                    self.display.config(text="%d : %d" % (self.mins, self.secs))

            if (self.mins == 0) and (self.secs == 0):
                self.display.config(text="Game Over!")
            else:
                if self.secs == 0:
                    self.mins -= 1
                    self.secs = 59
                else:
                    self.secs -= 1

                self.master.after(1000, self.countdown)
        else:
            self.master.after(100, self.countdown)

    def start(self):
        if self.state == False:
            self.state = True
            self.mins = self.minutes
            self.secs = self.seconds

    def pause(self):
        if self.state == True:
            self.state = False



root = tk.Tk()
my_timer = Timer(root)

root.mainloop()
