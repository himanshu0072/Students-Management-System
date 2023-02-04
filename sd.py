from tkinter import*
from tkinter import ttk
import pymysql
from tkinter import messagebox


#============================================================Student Management System page===============================================================================
class student:
    def __init__(self,root):
        self.root=root
        self.root.title("Students Management System")
        self.root.geometry("1600x1000+0+0")

        title=Label(self.root,text="Students Management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="red",fg="white")
        title.pack(side=TOP,fill=X)

       #------------------------------------------all Variables-----------------------------------------------
        self.id_i=StringVar()
        self.pass_i=StringVar()


        self.roll_no_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()

        self.search_by=StringVar()
        self.search_text=StringVar()




       #------------------------------manage  frame ---------------------------------------------------------------------------
        
        m_frame=Frame(self.root,bd=4,relief=RIDGE, bg="pink")
        m_frame.place(x=20,y=100,width=450,height=600)

        m_title=Label(m_frame,text="Manage Students",bg="pink",fg="white",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)


        lbl_roll=Label(m_frame,text="Roll No. :",bg="pink",fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")


        txt_roll=Entry(m_frame,textvariable=self.roll_no_var,font=("times new roman",10,"bold"),bd=3,relief=GROOVE)
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_name=Label(m_frame,text="Name :",bg="pink",fg="white",font=("times new roman",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")


        txt_name=Entry(m_frame,textvariable=self.name_var,font=("times new roman",10,"bold"),bd=3,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        
        lbl_email=Label(m_frame,text="Email :",bg="pink",fg="white",font=("times new roman",20,"bold"))
        lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="w")


        txt_email=Entry(m_frame,textvariable=self.email_var,font=("times new roman",10,"bold"),bd=3,relief=GROOVE)
        txt_email.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        lbl_Gender=Label(m_frame,text="Gender :",bg="pink",fg="white",font=("times new roman",20,"bold"))
        lbl_Gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        combo_gender=ttk.Combobox(m_frame,textvariable=self.gender_var,font=("times new roman",9,"bold"),state="readonly")
        combo_gender['values']=("Male","Female","Others")
        combo_gender.grid(row=4,column=1,padx=20,pady=10)

        

        


        lbl_cnt=Label(m_frame,text="Contact :",bg="pink",fg="white",font=("times new roman",20,"bold"))
        lbl_cnt.grid(row=5,column=0,pady=10,padx=20,sticky="w")


        txt_cnt=Entry(m_frame,textvariable=self.contact_var,font=("times new roman",10,"bold"),bd=3,relief=GROOVE)
        txt_cnt.grid(row=5,column=1,pady=10,padx=20,sticky="w")


        lbl_dob=Label(m_frame,text="D.O.B. :",bg="pink",fg="white",font=("times new roman",20,"bold"))
        lbl_dob.grid(row=6,column=0,pady=10,padx=20,sticky="w")


        txt_dob=Entry(m_frame,textvariable=self.dob_var,font=("times new roman",10,"bold"),bd=3,relief=GROOVE)
        txt_dob.grid(row=6,column=1,pady=10,padx=20,sticky="w")
        

        lbl_address=Label(m_frame,text="Address :",bg="pink",fg="white",font=("times new roman",20,"bold"))
        lbl_address.grid(row=7,column=0,pady=10,padx=20,sticky="w")


        self.txt_address=Text(m_frame,width=23,height=4,bd=3,font=("",10,"bold"))
        self.txt_address.grid(row=7,column=1,pady=10,padx=20,sticky="w")

         #----------------------------------Button---------------------------------------------------------------------------------------


        btn_frame=Frame(m_frame,bd=4,relief=RIDGE, bg="red")
        btn_frame.place(x=15,y=530,width=420)

        addbtn=Button(btn_frame,text="Add",width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        updbtn=Button(btn_frame,text="Update",width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=10) 
        dltbtn=Button(btn_frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10) 
        clrbtn=Button(btn_frame,text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)   



        btn_frame=Frame(bd=1)
        btn_frame.place(x=30,y=730,width=140)
        
        addbtn=Button(btn_frame,text="Back",width=15,height=2, bg="pink",command=self.login2).grid(row=1,column=1)




       #-----------------------detail   frame ---------------------------------------------------------------------------------------------

        d_frame=Frame(self.root,bd=4,relief=RIDGE, bg="pink")
        d_frame.place(x=500,y=100,width=850,height=600)

        lbl_name=Label(d_frame,text="Students Details:",bg="pink",fg="white",font=("times new roman",30,"bold"))


        lbl_name.grid(row=0,column=0,pady=10,padx=20,sticky="w")






    


      #----------------------------------------------------table frame right side--------------------------------------------------------------------------

        t_frame=Frame(d_frame,bd=4,relief=RIDGE, bg="pink")
        t_frame.place(x=10,y=70,width=800,height=450)

        scroll_x=Scrollbar(t_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(t_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(t_frame,columns=("Roll","Name","Email","Gender","contact","DOB","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("Roll",text="Roll no.")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("contact",text="Contact")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Address",text="Address")

        self.student_table['show']='headings'

        self.student_table.column("Roll",width=50)
        self.student_table.column("Name",width=120)
        self.student_table.column("Email",width=150)
        self.student_table.column("Gender",width=60)
        self.student_table.column("contact",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Address",width=150)



        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

        j_frame=Frame(self.root,relief=RIDGE)
        j_frame.place(x=1100,y=730,width=250,height=40)
        lbl_t=Label(j_frame,text="""Developed By: Himanshu Prajapati
Email : himanshu2003prajapati@gmail.com""",fg="black",font=("times new roman",10))
        lbl_t.grid(row=1,column=0,pady=10,padx=20,sticky="w")





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
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record has been inserted")



            

    def login2(self):
        
                
                if self.id_i.get()=="" or self.pass_i.get()=="":
                        messagebox.showinfo("Success","OK, if you want to go back Press ok")

                        root.destroy()
                        
                        import sl
                       
                else:
                        messagebox.showerror("Error","Sorry there is a technical issue") 




    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="Himanshu",database="stm")
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)

            con.commit()

        con.close()


    def clear(self):
        self.roll_no_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_address.delete("1.0",END)


    def get_cursor(self,ev):
        cursor_row=self.student_table.focus()
        contents=self.student_table.item(cursor_row)
        row=contents['values']
        self.roll_no_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[6])




    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="Himanshu",database="stm")
        cur=con.cursor()
        cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(
                self.name_var.get(),
                self.email_var.get(),
                self.gender_var.get(),
                self.contact_var.get(),
                self.dob_var.get(),
                self.txt_address.get('1.0',END),
                self.roll_no_var.get()
                ))
        
        con.commit()
        
        self.fetch_data()
        self.clear()
        con.close()
        



    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="Himanshu",database="stm")
        cur=con.cursor()
        cur.execute("delete from students where roll_no=%s",self.roll_no_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()



    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="Himanshu",database="stm")
        cur=con.cursor()

        cur.execute("select * from students where"+str(self.search_by.get())+"LIKE '%'"+str(self.search_text.get())+"'%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)
            

            con.commit()
        con.close()

  





root=Tk()
ob=student(root)
root.mainloop()



#===========================================================================================================================================         


