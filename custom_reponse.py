from flask import Flask, make_response

app= Flask(__name__)

# custome response
@app.route("/custom")
def custom_response():
    response= make_response("hello world \n")
    response.status_code=202
    response.headers['content-type']="text/plain"
    return response

if __name__ =="__main__":
    app.run(debug=True)