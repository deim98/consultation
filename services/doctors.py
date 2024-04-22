from fastapi import HTTPException
from schema.doctors import Doctors, DoctorCreate, doctor


class DoctorService:

    @staticmethod
    def parse_doctors(doctor_data):
        data =[]
        for doctor in doctor_data:
            data.append(doctors[doctor])
        return data
    

    @staticmethod
    def get_doctors_by_id(doctor_id):
        patient = doctors.get(doctor_id)
        if not doctor:
            raise HTTPException(detail='Doctor not found.', status_code=404)
        return doctor
    

    @staticmethod
    def create_doctor(doctor_data: DoctorCreate):
        id = len(doctors)
        doctor = Doctors(
            id=id,
            **doctor_data.model_dump()
        )
        doctors[id]= doctor
        return doctor
    
    @staticmethod
    def edit_doctor(reload: DoctorCreate):
        id = len(doctors)
        doctor = Doctors(
            id=id,
            **reload.model_dump()
        )
        doctors[id]= doctor
        return doctor
    
    @staticmethod
    def delete_doctor(doctor_id: int):
        doctor = doctors.get(doctor_id)
        if not doctor:
            raise HTTPException(detail='Doctor not found.', status_code=404)
        del doctors[doctor_id]
                           