# -*- coding: utf-8 -*-
import tkinter as tk


#クラスを重ねるとややこしくなる？
class task():
    def __init__(self, content, trow):

        self.label1=tk.Label(
            root, text=content,
            font=("MSゴシック","12", "bold"),
            anchor="center"
        )
        self.label1.grid(row=trow, column=0, padx=5, pady=5)
        
        self.button1=tk.Button(
            root, text="Done",
            command=self.doneClick,
            #commandは引数及び()はいらない。あると即実行される。
            width=7, height =1,
        )
        self.button1.grid(row=trow, column=1, padx=5, pady=5)
    
    def doneClick(self):
        self.label1.grid_forget()
        self.button1.grid_forget()
        '''
        global i
        with open("./ToDoList.txt", "r") as f:
            lines = f.readlines()
        with open("./ToDoList.txt", "w") as f:
            for 
        '''

class inputArea:
    def __init__(self):
        self.entry=tk.Entry(root,font=("MSゴシック","12", "bold"),bd=3, width=25)
        self.entry.grid(row=1, column=0, padx=5, pady=5)
        self.addButton=tk.Button(
            root, text="Add",
            command=self.addClick,
            width=7, height =1
        )
        self.addButton.grid(row=1, column=1, padx=5, pady=5)

    def addClick(self):
        global i
        task(self.entry.get(), i)
        i+=1
        self.entry.delete(0, tk.END)
        self.entry.grid()

def upload():
    pass

def mosttop():
    pass

root = tk.Tk()
root.geometry ("320x320")
upbtn = tk.Button(
    root, text="upload",
    command=upload,
    width=25, height=1
)
upbtn.grid(row=0, column=0, padx=5, pady=5)
mstopbtn=tk.Button(
    root, text="最前面",
    command=mosttop,
    width=7, height =1
)
mstopbtn.grid(row=0, column=1, padx=5, pady=5)
inputArea()
with open("./ToDoList.txt", "r") as f:
    lines = f.readlines()
i=2
for line in lines:
    task(line, i)
    i+=1


root.mainloop()