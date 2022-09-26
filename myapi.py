from pathlib import Path
from fastapi import FastAPI

app = FastAPI()

students = {
    1:{
        "name": "john",
        "age": 18,
        "class": "Year 15",
        "sex": "male"
        "sport": "soccer"
    }
}

#@app.get("/")
#def index():
 #   return {"name": "First Name"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(None, description="the ID of the student you want to view", gt=0 lt=3)):
    return students[student_id]