from tkinter import *
from tkinter import ttk


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry=("1350x700+0+0")
        self.root.title("Student Management System")

if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()