from fastapi import FastAPI

app = FastAPI()

students = {
    1:{
        "name": "john"'
        "age": 18
        "class": "Year 15"
        "sex": "male"
    }
}

@app.get("/")
def index():
    return {"name": "First Name"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int):
    return students[student_id]