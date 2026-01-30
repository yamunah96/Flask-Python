from flask import Flask, render_template,redirect,request,session,url_for
from bank import Bank
from customer import Customer
from database import db_query,mydb

from register import SignUp

app= Flask(__name__)
app.secret_key="yamuna"

@app.route("/",methods=["GET","POST"])
def SignIn():
    if request.method =="POST":
        username= request.form["username"]
        password=request.form["password"]
        temp = db_query(f"SELECT password FROM customers WHERE username = '{username}'")
        if temp and temp[0][0] == password:
            session["username"]=username
            return redirect(url_for('dashboard'))
        else:
            return "Invalid creditional"

    return render_template("login.html")

@app.route("/signup",methods=["GET","POST"])
def Sing_up():
   if request.method =="POST":
       SignUp()
   return render_template("signup.html")

@app.route("/dashboard",methods=["GET","POST"])
def dashboard():
    if "username" not in session:
            return redirect(url_for("SignIn"))
    username= session["username"]
    acc= db_query(f"SELECT account_number FROM customers WHERE username = '{username}'")[0][0]

    bank= Bank(username,acc)
    if request.method=="POST":
        action= request.form["action"]
        amount= int(request.form["amount"])
        if action == "deposit":
            bank.deposit(amount)
        elif action =="withdraw":
            bank.withdraw(amount)
        mydb.commit()
    balance= db_query(f"SELECT balance FROM customers WHERE username = '{username}'")[0][0]

    return render_template("dashboard.html",username=username,balance=balance)


@app.route("/logout")
def logout():
    session.pop("username",None)
    return redirect(url_for("SignIn"))

if __name__ =="__main__":
    app.run(debug=True)

