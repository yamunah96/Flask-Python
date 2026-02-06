#User Registration Signin Signup
from customer import *
from bank import Bank
import random

from flask import request,redirect,url_for,session,render_template
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import LoginManager, UserMixin, login_required, logout_user, current_user, login_user
from user import User

def SignUp():
    username = request.form["username"]
    temp = db_query(f"SELECT username FROM customers where username = '{username}';")
    if temp:
        return "Username Already Exists"
    else:
        print("Username is Available Please Proceed")
        password = request.form["password"]
        name = request.form["name"]
        age = request.form["age"]
        city = request.form["city"]
        while True:
            account_number = int(random.randint(10000000, 99999999))
            temp = db_query(f"SELECT account_number FROM customers WHERE account_number = '{account_number}';")
            if temp:
                continue
            else:
                print("Your Account Number",account_number)
                break
        cobj = Customer(username, password, name, age, city, account_number)
        cobj.createuser()
        bobj = Bank(username, account_number)
        bobj.create_transaction_table()
        mydb.commit()
        redirect(url_for("SignIn"))

def Sign_in():
    username= request.form["username"]
    password=request.form["password"]
    temp = db_query(f"SELECT password FROM customers WHERE username = '{username}'")
    stored_hash= temp[0][0]
    if check_password_hash(stored_hash,password):
            user= User(username)
            login_user(user)
            session["username"]=username
            return redirect(url_for('dashboard'))
    else:
            return "Invalid creditional"
  
# 