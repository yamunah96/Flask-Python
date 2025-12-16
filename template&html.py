from flask import Flask, make_response,render_template,request,abort,url_for

app= Flask(__name__,template_folder="yamuna_templates")  # use when u have your own templates folder

# custome response
@app.route("/")
# def custom_response():
#     return render_template("index.html")


@app.route("/")
def create_ulList():
    mylist=[10,20,30,40,50]
    return render_template("index.html",mylist=mylist)

@app.route("/other")
def otherpage():
    return render_template("other.html")

@app.route("/form",methods=["GET","POST"])
def calculate():
    if request.method =="GET":
        return render_template("form.html")
    else:
        maths = request.form["maths"]
        science = request.form["science"]
        history = request.form["history"]

        # Validate input before converting
        if not (maths.replace('.', '', 1).isdigit() and 
                science.replace('.', '', 1).isdigit() and 
                history.replace('.', '', 1).isdigit()):
            abort(400, description="Invalid data type. Only numeric values allowed.")

        # Convert after validation
        maths = float(maths)
        science = float(science)
        history = float(history)

        average = round((maths + science + history) / 3, 2)

        return render_template("form.html", result=average)


if __name__ =="__main__":
    app.run(debug=True)