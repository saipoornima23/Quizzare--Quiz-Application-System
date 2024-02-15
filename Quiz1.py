from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector as sql
import tkinter as tk
from tkinter import messagebox


root=Tk()
#getting screen width and height of display
width= root.winfo_screenwidth() 
height= root.winfo_screenheight()
#setting tkinter window size
root.geometry("%dx%d" % (width, height))
root.title("Quizarre")

mycon=sql.connect(host="localhost",user="root",passwd="dogood",database="project");
if mycon.is_connected()== False:
    print(" Database Not connected");
cursor=mycon.cursor();
     
                

# Admin Button clicked
def button1_clicked():
    button2.grid_forget()
    button1.grid_forget()
    buttonexit.grid_forget()
    label2=Label(frame2,text=" Enter Password",padx=100)
    label2.grid(row=2,column=0)
    password = StringVar() #Password variable
    passEntry = Entry(frame2, textvariable=password, show='*')
    button3 = Button(frame2, text='submit',command=lambda:submit(passEntry.get()))
    passEntry.grid(row=2,column=1,padx=100,pady=30)
    button3.grid(row=10,column=11)

#Admin password entered
def submit(pass1):
    clearFrame()
    
    cursor.execute("select pwd from adm_pwd");
    pwd1=cursor.fetchall()
    print(pwd1[0][0],pass1)
    if(pass1==pwd1[0][0]):
        
        label5=Label(frame2,text="Login sucessfull",padx=100)
        label5.grid(row=2,column=0)
        clearFrame()
        label7=Label(frame2,text="Welcome Admin,Choose options to proceed",font=("Times New Roman",20,"italic"))
        label7.grid(row=2,column=8)
        button8=Button(frame2,text="Change Password",padx=100,command=change_pwd)
        button9=Button(frame2,text="Winners Report",padx=102,command=win_report)
        button10=Button(frame2,text="Add/Modify Quiz",padx=100,command=mod_quiz)
        buttonexit=Button(frame2,text="Exit",padx=100,command=root.destroy)
        
        button8.grid(row=4,column=0,padx=50,pady=10)
        button9.grid(row=5,column=0,padx=50,pady=10)
        button10.grid(row=6,column=0,padx=50,pady=10)
        buttonexit.grid(row=7,column=0,padx=50,pady=10)
        
        
    else:
        #messagebox.showerror("showerror","Login failed")
        label6=Label(frame2,text="login failed",padx=100)
        label6.grid(row=2,column=0)
        buttonexit=Button(frame2,text="Exit",padx=100,command=root.destroy)
        buttonexit.grid(row=4,column=23,padx=50,pady=30)  
    return

#Player Button clicked
def button2_clicked():
    button2.grid_forget()
    button1.grid_forget()
    label3=Label(frame2,text=" Enter your  Name",padx=100)
    label3.grid(row=2,column=0)
    name = StringVar() 
    nameEntry = Entry(frame2, textvariable=name)
    button4 = Button(frame2, text='submit',padx=100,command=lambda:submit1(nameEntry.get()))
    nameEntry.grid(row=2,column=1)
    button4.grid(row=4,column=5,padx=50,pady=30)
   


# Player Name Submitted
def submit1(name):
    clearFrame()
    label4=Label(frame2,text="Choose your Topic",font=("Times New Roman",20,"italic"),background="#ffffff",justify="center")
    label4.grid(row=0,column=0,columnspan=2)
    button4 = Button(frame2, text='Current Affairs',command=lambda:submit3(name,"Current Affairs"))
    button5 = Button(frame2, text='Entertainment',command=lambda:submit3(name,"Entertainment"))
    button6 = Button(frame2, text='Countries and Capitals',command=lambda:submit3(name,"Countries and capitals"))
    button7= Button(frame2, text='Sports',command=lambda:submit3(name,"sports"))
    button4.grid(row=1,column=0,columnspan=2,padx=200)
    button5.grid(row=2,column=0,columnspan=2,padx=200)
    button6.grid(row=3,column=0,columnspan=2,padx=200)
    button7.grid(row=4,column=0,columnspan=2,padx=200)
    return

#Topic chosen
def submit3(name,category):
    clearFrame()
    fs=dbcon('sports_easy')
    cursor.execute("insert into player(pname,category,score) values('"+name+"','"+category+"','"+str(fs)+"')")
    mycon.commit()
    buttonexit=Button(frame2,text="Exit",padx=100,command=root.destroy)
    buttonexit.grid(row=4,column=23,padx=50,pady=30)

    
    return

def clearFrame():
    # destroy all widgets from frame
    for widget in frame2.winfo_children():
          widget.destroy()
     
    
   
# connecting Appropriate db for quiz
def dbcon(fname):
    score = 0
   
    mycon=sql.connect(host="localhost",user="root",passwd="dogood",database="project");
    if mycon.is_connected()== False:
        print(" Not connected")
    cursor=mycon.cursor()
    cursor.execute("select * from "+fname);
    data=cursor.fetchall()

    i=1

    for r in data:
        
         l1= Label(frame2,text="Score="+str(score),font=("Times New Roman",18,"italic"),background="#ffffff",justify="right")
         l1.grid(sticky=W,row=0,column=30)

         v= tk.IntVar()
         v.set(0)
         var=tk.IntVar()
           

            
         l2=Label(frame2,text=str(i)+".  "+r[0])

         l2.grid(row=1,column=0)
         r1=Radiobutton(frame2,text=r[1],variable=v,value=1)
         r1.grid(row=2,column=0)
         r2=Radiobutton(frame2,text=r[2],variable=v,value=2)
         r2.grid(row=3,column=0)
         r3=Radiobutton(frame2,text=r[3],variable=v,value=3)
         r3.grid(row=4,column=0)
         r4=Radiobutton(frame2,text=r[4],variable=v,value=4)
         r4.grid(row=5,column=0)
         button1=Button(frame2,text="Submit",padx=100,command=lambda: var.set(1))
         button1.grid(row=6,column=0)
         button1.wait_variable(var)
         print(v.get())
         
         if v.get()==r[5]:
             messagebox.showinfo("Show info","Ans correct")
             score= score+1
        
         else:
            messagebox.showinfo("show info","Ans incorrect")
         clearFrame()
   
    l3= Label(frame2,text="Final Score="+str(score),font=("Times New Roman",18,"italic"),background="#ffffff")
    l3.grid(sticky=W,row=2,column=30)
    return(score)

         
