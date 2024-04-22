from fastapi import APIRouter

from schema.appointment import AppointmentCreate, appointments
from schema.doctors import DoctorCreate, Doctors
from services.appointment  import AppointmentService
from routers.doctors import data
from datetime import datetime

appointment_router= APIRouter()

@appointment_router.post('', status_code=201)
def create_appointment(patient_id: int, doctor_id: int):
    for doctor in doctor:
        if doctor.id == doctor_id and doctor.is_available:
            appointment_id = len(appointments) + 1
            appointment = AppointmentCreate(id=appointment_id, patient_id=patient_id, doctor_id=doctor_id, date=str(datetime.now()))
            appointments.append(appointment)
            doctor.is_available = False
            return appointment
    raise HTTPException(status_code=400, detail="No available doctor found")

@appointment_router.put("/appointments/{appointment_id}/complete",)
def complete_appointment(appointment_id: int):
    for appointment in appointments:
        if appointment.id == appointment_id:
            # Remove appointment from the list
            appointments.remove(appointment)
            # Update doctor availability
            for doctor in doctor:
                if doctor.id == appointment.doctor_id:
                    doctor.is_available = True
            return appointment
    raise HTTPException(status_code=404, detail="Appointment not found", response_model= Appointment)


@appointment_router.put("/appointments/{appointment_id}/cancel",response_model= Appointment)
def cancel_appointment(appointment_id: int):
    for appointment in appointments:
        if appointment.id == appointment_id:
            # Remove appointment from the list
            appointments.remove(appointment)
            # Update doctor availability
            for doctor in doctor:
                if doctor.id == appointment.doctor_id:
                    doctor.is_available = True
            return appointment
    raise HTTPException(status_code=404, detail="Appointment not found")


@appointment_router.put("/doctors/{doctor_id}/set-availability/", response_model= Doctor)
def set_doctor_availability(doctor_id: int, is_available: bool):
    for doctor in doctor:
        if doctor.id == doctor_id:
            doctor.is_available = is_available
            return doctor
    raise HTTPException(status_code=404, detail="Doctor not found") 