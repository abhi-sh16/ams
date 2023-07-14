from fastapi import FastAPI
from ams import models
from ams.database import engine
from ams.repository.intialize_users import startup_event
from ams.routers import authentication, attendance_log, courses, students
from ams.routers import users, departments
from ams.routers import courses

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# # routes
app.include_router(users.router)
app.include_router(departments.router)
app.include_router(authentication.router)
app.include_router(attendance_log.router)
app.include_router(courses.router)
app.include_router(students.router)


@app.on_event("startup")
async def startup():
    # Calling the startup_event function
    startup_event()


