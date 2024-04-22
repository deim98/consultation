from pydantic import BaseModel

class Patient(BaseModel):
    id: int
    firstname: str
    lastname: str
    phone: str
    height: float
    weight: float
    age: int
    sex: str

class PatientCreate(BaseModel):
    firstname:str
    lastname: str
    age: int
    sex: str
    height: float
    weight: float
    phone: str

patients: list[Patient] = [
    Patient(id= 0, firstname='Funke', lastname='Akindele', age= 25, sex='Female', height= 165, weight= 75, phone= '0705678998'),
    Patient(id= 1, firstname='Jeffery', lastname='Francis', age= 90, sex='Male', height= 195, weight= 90, phone= '0805874976'),
    Patient(id= 2, firstname='Aisha', lastname='Umar', age= 19, sex='Female', height= 150, weight= 55, phone= '0702673695'),
    ]

