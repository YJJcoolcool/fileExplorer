import sys, os, time, subprocess
import tkinter as tk

currentDir = sys.path[0]
print(currentDir)
thing = currentDir
class Run():
    def __init__(self,directory):
        print(directory)
        os.chdir(directory)
        self.currentPath = str(os.getcwd())
        self.currentDir = str(self.currentPath.split('/')[-1])
        self.listoffiles = os.listdir()
        print(self.listoffiles)
        if self.currentDir=="":
            self.currentDir="Root"
        
        #Setup
        self.root = tk.Tk()
        self.root.title(self.currentDir)

        #Set the window Size
        self.window_option=open("window_size.txt","r").read().split()
        self.window_x = str(self.window_option[0])
        self.window_y = str(self.window_option[1])
        self.window_size = self.window_x+"x"+self.window_y
        self.root.geometry(self.window_size)

        self.bodyframe = tk.Frame(self.root, bg="#ff0000")
        self.bodyframe.pack(fill="both",expand=True)

        
        self.count=0
        
        for i in self.listoffiles:
            if len(str(i))>12:
                self.line1=str(i)[0:12]
                self.line2=str(i)[12:]
            self.appbutton = tk.Button(self.bodyframe,height=5,width=9,wraplength=70,bg="#000000",text=str(i),command=self.changeText)
            self.appbutton.grid(row=0,column=self.count,padx=10,pady=10)
            self.count+=1
    def changeText(self):
        self.root.title("Test2")
        
        
        
        os.listdir()
        self.root.mainloop()

    

app=Run(currentDir)

