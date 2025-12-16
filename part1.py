from fastapi import FastAPI
import uvicorn

app= FastAPI()

@app.get("/")
def greet():
    return "Hello Yamuna"

@app.get("/yamuna")
def add(a:int,b:int):
    return a+b

@app.post("/yamunapost")
def post_data(a:int,b:int):
    return a+b