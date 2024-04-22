from fastapi import FastAPI
from routers.doctors import doctor_router
from routers.patients import patient_router
from routers.appointment import appointment_router


app = FastAPI()

app.include_router(patient_router, prefix="/patients", tags=["patients"])
app.include_router(doctor_router, prefix="/doctors", tags=["doctors"])
app.include_router(appointment_router, prefix="/appointments", tags=["appointments"])

@app.get('/home')
def index():
    return "welcome to health is wealth"
