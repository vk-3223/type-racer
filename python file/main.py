import tkinter as tk
import time
import threading
import random


class TypeSpeedgui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("type speed")
        self.root.geometry("800x600")
        self.texts = open("2_text.txt","r").read().split("\n")

        self.frame = tk.Frame(self.root)

        self.sample_lable = tk.Label(self.frame,text=random.choice(self.texts),font=("arial",18))
        self.sample_lable.grid(row=0,column=0,columnspan=2,padx=5,pady=10)

        self.inpunt_entry = tk.Entry(self.frame,width=40,font=("arial",19))
        self.inpunt_entry.grid(row=1,column=0,columnspan=2,padx=5,pady=10)
        self.inpunt_entry.bind("<KeyPress>",self.start)

        self.speed_lable = tk.Label(self.frame,text="Speed: \n0.00 cps\n0.00 cpm\n0.00 wps\n0.00 wpm",font=("arial",18))
        self.speed_lable.grid(row=2,column=0,columnspan=2,padx=5,pady=10)

        self.reset_button = tk.Button(self.frame,text="Reset",command=self.reset)
        self.reset_button.grid(row=3,column=0,columnspan=2,padx=5,pady=10)

        self.frame.pack(expand=True)

        self.counter = 0
        self.running = False

        self.root.mainloop()

    def start(self,event):
        if not self.running:
            if not event.keycode in [16,17,18]:
                self.running = True
                t = threading.Thread(target=self.time_thread)
                t.start()
        if not self.sample_lable.cget('text').startswith(self.inpunt_entry.get()):
            self.inpunt_entry.config(fg="red")
        else:
            self.inpunt_entry.config(fg="black")
        if self.inpunt_entry.get()==self.sample_lable.cget('text')[:-1]:
            self.running = False
            self.inpunt_entry.config(fg="green")                

    def time_thread(self):
        while self.running:
            time.sleep(0.1)
            self.counter+=0.1
            cps = len(self.inpunt_entry.get()) / self.counter
            cpm = cps * 60
            wps = len(self.inpunt_entry.get().split(" "))/self.counter
            wpm = wps*60
            self.speed_lable.config(text=f"speed:\n{cps:.2f} cps\n{cpm:.2f} cpm\n{wps:.2f} wps\n{wpm:.2f} wpm\n")    
        
    def reset(self):
        self.running == False
        self.counter = 0
        self.speed_lable.config(text="Speed: \n0.00 cps\n0.00 cpm\n0.00 wps\n0.00 wpm")
        self.sample_lable.config(text=random.choice(self.texts))
        self.inpunt_entry.delete(0,tk.END)

TypeSpeedgui()    