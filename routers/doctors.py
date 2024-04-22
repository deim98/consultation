from fastapi import APIRouter, HTTPException

from schema.doctors import doctor, DoctorCreate
from services.doctors  import DoctorService

doctor_router = APIRouter()

@doctor_router.get('/', status_code=200)
def get_doctors():
    data = DoctorService.parse_patients(doctor_data=doctor)
    return {'message': 'successful', 'data': data}

@doctor_router.get('/{doctor_id}', status_code=200)
def get_doctor_by_id(doctor_id: int):
    data =  DoctorService.get_doctor_by_id(doctor_id)
    return {'message': 'successful', 'data': data} 

@doctor_router.post('/', status_code=201)
def create_doctor(reload: DoctorCreate):
    data = DoctorService.create_patient(reload)
    return {'message': 'Created', 'data': data}

@doctor_router.put('/{doctor_id}', status_code=200)
def edit_doctor(doctor_id: int, reload: DoctorCreate):
    data = DoctorService.edit_doctor(reload)
    return {'message': 'success', 'data': data}

@doctor_router.delete('/{doctor_id}')
def delete_doctor(doctor_id: int):
    DoctorService.delete_doctor(doctor_id)
    return {'messge': 'user deleted successfully.'}