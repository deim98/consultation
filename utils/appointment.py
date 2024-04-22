from schema.appointment import Appointment

class appointmentHelpers:

    @staticmethod
    def get_appointment_by_id(appointment_id: int):
        for appoint in appointments:
            if appointment.id == appointment_id:
                return appointment
        
        return None