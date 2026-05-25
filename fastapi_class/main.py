from fastapi import FastAPI
from adder import add
app = FastAPI()

@app.get("/")
def index(num1: int, num2: int):
    rs = add.add_num(num1, num2)
    return f"Ans is {rs}"

@app.get("/name")
def index(n: str):
    return f"Your name is {n}"

@app.post("/record")
def process_record(d: dict):
    return f"Data is {d}"