from tkinter import *
from tkinter import ttk

class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x740+0+0")

        title=Label(self.root, text= "Student Management System",font=("Arial",35,"bold"),bg="Brown")
        title.pack(side=TOP,fill="x")
        
    #========Manage_Frame=======
        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="pink")
        Manage_Frame.place(x=20,y=100,width=450,height=590)

        m_title=Label(Manage_Frame,text="Manage Students",font=("Arial",20,"bold"),bg="pink")
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll=Label(Manage_Frame,text="Roll No.",font=("Arial",15,"bold"),bg="pink")
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_roll= Entry(Manage_Frame,font=("Arial",15,"bold"),bg="pink")
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")
        
        lbl_name= Label(Manage_Frame,text="Name",font=("Arial",15,"bold"),bg="pink")
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_name= Entry(Manage_Frame,font=("Arial",15,"bold"),bg="pink")
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        lbl_email= Label(Manage_Frame,text="Email",font=("Arial",15,"bold"),bg="pink")
        lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        txt_email= Entry(Manage_Frame,font=("Arial",15,"bold"),bg="pink")
        txt_email.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        lbl_gender= Label(Manage_Frame,text="Gender",font=("Arial",15,"bold"),bg="pink")
        lbl_gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")
        
        combo_gender= ttk.Combobox(Manage_Frame,font=("Arial",15,"bold"),state="readonly")
        combo_gender['values']=("male","female","other")
        combo_gender.grid(row=4,column=1,padx=20,pady=10)

        lbl_contact= Label(Manage_Frame,text="Contact",font=("Arial",15,"bold"),bg="pink")
        lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        txt_contact= Entry(Manage_Frame,font=("Arial",15,"bold"),bg="pink")
        txt_contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        lbl_dob= Label(Manage_Frame,text="D.O.B",font=("Arial",15,"bold"),bg="pink")
        lbl_dob.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        txt_dob= Entry(Manage_Frame,font=("Arial",15,"bold"),bg="pink")
        txt_dob.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        lbl_address= Label(Manage_Frame,text="Address",font=("Arial",15,"bold"),bg="pink")
        lbl_address.grid(row=7,column=0,pady=10,padx=20,sticky="w")
        
        txt_address = Text(Manage_Frame,width=31,height=4,font=("arial",10),bg="pink")
        txt_address.grid(row=7,column=1,pady=10,padx=20,sticky="w")

    #=======Button_Frame========
        btn_Frame= Frame(Manage_Frame,bd=4,relief=RIDGE,bg="pink")
        btn_Frame.place(x=10,y=500,width=420)

        Addbtn= Button(btn_Frame,text="Add",width=10).grid(row=0,column=0,padx=10,pady=10)
        Uddatebtn= Button(btn_Frame,text="Update",width=10).grid(row=0,column=1,padx=10,pady=10)
        Deletebtn= Button(btn_Frame,text="Delete",width=10).grid(row=0,column=2,padx=10,pady=10)
        Clearbtn= Button(btn_Frame,text="Clear",width=10).grid(row=0,column=3,padx=10,pady=10)

    #========Deatil_Frame=======
        Detail_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="pink")
        Detail_Frame.place(x=500,y=100,width=800,height=590)

if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
