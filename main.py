from tkinter import *
from tkinter import ttk
import pymysql
import  tkinter.messagebox
from PIL import ImageTk,Image

db_name=""
db_pass=""
db_host=""
db_user=""
user = ''
passw = ''


class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x740+200+150")
        self.root.resizable(False,False)

        title=Label(self.root, text= "Student Management System",font=("Arial",35,"bold"),bg="pink")
        title.pack(side=TOP,fill="x")

    #=======All_Variables=======
        self.Roll_No_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()
        
        self.search_by=StringVar()
        self.search_txt=StringVar()
        
    #========Manage_Frame=======
        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="pink")
        Manage_Frame.place(x=20,y=100,width=450,height=590)

        m_title=Label(Manage_Frame,text="Manage Students",font=("Arial",20,"bold"),bg="pink")
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll=Label(Manage_Frame,text="Roll No.",font=("Arial",15,"bold"),bg="pink")
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_roll= Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("Arial",15,"bold"),bg="pink")
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")
        
        lbl_name= Label(Manage_Frame,text="Name",font=("Arial",15,"bold"),bg="pink")
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_name= Entry(Manage_Frame,textvariable=self.name_var,font=("Arial",15,"bold"),bg="pink")
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        lbl_email= Label(Manage_Frame,text="Email",font=("Arial",15,"bold"),bg="pink")
        lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        txt_email= Entry(Manage_Frame,textvariable=self.email_var,font=("Arial",15,"bold"),bg="pink")
        txt_email.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        lbl_gender= Label(Manage_Frame,text="Gender",font=("Arial",15,"bold"),bg="pink")
        lbl_gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")
        
        combo_gender= ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("Arial",15,"bold"),state="readonly")
        combo_gender['values']=("male","female","other")
        combo_gender.grid(row=4,column=1,padx=20,pady=10)

        lbl_contact= Label(Manage_Frame,text="Contact",font=("Arial",15,"bold"),bg="pink")
        lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        txt_contact= Entry(Manage_Frame,textvariable=self.contact_var,font=("Arial",15,"bold"),bg="pink")
        txt_contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        lbl_dob= Label(Manage_Frame,text="D.O.B",font=("Arial",15,"bold"),bg="pink")
        lbl_dob.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        txt_dob= Entry(Manage_Frame,textvariable=self.dob_var,font=("Arial",15,"bold"),bg="pink")
        txt_dob.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        lbl_address= Label(Manage_Frame,text="Address",font=("Arial",15,"bold"),bg="pink")
        lbl_address.grid(row=7,column=0,pady=10,padx=20,sticky="w")
        
        self.txt_address = Text(Manage_Frame,width=31,height=4,font=("arial",10),bg="pink")
        self.txt_address.grid(row=7,column=1,pady=10,padx=20,sticky="w")

    #=======Button_Frame========
        btn_Frame= Frame(Manage_Frame,bd=4,relief=RIDGE,bg="pink")
        btn_Frame.place(x=10,y=500,width=420)

        Addbtn= Button(btn_Frame,text="Add",width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        Uddatebtn= Button(btn_Frame,text="Update",width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        Deletebtn= Button(btn_Frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        Clearbtn= Button(btn_Frame,text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)

    #========Deatil_Frame=======
        Detail_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="pink")
        Detail_Frame.place(x=500,y=100,width=800,height=590)

        lbl_search= Label(Detail_Frame,text="Search By",font=("Arial",15,"bold"),bg="pink")
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search= ttk.Combobox(Detail_Frame,textvariable=self.search_by,width= 10,font=("Arial",15,"bold"),state="readonly")
        combo_search['values']=("Roll_no","Name","Contact")
        combo_search.grid(row=0,column=1,padx=20,pady=10)

        txt_search= Entry(Detail_Frame,textvariable=self.search_txt,width=15,font=("Arial",15,"bold"),bg="pink")
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        search_btn= Button(Detail_Frame,text="Search",width=10,pady=5,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        showall_btn= Button(Detail_Frame,text="Show All",width=10,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)
    
    #========Table_Frame========
        table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="pink")
        table_Frame.place(x=15,y=70,width=760,height=450)

        scroll_x= Scrollbar(table_Frame,orient=HORIZONTAL)
        scroll_y= Scrollbar(table_Frame,orient=VERTICAL)
        
        self.Student_table= ttk.Treeview(table_Frame,columns=("roll","name","email","gender","contact","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("roll",text="Roll No.")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("email",text="Email")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("contact",text="Contact")
        self.Student_table.heading("dob",text="D.O.B")
        self.Student_table.heading("address",text="Address")

        self.Student_table.column("roll",width=70)
        self.Student_table.column("name",width=150)
        self.Student_table.column("email",width=120)
        self.Student_table.column("gender",width=80)
        self.Student_table.column("contact",width=100)
        self.Student_table.column("dob",width=100)
        self.Student_table.column("address",width=150)

        self.Student_table["show"]="headings"
        self.Student_table.pack(fill=BOTH,expand=1)
        
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        self.fetch_data()

    def add_students(self):
        con=pymysql.connect(host=db_host,user=db_user,password=db_pass,database=db_name)
        cur=con.cursor()
        cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                        self.name_var.get(),
                                                                        self.email_var.get(),
                                                                        self.gender_var.get(),
                                                                        self.contact_var.get(),
                                                                        self.dob_var.get(),
                                                                        self.txt_address.get(1.0,END)
                                                                        ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def fetch_data(self):
        con=pymysql.connect(host=db_host,user=db_user,password=db_pass,database=db_name)
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if (rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()

    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_address.delete("1.0",END)

    def get_cursor(self,ev):
        cursor_row=self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row=contents['values']
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[6])

    def update_data(self):
        con=pymysql.connect(host=db_host,user=db_user,password=db_pass,database=db_name)
        cur=con.cursor()
        cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(
                                                                                        self.name_var.get(),
                                                                                        self.email_var.get(),
                                                                                        self.gender_var.get(),
                                                                                        self.contact_var.get(),
                                                                                        self.dob_var.get(),
                                                                                        self.txt_address.get(1.0,END),
                                                                                        self.Roll_No_var.get()
                                                                                        ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con=pymysql.connect(host=db_host,user=db_user,password=db_pass,database=db_name)
        cur=con.cursor()
        cur.execute("delete from students where roll_no=%s",self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
    
    def search_data(self):
        con=pymysql.connect(host=db_host,user=db_user,password=db_pass,database=db_name)
        cur=con.cursor()

        cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if (rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()




class Authentication:

    def __init__(self,root):

        self.root = root
        self.root.title('USER AUTHENTICATION')
        self.root.resizable(0,0)
        self.root.geometry("350x500")

    #======gradient_frame=======

        j=0
        r=10
        for i in range(100):
            c=str(222222+r)
            Frame(root,width=10,height=500,bg="#"+c).place(x=j,y=0)   
            j=j+10                                                  
            r=r+1

    #====main_frame======

        frame1=Frame(root,width=250,height=400,bg='white')
        frame1.place(x=50,y=50)

        l1=Label(root,text='Username',bg='white')
        l=('Consolas',13)
        l1.config(font=l)
        l1.place(x=80,y=200)

        #e1 entry for username entry
        e1=Entry(root,width=20,border=0)
        l=('Consolas',13)
        e1.config(font=l)
        e1.place(x=80,y=230)

        #e2 entry for password entry
        e2=Entry(root,width=20,border=0,show='*')
        e2.config(font=l)
        e2.place(x=80,y=310)


        l2=Label(root,text='Password',bg='white')
        l=('Consolas',13)
        l2.config(font=l)
        l2.place(x=80,y=280)


    #======frame_on_entry=======

        Frame(root,width=180,height=2,bg='#141414').place(x=80,y=332)
        Frame(root,width=180,height=2,bg='#141414').place(x=80,y=252)

        
    #=========open_img=============
        
        imagea=Image.open("log.png")
        self.imageb= ImageTk.PhotoImage(imagea)

        label1 = Label(root,image=self.imageb,
                    border=0,
                    justify=CENTER)


        label1.place(x=115, y=50)
       

    #=========Command==============
        def cmd():
            if e1.get()== user and e2.get()==passw :
                msg1= tkinter.messagebox.showinfo("LOGIN SUCCESSFULLY", f"         WELCOME  {user}       ")
    
                #Destroy current window
                root.destroy()
                
                #Open new window
                newroot = Tk()
                application = Student(newroot)
                newroot.mainloop()
                
            else:
                ms2 = tkinter.messagebox.showwarning("LOGIN FAILED","        PLEASE TRY AGAIN        ")


    #===Button_with_hover_effect===

        def bttn(x,y,text,ecolor,lcolor):
            def on_entera(e):
                myButton1['background'] = ecolor #ffcc66
                myButton1['foreground']= lcolor  #000d33

            def on_leavea(e):
                myButton1['background'] = lcolor
                myButton1['foreground']= ecolor

            myButton1 = Button(root,text=text,
                        width=20,
                        height=2,
                        fg=ecolor,
                        border=0,
                        bg=lcolor,
                        activeforeground=lcolor,
                        activebackground=ecolor,
                            command=cmd)
                  
            myButton1.bind("<Enter>", on_entera)
            myButton1.bind("<Leave>", on_leavea)

            myButton1.place(x=x,y=y)


        bttn(100,375,'L O G I N','white','#994422')



if __name__ == '__main__':

    root = Tk()
    root.geometry('425x185+700+300')
    application = Authentication(root)

    root.mainloop()
