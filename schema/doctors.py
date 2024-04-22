from pydantic import BaseModel

class Doctors(BaseModel):
    id: int
    name: str
    specialization: str
    phone: str
    is_available: bool = True


class DoctorCreate(BaseModel):
    name: str
    specialization: str
    phone: str


doctor: list[Doctors] = [
    Doctors(id= 0, name= 'Adekunle Jabi', specialization= 'Gastroenterologist', phone= '08123457899')
    Doctors(id= 1, name='Olafunke Dumebi', specialization= 'Cardiologist', phone= '07023456788')
    Doctors(id= 2, name= 'Chigozie Iweaka', specialization= 'Nephrologist', phone= '0815432899')
]