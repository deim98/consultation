from fastapi import HTTPException

from schema.appointment import Appointment, AppointmentCreate, appointments
from schema.doctors import Doctors, doctor
from schema.patients import Patient, patients
from utils.appointment import appointmentHelpers

class AppointmentService:

    @staticmethod
    def create_appointment(reload: AppointmentCreate):
        id = len(appointments)
        patient_id: Patient = patients[reload.patient_id]
        doctor_id: Doctors = doctor[reload.doctor_id]
        appointment = Appointment(
            id=id,
            patient_id= patient_id,
            doctor_id=doctor_id,
            date=reload.date
        )
        appointments.append(appointment)
        return appointment
    
    @staticmethod
    def get_appointment_by_id(appointment_id: int):
        appointment = appointmentHelpers.get_appointment_by_id(appointment_id)
        if not appointment:
            raise HTTPException(detail='appointment not found', status_code=404)
        return appointment
    
    @staticmethod
    def edit_appointment(appointment_id: int, reload: AppointmentCreate):
        appointment: Appointment  = appointmentHelpers.get_appointment_by_id(appointment_id)
        if not appointment:
            raise HTTPException(detail='appointment not found', status_code=404)
        
        patient_id: Patient = patients[reload.patient_id]
        doctor_id: Doctors = doctor[reload.doctor_id]

        appointment.date= reload.date
        return appointment
    
    @staticmethod
    def delete_appointment(appointment_id):
        appointment: Appointment  = appointmentHelpers.get_appointment_by_id(appointment_id)
        if not appointment:
            raise HTTPException(detail='appointment not found', status_code=404)
        del appointments[appointment_id]


