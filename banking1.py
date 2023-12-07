#imports
from tkinter import*
import os
from PIL import ImageTk,Image

def passwordCheck(password):
    if len(password)<8:
        return False
    sp=0
    up=0
    low=0
    num=0
    special=['~','`','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}',']','|','\\',':',';','"',"'",'<','>','.','?','/']
    for i in password:
        if i in special:
            sp+=1
        elif i.isnumeric():
            num+=1
        elif i.isalpha():
            if i.islower():
                low+=1
            else:
                up+=1
        elif i=='=':
            return False
    if (sp==0 or low==0 or up==0 or num==0):
        return False
    return True
    
    

#Main screen
root=Tk()
root.title("Banking App")
root.geometry('250x450')

def finish_reg():
    name=temp_name.get()
    Mob=temp_Mob.get()
    age=temp_age.get()
    gender=temp_gender.get()
    password=temp_password.get()
    all_accounts=os.listdir()
    if name == "" or Mob =="" or age =="" or gender =="" or password == "":
        (notif.config(fg="red",text="All field are required* "))   
        return
    if int(age) <18 or int(age)>100:
      notif.config(fg="red",text="please enter the valid age")
      return
    gender=gender.upper()
    if gender not in ["MALE","FEMALE","TRANS"]:
       (notif.config(fg="red",text="Invalid gender!!"))   
       return
    if len(Mob)!=10 or not(Mob.isnumeric()):
        (notif.config(fg="red",text="Invalid mobile number!!"))
        return
    if not(passwordCheck(password)):
        (notif.config(fg="red",text="Please enter a valid password!!"))
        return

    
    for name_check in all_accounts:
        print(name_check)
        if name==name_check:
            notif.config(fg="red",text="Account already exist")
            return
        else:
            new_file=open(name,"w")
            new_file.write('0'+'\n')
            new_file.write(name+'\n')
            new_file.write(Mob+'\n')
            new_file.write(age+'\n')
            new_file.write(gender+'\n')
            new_file.write(password+'\n')
            
            new_file.close() 
            notif.config(fg="green",text="Account has been created")
   
#Functions
def register():

    global temp_name
    global temp_Mob
    global temp_age
    global temp_gender
    global temp_password
    global notif
    
    

    temp_name=StringVar()
    temp_Mob=StringVar()
    temp_age=StringVar()
    temp_gender=StringVar()
    temp_password=StringVar()

    register_screen=Toplevel(root)
    register_screen.title('Register')
    register_screen.resizable(False,False)
    #Labels
    Label(register_screen,text="Please enter your detail to register",fg="Black",bg='#99FF00',font=('calibri',12)).grid(row=0,sticky=N,pady=10)
    Label(register_screen,text="Name",font=('calibri',12)).grid(row=1,sticky=W)
    Label(register_screen,text="Mob",font=('calibri',12)).grid(row=2,sticky=W)
    Label(register_screen,text="Age",font=('calibri',12)).grid(row=3,sticky=W)
    Label(register_screen,text="Gender",font=('calibri',12)).grid(row=4,sticky=W)
    Label(register_screen,text="Password",font=('calibri',12)).grid(row=5,sticky=W) 
    notif=Label(register_screen,font=('calibri',12))
    notif.grid(row=8,sticky=N,pady=10)
    #Entries
    Entry(register_screen,textvariable=temp_name).grid(row=1,column=1)
    Entry(register_screen,textvariable=temp_Mob).grid(row=2,column=1)
    Entry(register_screen,textvariable=temp_age).grid(row=3,column=1)
    Entry(register_screen,textvariable=temp_gender).grid(row=4,column=1)
    Entry(register_screen,textvariable=temp_password,show="*").grid(row=5,column=1)


    #Buttons
    Button(register_screen,text="Register",command=finish_reg,font=('Calibri',12)).grid(row=6,sticky=N,pady=10)
