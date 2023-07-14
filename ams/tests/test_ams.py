from fastapi.testclient import TestClient
from ams.main import app

client = TestClient(app)


def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "welcome!"}


def test_create_department():
    response = client.post(
        "/departments",
        json={"department_name": "Computer Science", "submitted_by": "admin"}
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Department created successfully", "department_id": 1}


def test_create_course():
    # Create a test department
    response_department = client.post(
        "/departments",
        json={"department_name": "Computer Science", "submitted_by": "admin"}
    )
    department_id = response_department.json()["department_id"]

    # Create a course
    response = client.post(
        "/courses",
        json={
            "course_name": "Introduction to Programming",
            "department_id": department_id,
            "semester": "Spring 2023",
            "class_name": "CS101",
            "lecture_hours": 3,
            "submitted_by": "admin"
        }
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Course created successfully", "course_id": 1}


# Students

def test_create_student():
    response = client.post(
        "/students",
        json={"full_name": "John Doe", "department_id": 1, "class_name": "CS101", "submitted_by": "admin"}
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Student created successfully", "student_id": 1}


# Attendance Logs

def test_create_attendance_log():
    response = client.post(
        "/attendance-logs",
        json={"student_id": 1, "course_id": 1, "present": True, "submitted_by": "admin"}
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Attendance log created successfully", "attendance_log_id": 1}


# Add more test cases for other endpoints

if __name__ == "__main__":
    import pytest

    pytest.main()
