from flask import Flask, make_response,render_template,request,abort,url_for,session

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
def session_page():
    return render_template("session&cookies.html")


@app.route("/setsession")
def set_session():
    session["name"]="yamuna"
    session["course"]="python"
    return render_template("session&cookies.html",message_session="session data added")

@app.route("/get_session_data")
def get_session_data():
    if "name" in session.keys() and 'course' in session.keys():
        name=session['name']
        course= session["course"]
        return render_template("session&cookies.html",message_session=f"Name {name},Course {course}")
    else:
        return render_template("session&cookies.html",message_session=f"No data in session")
    
@app.route("/updatesession")
def update_session():
    if "name" in session.keys() and 'course' in session.keys():
        new_data={
            "name":"vinod","course":"AI"
        }
        session.update(new_data)
        return render_template("session&cookies.html",message_session=f"updated the session")
    else:
        return render_template("session&cookies.html",message_session=f"Unable to find the keys")

@app.route("/cleardata")
def clear_session():
    session.clear()
    # session.pop("name") # we can clear the particular key data also
    return render_template("session&cookies.html",message_session="Session Data cleared")

@app.route("/add_cookies")
def add_cookies():
    response= make_response(render_template("session&cookies.html",message_cookie="cookies added"))
    response.set_cookie(key="cookie_name_yamuna",value="yamuna cookies")
    return response
  
@app.route("/get_cookies")
def get_cookies():
    if "cookie_name_yamuna" in request.cookies.keys():
        cookie_value= request.cookies['cookie_name_yamuna']
        return render_template("session&cookies.html",message_cookie=f"{cookie_value} is fetched")
    else:
        return render_template("session&cookies.html",message_cookie=f"dont have any cookies to fetch")
    
@app.route("/clear_cookies")
def clear_cookies():
    response= make_response(render_template("session&cookies.html",message_cookie="cookies removed"))
    response.set_cookie(key="cookie_name_yamuna",expires=0)
    return response

@app.route("/update_cookies")
def update_cookies():
    if "cookie_name_yamuna" in request.cookies:
        response = make_response(
            render_template("session&cookies.html", message_cookie="Cookie updated")
        )
        response.set_cookie("cookie_name_yamuna", "cookie name updated to vinod")
        return response
    else:
        return render_template("session&cookies.html", message_cookie="Cookie not found")


if __name__ =="__main__":
    app.run(debug=True)


# sql database(sqlalchemy) (FASTAPI) (REST API, FASTAPI)