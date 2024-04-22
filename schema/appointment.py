from pydantic import BaseModel

from schema.patients import Patient, patients 
from schema.doctors import Doctors, doctor


class Appointment(BaseModel):
    id: int
    patient_id: Patient
    doctor_id: Doctors
    date: str


class AppointmentCreate(BaseModel):
    patient_id: int
    doctor_id: int
    date: str


appointments: list[Appointment] =[
    Appointment(
        id = 0, patient_id=Patient[0], doctor_id= Doctors[0], date= '15/04/2024'
    )
]