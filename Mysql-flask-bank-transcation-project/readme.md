# 🏦 Flask MySQL Bank Transaction Project

A **simple bank transaction web application** built using **Python Flask** and **MySQL**.  
This project simulates core banking features such as user authentication, balance management, deposits, withdrawals, and account deactivation.

---

## 📌 Project Description

This application allows users to create an account, log in securely, and perform basic banking operations.  
It uses **Flask-Login** for authentication, **hashed passwords** for security, and a **MySQL database** for persistent storage.

The project follows a **modular structure**, separating business logic (Bank, Customer, User) from routes and database operations.

---

## 🚀 Features

- User signup and secure login
- Password hashing using Werkzeug
- Deposit and withdraw money
- View account balance on dashboard
- Account deactivation using soft delete (`status` flag)
- Session handling with Flask-Login
- MySQL database integration

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask  
- **Database:** MySQL  
- **Authentication:** Flask-Login  
- **Security:** Werkzeug password hashing

<h3>Customer Table in database</h3>
<img src="https://github.com/yamunah96/Flask-Python/blob/main/Mysql-flask-bank-transcation-project/images/customer%20table.png"/>
<h3>Transcation Table in database</h3>
<img src="https://github.com/yamunah96/Flask-Python/blob/main/Mysql-flask-bank-transcation-project/images/transcation%20table.png"/>