def change_pwd():
    clearFrame()
    label5=Label(frame2,text="Change password",font=("Times New Roman",20,"italic"),background="#ffffff",justify="center")
    label5.grid(row=0,column=4,columnspan=2)
    label6=Label(frame2,text="Enter Existing passsword",padx=50,pady=10,background="#ffffff",justify="center")
    label7=Label(frame2,text="Enter New Password",padx=50,pady=10,background="#ffffff",justify="center")
    label8=Label(frame2,text="Confirm Password",padx=50,pady=10,background="#ffffff",justify="center")
    
    password1= StringVar() #Password variable
    password2= StringVar()
    password3= StringVar()
    
    passEntry1= Entry(frame2, textvariable=password1, show='*')
    passEntry2= Entry(frame2, textvariable=password2, show='*')
    passEntry3= Entry(frame2, textvariable=password3, show='*')
    label6.grid(row=1,column=0)
    label7.grid(row=2,column=0)
    label8.grid(row=3,column=0)
    passEntry1.grid(row=1,column=6)
    passEntry2.grid(row=2,column=6)
    passEntry3.grid(row=3,column=6)
    

    
    
    button8=Button(frame2,text="Submit",padx=50,command=lambda:submit4( passEntry1.get(),passEntry2.get(),passEntry3.get()))
    button8.grid(row=4,column=3,padx=50,pady=30)
    buttonexit=Button(frame2,text="Exit",padx=50,command=root.destroy)
    buttonexit.grid(row=4,column=10,padx=50,pady=30)
   
    return
def submit4(p1,p2,p3):
   
    #passEntry2.get()
    #passEntry3.get()
    mycon=sql.connect(host="localhost",user="root",passwd="dogood",database="project");
    if mycon.is_connected()== False:
        print(" Database Not connected");
    cursor=mycon.cursor();
    cursor.execute("select pwd from adm_pwd");
    pwd1=cursor.fetchall()
    print(pwd1,p1,p2,p3)
    if pwd1[0][0]!=p1:
      messagebox.showerror("showerror","Incorrect Existing password")
    else:
      if p2!=p3:
          messagebox.showerror("showerror","Both New passwords dont match")
      else:
          print("update adm_pwd set pwd='"+p2+"'")
          cursor.execute("update adm_pwd set pwd='"+p2+"'")
          mycon.commit()
          messagebox.showinfo("showinfo","Password updated succesfully")
          clearFrame()
        
    return
def win_report():
    return
def mod_quiz():
    clearFrame()
    label4=Label(frame2,text="Choose your Topic",font=("Times New Roman",20,"italic"),background="#ffffff",justify="center")
    label4.grid(row=0,column=0,columnspan=2)
    button4 = Button(frame2, text='Current Affairs',command=submit5)
    button5 = Button(frame2, text='Entertainment',command=submit5)
    button6 = Button(frame2, text='Countries and Capitals',command=submit5)
    button7= Button(frame2, text='Sports',command=submit5)
    button4.grid(row=1,column=0,columnspan=2,padx=200)
    button5.grid(row=2,column=0,columnspan=2,padx=200)
    button6.grid(row=3,column=0,columnspan=2,padx=200)
    button7.grid(row=4,column=0,columnspan=2,padx=200)
    
    return
def submit5():
    return

     


canvas = Canvas(root, width=200, height=200, background="bisque")
canvas.pack(side="bottom", fill="both", expand=True)

#top frame
frame1=LabelFrame(canvas,background="#ffffff",padx=5,pady=5)
frame1.pack(padx=100,pady=10,fill="both")

labeltext=Label(frame1,text="Quizzare",font=("Comic sans MS",36,"bold"),
                background="#ffffff",padx=100)
labeltext.pack()


img1=ImageTk.PhotoImage(Image.open("world.jpg"))

labelimage=Label(frame1,image=img1,background="#ffffff",padx=100)
labelimage.pack()


labeltext1=Label(frame1,text="Unlocking Knowledge",font=("Comic sans MS",20,"italic"),
                background="#ffffff",padx=100)
labeltext1.pack()

# second frame
global button1,button2,buttonexit
frame2=LabelFrame(canvas,background="#ffffff")
frame2.pack(padx=100,pady=50,fill="both")
labeltext2=Label(frame2,text="Enter Login Details",font=("Times New Roman",20,"italic"),background="#ffffff",justify="center")

labeltext2.grid(row=0,column=20,columnspan=1)
button1=Button(frame2,text="Admin",padx=100,command=button1_clicked)

button1.grid(row=4,column=17,padx=100,pady=30)
button2=Button(frame2,text="Player",padx=100,command=button2_clicked)
button2.grid(row=4,column=20,padx=50,pady=30)
buttonexit=Button(frame2,text="Exit",padx=100,command=root.destroy)
buttonexit.grid(row=4,column=23,padx=50,pady=30)




mainloop()
