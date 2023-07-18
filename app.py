from flask import Flask,redirect,url_for,render_template,request
import password_manager
import _show_pass
import Generater
app = Flask(__name__)

list_,pre,passw=[],[],[]

##@app.route("/profile")
##def profile():
##    p_img="C:\Users\Milind\Desktop\boot\Milind.jpg"
##    return render_template("Main.html",j=p_img)
@app.route("/mail")
def mail():
    import smtplib
    from email.message import EmailMessage
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    def email_alert(subject,to):
        msg=msg = MIMEMultipart('alternative')
        msg['Subject']=subject
        msg['to']=to

        user="pmgroup.alert@gmail.com"
        msg['from']=user
        password="xknvmrhrulljsond"


        text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
        html = """\
        <html>
          <head><title>go</title></head>
          <body>
            <p>Password Manager</p>
            <p>Do not share OTP(One Time Password) with any one<br>
            </p>
            <input type="text" palceholder="OTP" value="123" readonly>
          </body>
        </html>
        """

        # Record the MIME types of both parts - text/plain and text/html.
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
        msg.attach(part1)
        msg.attach(part2)




        sever=smtplib.SMTP("smtp.gmail.com",587)
        sever.starttls()
        sever.login(user,password)
        sever.send_message(msg)

        sever.quit()
        
    email_alert("py","milindshivampandey@gmail.com")
    print("successfuly\nplease check you mail")
    return "<center><h1 style= font-color:red> we sended you login page to your email</h1></center>"


@app.route("/login", methods=["POST","GET"])
def login():
    if request.method=="POST":
            if request.form['Login']=='Login':
                user_id=request.form["user_id"]
                list_.append(user_id)
                user_pass=request.form["user_pass"]
                
                if password_manager.login_database(user_id,user_pass):
                    return redirect(url_for("welcome"))
                else:
                    return render_template("index.html")
                return render_template("index.html")    


            else:
                return render_template("index.html")
    else:
        return render_template("index.html")


@app.route("/welcome")
def welcome():
    return render_template("after_login.html")
#-----------------hyperlike of after_login-------------------------------------
@app.route("/signup", methods=["POST","GET"])
def signup():
    if request.method=="POST":
            if request.form['Signup']=='Signup':
                new_user_=request.form["nuser_id"]
                new_pass=request.form["nuser_pass"]
                _show_pass.new_user(new_user_,new_pass)

            else:
                return render_template("signup.html")
    else:
        return render_template("signup.html")


    return redirect(url_for("login"))

@app.route("/show_pass")
def show_pass():
    user_id=list_[0]
    passwords=_show_pass.show_pass(user_id)
    return render_template("show_pass.html",password=passwords)
@app.route("/insert_pass", methods=["POST","GET"])
def insert_pass():
    user_id=list_[0]
    if request.method=="POST":
            if "Insert_password" in request.form :
                site_=request.form["site"]
                passw.append(site_)
                site_pass=request.form["password"]
                passwords=_show_pass.insert_password(user_id,site_,site_pass)

            elif "Auto" in request.form:
                site_=request.form["site"]
                auo=Generater.generate_pass(10)
                return render_template("insert_pass_after_ato.html",auto=auo,site=site_)
            else:
                return render_template("insert_pass.html")
    else:
        return render_template("insert_pass.html")
    return redirect(url_for("show_pass"))


@app.route("/update_pass",methods=["POST","GET"])
def update_pass():
    user_id=list_[0]
    if request.method=="POST":
            if request.form['Update']=='Update':
                site_=request.form["site"]
                site_npass=request.form["npassword"]
                passwords=_show_pass.Update_Password(user_id,site_,site_npass)

            else:
                return render_template("update_pass.html")
    else:
        return render_template("update_pass.html")
    
    return redirect(url_for("show_pass"))
@app.route("/delete_pass",methods=["POST","GET"])
def delete_pass():
    user_id=list_[0]
    if request.method=="POST":
            if request.form['Delete']=='Delete':
                site_=request.form["site"]
                passwords=_show_pass.delete_password(user_id,site_)

            else:
                return render_template("delete_pass.html")
    else:
        return render_template("delete_pass.html")

    return redirect(url_for("show_pass"))



@app.route("/forget",methods=["POST","GET"])
def forget():
    _show_pass.pin()
    print("please check you email milind")
    if request.method=="POST":
        if "next" in request.form :
            user_id=request.form["user_id"]           
            pre.append(user_id)
            chack_=request.form["user_pass"]
            ch_=0
            passwords=_show_pass.otp_ch(user_id,chack_)
##if we close the web page than it not remove the data
            if _show_pass.ch_[0]==1:
                return redirect(url_for("new"))
            else:
                ch_=0
                print(ch_)
                _show_pass.ch_.pop()
                print(_show_pass.ch_)
                print(ch_)
                return redirect(url_for("forget"))
        else:
            return render_template("forget.html")
    else:
        return render_template("forget.html")

    return redirect(url_for("new",pre=pre))


@app.route("/new",methods=["POST","GET"])
def new():
    name=pre[0]
    if request.method=="POST":
        if "submit" in request.form :
            user_id=request.form["user_id"]
            user_pass=request.form["pass"]
            passwords=_show_pass.inpass(user_id,user_pass)

        else:
            return render_template("forget_.html",prer=name)
    else:
        return render_template("forget_.html",prer=name)

    return redirect(url_for("login"))






@app.route("/logout",methods=["POST","GET"])
def logout():
    list_.pop()
    print(list_)
    return redirect(url_for("login"))
if __name__ == '__main__':
    app.run()