def login_session():
   global login_name
   all_accounts=os.listdir()
   login_name=temp_login_name.get()
   login_password=temp_login_password.get()
   
   for name in all_accounts:
       if name==login_name:
           file=open(name,"r")
           file_data=file.read()
           file_data=file_data.split('\n')
           password=file_data[5]
           #account dashboard
           if login_password==password:
               login_screen.destroy()
               account_dashboard=Toplevel(root)
               account_dashboard.title('Dashboard')
               #labels
               account_dashboard.resizable(False,False)
               Label(account_dashboard,text="Account Dashboard",font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
               Label(account_dashboard,text="Welcome"+" "+name,font=('Calibri',12)).grid(row=1,sticky=N,pady=5)

               Button(account_dashboard,text="Personal Details",font=('Calibri',12),width=30,command=Personal_Details).grid(row=2,sticky=N,padx=10)
               Button(account_dashboard,text="Deposit",font=('Calibri',12),width=30,command=deposit).grid(row=3,sticky=N,padx=10)
               Button(account_dashboard,text="Withdraw",font=('Calibri',12),width=30,command=Withdraw).grid(row=4,sticky=N,padx=10)
    
               Label(account_dashboard).grid(row=6,sticky=N,pady=10)
               return
           else:
               login_notif.config(fg="red",text="Password incorrect!!")
               return
   login_notif.config(fg="red",text="No account Found!!")
def deposit():
    global amount
    global deposit_notif
    global current_balance_label
    global updated_balance
    amount=StringVar()
    file=open(login_name,"r")
    file_data=file.read()
    user_details=file_data.split('\n')
    details_balance=user_details[0]
    deposit_screen=Toplevel(root)
    deposit_screen.title('Deposit')
    Label(deposit_screen,text="Deposit",font=('calibri',12)).grid(row=0,sticky=N,pady=10)
    current_balance_label=Label(deposit_screen,text="Current Balance : "+ details_balance,font=('calibri',12))
    current_balance_label.grid(row=1,sticky=W)
    Label(deposit_screen,text="Amount",font=('calibri',12)).grid(row=2,sticky=W)
    deposit_notif=Label(deposit_screen,font=('calibri',12))
    deposit_notif.grid(row=4,sticky=N,pady=5)

    
   #Entry
    Entry(deposit_screen,textvariable= amount).grid(row=2,column=1)
    Button(deposit_screen,text="Finish",font=('Calibri',12),command=finish_deposit).grid(row=3,sticky=W,pady=5)
    
def finish_deposit():
    global updated_balance
    if amount.get()=="":
        deposit_notif.config(text="Amount is required",fg="red")
    if float(amount.get())<=0:
        deposit_notif.config(text=" Negative Amount  and zero amount is Not Accepted",fg="red")
        return
    file=open(login_name,'r+')
    file_data=file.read()
    details=file_data.split('\n')
    current_balance=details[0]
    updated_balance=current_balance
    updated_balance=float(updated_balance)+float(amount.get())
    file_data=file_data.replace(current_balance,str(updated_balance),1)
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()
    current_balance_label.config(text="Current balance :"+str(updated_balance),fg='green')
    deposit_notif.config(text="Balance Updated",fg='green')
def Withdraw():
    global Withdraw_amount
    global Withdraw_notif
    global current_balance_label
    global updated_balance
    Withdraw_amount=StringVar()
    file=open(login_name,"r")
    file_data=file.read()
    user_details=file_data.split('\n')
    details_balance=user_details[0]
    Withdraw_screen=Toplevel(root)
    Withdraw_screen.title('Withdraw')
    Label(Withdraw_screen,text="Withdraw",font=('calibri',12)).grid(row=0,sticky=N,pady=10)
    current_balance_label=Label(Withdraw_screen,text="Current Balance : "+ details_balance,font=('calibri',12))
    current_balance_label.grid(row=1,sticky=W)
    Label(Withdraw_screen,text="Amount",font=('calibri',12)).grid(row=2,sticky=W)
    Withdraw_notif=Label(Withdraw_screen,font=('calibri',12))
    Withdraw_notif.grid(row=4,sticky=N,pady=5)

    
   #Entry
    Entry(Withdraw_screen,textvariable= Withdraw_amount).grid(row=2,column=1)
    Button(Withdraw_screen,text="Finish",font=('Calibri',12),command=finish_Withdraw).grid(row=3,sticky=W,pady=5)
    
def finish_Withdraw():
    global updated_balance
    global current_balance
    if Withdraw_amount.get()=="":
        Withdraw_notif.config(text="Withdraw amount is required",fg="red")
    if float(Withdraw_amount.get())<=0:
        Withdraw_notif.config(text=" Negative WithdrawAmount  and zero amount is Not Accepted",fg="red")
        return
   

    file=open(login_name,'r+')
    file_data=file.read()
    details=file_data.split('\n')
    current_balance=details[0]
    if float(Withdraw_amount.get())>float(current_balance):
        Withdraw_notif.config(text="Insufficient amount",fg="red")
        return
    updated_balance=current_balance
    updated_balance=float(updated_balance)-float(Withdraw_amount.get() )
    file_data=file_data.replace(current_balance,str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()
    current_balance_label.config(text="Current balance :"+str(updated_balance),fg='green')
    deposit_notif.config(text="Balance Updated",fg='green')

def Personal_Details():
    file=open(login_name,'r')
    file_data=file.read()
    user_details=file_data.split('\n')
    details_name=user_details[1]
    details_Mob=user_details[2]
    details_age=user_details[3]
    details_gender=user_details[4]
    details_balance=user_details[0]

    personal_details_screen=Toplevel(root)
    personal_details_screen.title("Personal Details")
    #labels
    personal_details_screen.resizable(False,False)
    Label(personal_details_screen,text="Personal Details",font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    Label(personal_details_screen,text="Name : "+details_name,font=('Calibri',12)).grid(row=1,sticky=W)
    Label(personal_details_screen,text="Mob : "+details_Mob,font=('Calibri',12)).grid(row=2,sticky=W)
    Label(personal_details_screen,text="Age : "+details_age,font=('Calibri',12)).grid(row=3,sticky=W)
    Label(personal_details_screen,text="Gender : "+details_gender,font=('Calibri',12)).grid(row=4,sticky=W)
    Label(personal_details_screen,text="Balance : "+details_balance,font=('Calibri',12)).grid(row=5,sticky=W)
def login():
    global temp_login_name
    global temp_login_password
    global login_notif
    global login_screen

    temp_login_name=StringVar()
    temp_login_password=StringVar()
    #login screen
    login_screen=Toplevel(root)
    login_screen.title('Login')
    #labels
    login_screen.resizable(False,False)
    Label(login_screen,text="Login to your account",font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    Label(login_screen,text="Username",font=('Calibri',12)).grid(row=1,sticky=N,pady=10)
    Label(login_screen,text="Password",font=('Calibri',12)).grid(row=2,sticky=N,pady=10)
    login_notif=Label(login_screen,font=('Calibri',12))
    login_notif.grid(row=4,sticky=N)
    #entries
    Entry(login_screen,textvariable=temp_login_name).grid(row=1,column=1,padx=5)
    Entry(login_screen,textvariable=temp_login_password).grid(row=2,column=1,padx=5)
   #button
    Button(login_screen,text='Login',command=login_session,width='15',font=('Calibri',12)).grid(row=3,sticky=W,pady=5,padx=5)


#Image Import

img=ImageTk.PhotoImage(Image.open('download.png'))
# img = Image.resize((80,80),Image.ANTIALIAS)
img_label=Label(root,image=img)
root.configure(background="Orange")
# bg = PhotoImage(file='result.png')

# win_width = root.winfo_width()
# win_height = root.winfo_height()

root.resizable(False,False)
#Labels
Label(root,text="Public Bank Of India(PBI)",fg="Black",bg='#55e3f2',font=('Calibri',14)).grid(row=0,sticky=N,pady=10)
Label(root,text="Credibility Makes The Relation Strong",fg="Black",bg='#55e3f2',font=('Calibri',12)).grid(row=1,sticky=N)
Label(root,image=img, bg="Blue").grid(row=2,sticky=N,pady=15)
#BUTTONS
Button(root,text="Register",font=('Calibri',12),width=20,command=register,bg="Pink").grid(row=3,sticky=N)
Button(root,text="Login",font=('Calibri',12),width=20,command=login,bg="Pink").grid(row=4,sticky=N,pady= 10)

root.mainloop()