from tkinter import*
from tkinter import ttk
import pymysql
from tkinter import messagebox


class login1:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1600x1000+0+0")

        title=Label(self.root,text="WELCOME TO STUDENT  MANAGEMENT SYSTEM",bd=10,relief=GROOVE,font=("times new roman",30,"bold"),bg="green",fg="black")
        title.pack(side=TOP,fill=X)
        t1=Label(self.root,text="         Please fill the form carefully and correct    ",relief=GROOVE,bd=4,font=("times new roman",20,"bold"))
        

        self.id_i=StringVar()
        self.pass_i=StringVar()



        self.roll_no_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()



        m_frame=Frame(self.root,bd=4,relief=RIDGE, bg="pink")
        m_frame.place(x=520,y=170,width=510,height=600)

        m_title=Label(m_frame,text="Students Resistration",bg="pink",fg="black",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)


        lbl_roll=Label(m_frame,text="Roll No. :",bg="pink",fg="black",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")


        txt_roll=Entry(m_frame,textvariable=self.roll_no_var,font=("times new roman",10,"bold"),bd=3,relief=GROOVE)
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_name=Label(m_frame,text="Name :",bg="pink",fg="black",font=("times new roman",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")


        txt_name=Entry(m_frame,textvariable=self.name_var,font=("times new roman",10,"bold"),bd=3,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        
        lbl_email=Label(m_frame,text="Email :",bg="pink",fg="black",font=("times new roman",20,"bold"))
        lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="w")


        txt_email=Entry(m_frame,textvariable=self.email_var,font=("times new roman",10,"bold"),bd=3,relief=GROOVE)
        txt_email.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        lbl_Gender=Label(m_frame,text="Gender :",bg="pink",fg="black",font=("times new roman",20,"bold"))
        lbl_Gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        combo_gender=ttk.Combobox(m_frame,textvariable=self.gender_var,font=("times new roman",9,"bold"),state="readonly")
        combo_gender['values']=("Male","Female","Others")
        combo_gender.grid(row=4,column=1,padx=20,pady=10)

        

        


        lbl_cnt=Label(m_frame,text="Contact :",bg="pink",fg="black",font=("times new roman",20,"bold"))
        lbl_cnt.grid(row=5,column=0,pady=10,padx=20,sticky="w")


        txt_cnt=Entry(m_frame,textvariable=self.contact_var,font=("times new roman",10,"bold"),bd=3,relief=GROOVE)
        txt_cnt.grid(row=5,column=1,pady=10,padx=20,sticky="w")


        lbl_dob=Label(m_frame,text="D.O.B. :",bg="pink",fg="black",font=("times new roman",20,"bold"))
        lbl_dob.grid(row=6,column=0,pady=10,padx=20,sticky="w")


        txt_dob=Entry(m_frame,textvariable=self.dob_var,font=("times new roman",10,"bold"),bd=3,relief=GROOVE)
        txt_dob.grid(row=6,column=1,pady=10,padx=20,sticky="w")
        

        lbl_address=Label(m_frame,text="Address :",bg="pink",fg="black",font=("times new roman",20,"bold"))
        lbl_address.grid(row=7,column=0,pady=10,padx=20,sticky="w")


        self.txt_address=Text(m_frame,width=23,height=4,bd=3,font=("",10,"bold"))
        self.txt_address.grid(row=7,column=1,pady=10,padx=20,sticky="w")


        btn_frame=Frame(m_frame,bd=1, bg="pink")
        btn_frame.place(x=360,y=520,width=140)
        
        addbtn=Button(btn_frame,text="Submit",width=15,height=2,command=self.add_students).grid(row=1,column=1)


        btn_frame=Frame(m_frame,bd=1, bg="pink")
        btn_frame.place(x=30,y=520,width=140)
        
        addbtn=Button(btn_frame,text="Back",width=15,height=2,command=self.login2).grid(row=1,column=1)

        btn_frame=Frame(m_frame,bd=1, bg="pink")
        btn_frame.place(x=200,y=520,width=140)
        
        addbtn=Button(btn_frame,text="clear",width=15,height=2,command=self.clear).grid(row=1,column=1)



        j_frame=Frame(self.root,relief=RIDGE)
        j_frame.place(x=1100,y=730,width=250,height=40)
        lbl_t=Label(j_frame,text="""Developed By: Himanshu Prajapati
Email : himanshu2003prajapati@gmail.com""",fg="black",font=("times new roman",10))
        lbl_t.grid(row=1,column=0,pady=10,padx=20,sticky="w")






    def login2(self):
        
                
                if self.id_i.get()=="" or self.pass_i.get()=="":
                        messagebox.showinfo("Success","OK, if you want to go back Press ok")

                        root.destroy()
                        import sl


                        
                        
                       
                else:
                        messagebox.showerror("Error","Sorry there is a technical issue")




    def add_students(self):
            if self.roll_no_var.get()=="" or self.name_var.get()=="":
               messagebox.showerror("Error","All fields are required!")
            elif self.contact_var.get()=="" or self.dob_var.get()=="":
                messagebox.showerror("Error","All fields are required!")
            else:
                con=pymysql.connect(host="localhost",user="root",password="Himanshu",database="stm")
                cur=con.cursor()
                cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.roll_no_var.get(),
                self.name_var.get(),
                self.email_var.get(),
                self.gender_var.get(),
                self.contact_var.get(),
                self.dob_var.get(),
                self.txt_address.get('1.0',END)

                ))
                con.commit()
                print("Student is added in database")
                
                self.clear()
                con.close()
                messagebox.showinfo("Success","Record has been inserted")
                

    def clear(self):
                self.roll_no_var.set("")
                self.name_var.set("")
                self.email_var.set("")
                self.gender_var.set("")
                self.contact_var.set("")
                self.dob_var.set("")
                self.txt_address.delete("1.0",END)
           
                
root=Tk()
obj=login1(root)
root.mainloop()
