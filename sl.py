from tkinter import*
from tkinter import ttk
import pymysql
from tkinter import messagebox

#============================================================MAIN PAGE===============================================================================

class login2:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1600x1000+0+0")

        title=Label(self.root,text="WELCOME TO STUDENT  MANAGEMENT SYSTEM",bd=10,relief=GROOVE,font=("times new roman",30,"bold"),bg="green",fg="white")
        title.pack(side=TOP,fill=X)
        t1=Label(self.root,text="              Kindaly select any one        ",relief=GROOVE,bd=4,font=("times new roman",20,"bold"),bg='black',fg="white")
        t1.pack(side=TOP,pady=60)


        self.id_i=StringVar()
        self.pass_i=StringVar()


        m_frame=Frame(self.root,bd=6,relief=RIDGE,bg="pink")
        m_frame.place(x=300,y=240,width=950,height=200)


        btn_frame=Frame(m_frame,bd=1,relief=RIDGE)
        btn_frame.place(x=100,y=60,width=150)
        
        addbtn=Button(btn_frame,text="Student registration",width=20,height=3,command=self.login).grid(row=1,column=1)


        
        btn_frame=Frame(m_frame,bd=1,relief=RIDGE)
        btn_frame.place(x=600,y=60,width=150)
        
        addbtn=Button(btn_frame,text="Student Details",width=20,height=3,command=self.login2).grid(row=0,column=2)

   
        j_frame=Frame(self.root,relief=RIDGE)
        j_frame.place(x=1100,y=730,width=250,height=40)
        lbl_t=Label(j_frame,text="""Developed By: Himanshu Prajapati
Email : himanshu2003prajapati@gmail.com""",fg="black",font=("times new roman",10))
        lbl_t.grid(row=1,column=0,pady=10,padx=20,sticky="w")


#============================================================MAIN PAGE===============================================================================
        


#===========================================================login definition===========================================================================
    def login(self):
        
                if self.id_i.get()=="" or self.pass_i.get()=="":
                        messagebox.showinfo("Success","OK, if you want to register student Details Press ok")

                        
                        root.destroy()
                        import sr
                       
                else:
                        messagebox.showerror("Error","Sorry there is a technical issue")




    def login1(self):
        
                
                if self.id_i.get()=="" or self.pass_i.get()=="":
                        messagebox.showinfo("Success","OK, if you want to manage student Attendence Press ok")

                        
                        root.destroy()
                        import sr
                       
                else:
                        messagebox.showerror("Error","Sorry there is a technical issue")
        

                        
                



    def login2(self):
        
                
                if self.id_i.get()=="" or self.pass_i.get()=="":
                        messagebox.showinfo("Success","OK, if you want to manage student Details Press ok")

                        
                        root.destroy()
                        import sd 
                       
                else:
                        messagebox.showerror("Error","Sorry there is a technical issue")

               
root=Tk()
obj=login2(root)
root.mainloop()



