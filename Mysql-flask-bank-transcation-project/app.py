from flask import Flask, render_template,redirect,request,session,url_for
from bank import Bank
from customer import Customer
from database import db_query,mydb

from register import SignUp,Sign_in
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import LoginManager, UserMixin, login_required, logout_user, current_user, login_user
from user import User
app= Flask(__name__)
app.secret_key="yamuna"

# flask login setup
login_manger= LoginManager()
login_manger.init_app(app)
login_manger.login_view="SignIn"

@login_manger.user_loader
def load_user(username):
    temp=db_query(
        f"SELECT username FROM customers WHERE username = '{username}' AND status = 1;"
    )
    if temp:
        return User(username) 
    return None


@app.route("/",methods=["GET","POST"])
def SignIn():
    if request.method =="POST":
        Sign_in()
       
    return render_template("login.html")

@app.route("/signup",methods=["GET","POST"])
def Sign_up():
   if request.method =="POST":
       SignUp()
   return render_template("signup.html")

@app.route("/dashboard",methods=["GET","POST"])
@login_required
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
@login_required
def logout():
    session.pop("username",None)
    logout_user()
    return redirect(url_for("SignIn"))

@app.route("/deactivate")
@login_required
def deactivate():
    username= session["username"]
    db_query(
        f"UPDATE customers SET status = 0 WHERE username = '{username}' AND status = 1"
    )
    mydb.commit()
    session.pop("username",None)
    return redirect(url_for("SignIn"))
if __name__ =="__main__":
    app.run(debug=True)


