from tkinter import*
from tkinter import ttk
import pymysql
from tkinter import messagebox






#============================================================login page===============================================================================

class login1:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1600x1000+0+0")

        title=Label(self.root,text="WELCOME TO STUDENT  MANAGEMENT SYSTEM",bd=10,relief=GROOVE,font=("times new roman",30,"bold"),bg="green",fg="white")
        title.pack(side=TOP,fill=X)
        t1=Label(self.root,text="              Enter your  ID and Password        ",relief=GROOVE,bd=4,font=("times new roman",20,"bold"),bg='black',fg="white")
        t1.pack(side=TOP,pady=60)


        self.id_i=StringVar()
        self.pass_i=StringVar()

        m_frame=Frame(self.root,bd=6,relief=RIDGE, bg="red")
        m_frame.place(x=560,y=240,width=400,height=200)

        lbl_roll=Label(m_frame,text="User ID :",bg="red",fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")


        txt_roll=Entry(m_frame,textvariable=self.id_i,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")


        lbl_name=Label(m_frame,text="Password :",bg="red",fg="white",font=("times new roman",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")


        txt_name=Entry(m_frame,textvariable=self.pass_i,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        btn_frame=Frame(m_frame,bd=4,relief=RIDGE, bg="red")
        btn_frame.place(x=290,y=130,width=85)
        
        addbtn=Button(btn_frame,text="Submit",width=10,command=self.login).grid(row=9,column=6)
        

        j_frame=Frame(self.root,relief=RIDGE)
        j_frame.place(x=1100,y=730,width=250,height=40)
        lbl_t=Label(j_frame,text="""Developed By: Himanshu Prajapati
Email : himanshu2003prajapati@gmail.com""",fg="black",font=("times new roman",10))
        lbl_t.grid(row=1,column=0,pady=10,padx=20,sticky="w")



    

        
    def login(self):
        
                if self.id_i.get()=="" or self.pass_i.get()=="":
                        messagebox.showerror("Error","please enter a ID and Password")
                elif self.id_i.get()=="h" and self.pass_i.get()=="1":
                        messagebox.showinfo("Success",f"Welcome {self.id_i.get()} as a user")
                        root.destroy()
                        import sl
                        

                elif self.id_i.get()=="rajan" and self.pass_i.get()=="1234":
                        messagebox.showinfo("Success",f"Welcome {self.id_i.get()} as a user")
                        
                        root.destroy()
                        
                       
                else:
                        messagebox.showerror("Error","Enter valid username and password")

    
        
        
        	
                
root=Tk()
obj=login1(root)
root.mainloop()


