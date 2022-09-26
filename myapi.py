from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"name": "First Data" , "age": "Second Data" , "sex": "Third Data"}
