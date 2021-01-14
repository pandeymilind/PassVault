import mysql.connector
import time
import password
a=mysql.connector.connect(host="localhost", user="root",passwd="123456789")
b=a.cursor()    
def welcome(con):
    while con:
        print("1.Login\n2.sign in\n3.Exit")
        t_user=str(input("Enter 1 or 2 : "))
        if t_user=="1":#Old User
            
            user_id=input("Enter user id")
            user_pass=input("Enter password")
            login_database(user_id,user_pass)
            con=0

        elif t_user=="2":#New User
            new_user=input("Enter user id")
            if database_check(new_user):
                print("id already exist")
            else:
                new_pass=input("Enter password")
                c=a.cursor()
                c.execute("use login_")
                command="insert into user values('"+new_user+"','"+new_pass+"')"
                c.execute(command)
                a.commit()
                command="create table "+new_user+" ("+" site char(30), Password char(20)"+")"
                c.execute(command)
                print("Account created login for access")
                NEW_user_id=input("Enter user id")
                NEW_user_pass=input("Enter password")
                
                login_database(NEW_user_id,NEW_user_pass)
        elif t_user=="3":
            print("Thank You")
            exit()
            
                
                
            ##check it previus exit or not

            
        else:
            print("wrong choice try again")

def Welcomw(name):
    print("Welcome "+name)
    
def show_password(user_id):
    c=0
    cor=a.cursor()
    command_="select * from "+user_id
    cor.execute(command_)
    for i in cor :
               
        print(i)
        c+=1
    if not c:
        print("No database found!")
    after_login(user_id)


def insert_password(user_id):
    new_site=input("Enter your site")
    option=int(input("1.generate password\n2.Enter own password\nEnter your choice:  "))
    if option==2:#Enter own password
        new_pass=input("Enter your new password")
    elif option==1:#generate password
        new_pass=password.generate_pass()
    else:
        print("wrong choice")
        after_login(user_id)
        
    cor=a.cursor()
    command_="insert into "+user_id+" values ('"+ new_site +"' , '"+new_pass+"' )"
    cor.execute(command_)
    a.commit()

def after_login(user_id):
    print("1.Show Password\n2.Insert Password\n3.Logout")
    ask_pass=int(input("Enter your Choice  "))
  
    if ask_pass==1:#Show Password
        show_password(user_id)
    elif ask_pass==2:#Insert Password
        insert_password(user_id)
        show_password(user_id)
    elif ask_pass==3:#Logout
        print("loging out")
        time.sleep(3)
        print("Logout successful")
        con=1
        welcome(con)
    else:
        print(welcomw(user_id))
        
def login_database(user_id,user_pass):
    d={}
    p=b.execute("use login_")
    b.execute("select * from user")
    x=b.fetchall()
    for i in x:
        d[i[0]]=i[1]
    if user_id in d.keys():
        if d[user_id]==user_pass:
            print("Login success")
            Welcomw(user_id)
            after_login(user_id)
            
        else:
            print("password wrong")
            welcome(1)
    else:
        print("Wrong User id")
        welcome(1)

def database_check(user_id):
    all_users=[]
    p=b.execute("use login_")
    b.execute("select * from user")
    x=b.fetchall()
    for i in x:
        all_users.append(i[0])

    if user_id in all_users:
        return 1
    else:
        return 0
welcome(1)

