import mysql.connector 
from tkinter import *
from tkinter import messagebox
conn=mysql.connector.connect(host="localhost",user="root",password="lakshmi", database="Jai_kisan")
mycur=conn.cursor()
#mycur.execute("CREATE DATABASE Jai_kisan") #create databases
#mycur.execute("CREATE TABLE IF NOT EXISTS Farmer_info(farmerName varchar(100),StateName varchar(100),Revenue int)")
#print("create successfully")

w=Tk() # this is for open a login window
w.title("Farmers revenue Survey") 
w.geometry('500x300')
label0=Label(w,text="Enter the login",fg="black",bg="olive",font=("calibri",15))
label0.pack(pady=10) 
label1=Label(w,text="User*",fg="black",bg="olive",font=("calibri",15))
label1.pack(pady=10)
ent=Entry(w)
ent.pack(pady=10)
label2=Label(w,text="Password*",fg="black",bg="olive",font=("calibri",15)) 
label2.pack(pady=10)
ent1=Entry(w,show='*') 
ent1.pack(pady=10)
def login():  # logic for the login window
     global ent2,ent3,ent4,add_farmer
     if ent.get()=="farmer".lower() and ent1.get()=="kisan".lower():
          w1=Tk()    # this is for again create a window,when click the login button
          w1.title("Farmer info")
          w1.geometry('700x800')
          label1=Label(w1,text="F a r m e r i n f o",bg="olive",font=(20)) 
          label1.pack(pady=20)
          label2=Label(w1,text="FarmerName:",bg="olive",font=(10))
          label2.pack(pady=10)
          ent2=Entry(w1) 
          ent2.pack(pady=10)
          label3=Label(w1,text="StateName:",bg="olive",font=(10))
          label3.pack(pady=10)
          ent3=Entry(w1)
          ent3.pack(pady=10)
          label4=Label(w1,text="Revenue:",bg="olive",font=(10))
          label4.pack(pady=10)
          ent4=Entry(w1)
          ent4.pack(pady=10)
          button1=Button(w1,text="Add Farmer",bg="olive",command=add_farmer,width=10,font=(15)) 
          button1.pack(pady=15)
          button2=Button(w1,text="state average",bg="olive",command=st_avg,width=10,font=(12))
          button2.pack(pady=15)
     else:
          messagebox.showerror("Login failed","incorrect username and password")
def add_farmer():  # this is for add farmer into the backend
    name=ent2.get()
    state=ent3.get() 
    rev=ent4.get()
    quy="INSERT INTO farmer_info(FarmerName,StateName,Revenue) VALUES(%s,%s,%s)"
    mycur.execute(quy,(name,state,rev))
    conn.commit()
    messagebox.showinfo("farmer","ADDED SUCCESSFULLY")
button1=Button(w,text="login",bg="olive",command=login,width=10,font=(15))
button1.pack(pady=18)
def st_avg(): # this is for average of individual state
    w=Tk()
    w.title("Average Revenue ")
    w.geometry('500x300')
    label1=Label(w,text="AVERAGE REVENUE OF THE STATES",bg="olive",font=(20 )) 
    label1.pack(pady=30)
    mycur=conn.cursor()
    def avg_apstate():  # this is for getting average of state from the backend
        qury="SELECT Revenue FROM farmer_info WHERE StateName='Andhrapradesh' "
        mycur.execute(qury)
        data=mycur.fetchall()
        if len(data)>0:
            avg=sum(da[0] for da in data )
            avg=avg/len(data)
            messagebox.showinfo("Average",f"{avg:.2f} is the Average revenue of the state")
        else:
            messagebox.showinfo("Average","Average revenue is not found for this state")
    def avg_telstate():  # this is for getting average of state from the backend
        qury="SELECT Revenue FROM farmer_info WHERE StateName='Telangana' "
        mycur.execute(qury)
        data=mycur.fetchall()
        if len(data)>0:
            avg=sum(da[0] for da in data )
            avg=avg/len(data)
            messagebox.showinfo("Average",f"{avg:.2f} is the Average revenue of the state") 
        else:
            messagebox.showinfo("Average","Average revenue is not found for this state")
    def avg_tnstate():  # this is for getting average of state from the backend
        qury="SELECT Revenue FROM farmer_info WHERE StateName='TamilNadu' "
        mycur.execute(qury)
        data=mycur.fetchall()
        if len(data)>0:
            avg=sum(da[0] for da in data ) 
            avg=avg/len(data)
            messagebox.showinfo("Average",f"{avg:.2f} is the Average revenue of the state") 
        else:
            messagebox.showinfo("Average","Average revenue is not found for this state")
    button1=Button(w,text="Andhrapradesh",bg="olive",command=avg_apstate,font=(10))
    button1.pack(pady=10)
    button2=Button(w,text="Telangana",bg="olive",command=avg_telstate,font=(10))
    button2.pack(pady=10) 
    button3=Button(w,text="Tamilnadu",bg="olive",command=avg_tnstate,font=(10))
    button3.pack(pady=10)
w.mainloop()


