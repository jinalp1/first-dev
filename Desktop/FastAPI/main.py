
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Model for Employee
class Employee(BaseModel):
    id: int
    name: str
    age: int
    experience: int | None = None

# Dummy database
EMPLOYEE_DB = []

# Create employee
@app.post("/employees/")
def create_employee(create: Employee):
    EMPLOYEE_DB.append(create)
    return {"message": "Employee created successfully"}

# Read All employees
@app.get("/employees/", response_model=List[Employee])
def read_employees():
    return EMPLOYEE_DB

# Read One employee
@app.get("/employees/{employee_id}", response_model=Employee)
def read_employee(employee_id: int):
    for i in EMPLOYEE_DB:
        if i.id == employee_id:
            return i
    raise HTTPException(status_code=404, detail="Employee not found")

# Delete employee
@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    for ind, emp in get_employee(EMPLOYEE_DB):
        if emp.id == employee_id:
            del EMPLOYEE_DB[ind]
            return {"message": "Employee deleted successfully"}
    raise HTTPException(status_code=404, detail="Employee not found")

# Update employee
@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, update: Employee):
    for ind,emp in get_employee(EMPLOYEE_DB):
        if emp.id == employee_id:
            EMPLOYEE_DB[ind] = update
            return {"message": "Employee updated successfully"}
    raise HTTPException(status_code=404, detail="Employee not found")


def get_employee(EMPLOYEE_DB):
    i=0
    for i in range(len(EMPLOYEE_DB)):
        for j in EMPLOYEE_DB:
            yield i,j
            i+=1
    


