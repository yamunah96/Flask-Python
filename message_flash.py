from flask import Flask, make_response,render_template,request,abort,url_for,session,flash

# use when u have your own templates folder, and for static files like css, images,video, js 
app= Flask(__name__,template_folder="yamuna_templates",static_folder="static",static_url_path="/")  
'''
A secret key in Flask is used to encrypt and secure session data stored in the browser.
Without it, anyone could modify cookies or steal session information.
It ensures your app’s sessions are safe, tamper-proof, and trusted.
'''
app.secret_key="SOME KEY"

# custome response
@app.route("/")
def get_form():
    return render_template("main.html")


@app.route("/login",methods=["GET","POST"])
def login_flash():
    if request.method == "GET":
        return render_template("login.html")
    else:
        username= request.form.get("username")
        password= request.form.get("password")
        if username =="yamuna" and password =="123456":
            flash("Successful Login")
            return render_template("login.html",messages="")
        else:
            flash("Login Failed")
            return render_template("login.html",messages="")

if __name__ =="__main__":
    app.run(debug=True)