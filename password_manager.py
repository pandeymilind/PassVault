import mysql.connector
a=mysql.connector.connect(host="localhost", user="root",passwd="12345")
b=a.cursor()

#---------------------Login-------------------------------------------

def login_database(user_id,user_pass):
    d={}
    p=b.execute("use login_")
    b.execute("select * from user")
    x=b.fetchall()
    for i in x:
        d[i[0]]=i[1]
    if user_id in d.keys():
        if d[user_id]==user_pass:
            return 1
            
        else:
            return 0
    else:
        return 0
#-----------------------------------------------------------------------
