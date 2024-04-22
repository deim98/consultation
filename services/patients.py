from fastapi import HTTPException
from schema.patients import Patient, PatientCreate, patients


class PatientService:

    @staticmethod
    def parse_patients(patient_data):
        data =[]
        for patient in patient_data:
            data.append(patients[patient])
        return data
    

    @staticmethod
    def get_patients_by_id(patient_id):
        patient = patients.get(patient_id)
        if not patient:
            raise HTTPException(detail='Patient not found.', status_code=404)
        return patient
    

    @staticmethod
    def create_patient(patient_data: PatientCreate):
        id = len(patients)
        patient = Patient(
            id=id,
            **patient_data.model_dump()
        )
        patients[id]= patient
        return patient
    
    @staticmethod
    def edit_patient(reload: PatientCreate):
        id = len(patients)
        patient = Patients(
            id=id,
            **reload.model_dump()
        )
        patients[id]= patient
        return patient
    
    @staticmethod
    def delete_patient(patient_id: int):
        patient = patients.get(patient_id)
        if not patient:
            raise HTTPException(detail='Patient not found.', status_code=404)
        del patients[patient_id]
                           