from fastapi import APIRouter, HTTPException

from schema.patients import patients, PatientCreate
from services.patients  import PatientService

patient_router = APIRouter()

@patient_router.get('/', status_code=200)
def get_patients():
    data = PatientService.parse_patients(patient_data=patients)
    return {'message': 'successful', 'data': data}

@patient_router.get('/{patient_id}', status_code=200)
def get_patient_by_id(patient_id: int):
    data =  PatientService.get_patient_by_id(patient_id)
    return {'message': 'successful', 'data': data} 

@patient_router.post('/', status_code=201)
def create_patient(reload: PatientCreate):
    data = PatientService.create_patient(reload)
    return {'message': 'Created', 'data': data}

@patient_router.put('/{patient_id}', status_code=200)
def edit_patient(patient_id: int, reload: PatientCreate):
    data = PatientService.edit_customer(reload)
    return {'message': 'success', 'data': data}

@patient_router.delete('/{patient_id}')
def delete_patient(patient_id: int):
    PatientService.delete_patient(patient_id)
    return {'messge': 'user deleted successfully.'}