import mysql.connector
import random
from tabulate import tabulate
import gogmail

a=mysql.connector.connect(host="localhost", user="root",passwd="12345")
cor=a.cursor()
cor.execute("use login_")
def show_pass(user_id):
    cor.execute("use login_")
    ab=[]
    command_="select * from "+user_id
    cor.execute(command_)
    for i in cor :
        ab.append(i)
    return ab

def Update_Password(user_id,site_,new_pass_):

##for update password-------------------
    update=a.cursor()
    command="update "+ user_id +" set Password= '"+new_pass_+"' where site= '"+site_+"'"
    update.execute(command)
    a.commit()


def insert_password(user_id,new_site,new_pass):      
    cor=a.cursor()
    command_="insert into "+user_id+" values ('"+ new_site +"' , '"+new_pass+"' )"
    cor.execute(command_)
    a.commit()

def delete_password(user_id,site_):
    cor=a.cursor()
    command="delete from "+ user_id +" where site= '"+site_+"'"
    cor.execute(command)
    a.commit()
##---------------------------------------------------------------------------------
def database_check(user_id):
    
    all_users=[]
    
    cor.execute("use login_")
    
    cor.execute("select * from user")
    
    x=cor.fetchall()
    
    for i in x:
        all_users.append(i[0])

    if user_id in all_users:
        return 1
    else:
        return 0
##---------------------------------------------------------------------------------

##---------------------------------------------------------------------------------------
def new_user(new_user,new_pass):  

    if database_check(new_user):
        return  "no"
    else:    
        c=a.cursor()
        c.execute("use login_")
        command="insert into user values('"+new_user+"','"+new_pass+"')"
        c.execute(command)
        a.commit()
        command="create table "+new_user+" ("+" site char(30), Password char(20)"+")"
        c.execute(command)
##-------------------------------------------------------------------------------------------




##--------------------------forget password---------------------------------
def pin():
        
    gama=("1","2","3","4","5","6","7","8","9","0")
    PIN=random.choices(gama,k=4)
    global otp_
    otp_="".join(PIN)
    pin_=str(otp_)
    meanin=[otp_,]
    mean=[meanin,]
    OTP_=tabulate(mean)
    ##----------------------------------------------------------------------------
    with open("OTP.txt","w") as otp_file:
        otp_file.write(OTP_)
    #-----------------------------sending mail---------------------------------
        gogmail.email_alert("Password",pin_,"milindshivampandey@gmail.com")

##----------------------------------------------------------------------------
ch_=[]
def otp_ch(user_id,chack_):
        
    if chack_==otp_:
        ch_.append(1)
    else:
        ch_.append(2)
#--check_ is for otp check,new_Pass is is new password
##----------------------------------------------------------------------------
def inpass(user_id,new_pass):
    command="update user set pass= '"+new_pass+"' where id= '"+user_id+"'"
    cor.execute(command)
    a.commit()
