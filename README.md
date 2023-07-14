
# Attendance Management System (AMS)

This is an Attendance Management System (AMS) built using FastAPI. The system allows users to manage users, departments, courses, students, and attendance logs. It provides API endpoints to create, retrieve, update, and delete data related to these entities.



## Setup and Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your/repository.git
   ```

## Use Case: Managing Course Attendance
![Screenshot from 2023-07-14 16-51-49.png](..%2F..%2FPictures%2FScreenshots%2FScreenshot%20from%202023-07-14%2016-51-49.png)
![Screenshot from 2023-07-14 16-54-13.png](..%2F..%2FPictures%2FScreenshots%2FScreenshot%20from%202023-07-14%2016-54-13.png)
The AMS (Attendance Management System) provides a comprehensive solution for managing course attendance in educational institutions. With the AMS, administrators, instructors, and students can efficiently track and monitor attendance records, ensuring accurate attendance management and streamlined reporting.

To ensure data integrity and maintain proper relationships between the models, it is important to follow a specific order when populating data. Here's the recommended order to populate data in the given models:

1. Departments: Start by populating the `Departments` table since it serves as the parent table for the `Courses` table.

2. Courses: After populating the `Departments` table, proceed to populate the `Courses` table. The `department_id` column in the `Courses` table references the `id` column in the `Departments` table, establishing a foreign key relationship.

3. Users: Next, populate the `Users` table. The `submitted_by` column in both the `Departments` and `Courses` tables references the `Users` table. Therefore, it is necessary to have existing user entries before populating the other tables.

4. Students: Once the `Departments`, `Courses`, and `Users` tables are populated, you can proceed to populate the `Students` table. The `department_id` and `class_name` columns in the `Students` table reference the respective primary keys in the `Departments` and `Courses` tables.

5. AttendanceLog: Finally, populate the `AttendanceLog` table. The `student_id` and `course_id` columns in the `AttendanceLog` table reference the respective primary keys in the `Students` and `Courses` tables.

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database:

   The system uses a database to store the data. Make sure you have a supported database engine installed and running. Update the database connection details in the `ams/database.py` file.

   By default, the system is configured to use an SQLite database. If you want to use a different database engine, make the necessary changes in the database configuration.

4. Initialize the database schema:

   ```bash
   python main.py initialize_db
   ```

5. Start the server:

   ```bash
   python main.py
   ```

   The server will start running on `http://localhost:8000`.

## API Endpoints

The following API endpoints are available:

- `GET /` - Get the welcome message.

### Users

- `POST /users` - Create a new user.

### Departments

- `POST /departments` - Create a new department.

### Authentication

- `POST /login` - Authenticate a user and get an access token.

### Attendance Logs

- `POST /attendance-logs` - Create a new attendance log.

### Courses

- `POST /courses` - Create a new course.

### Students

- `POST /students` - Create a new student.

### Additional Endpoints

The system also provides the following additional endpoints:

- `GET /get_student_id` - Get the student ID based on the full name and class name.
- `GET /get_course_id` - Get the course ID based on the class name.

Refer to the API documentation for detailed information about the request and response formats of each endpoint.

## Authentication and Authorization

The system uses token-based authentication for secure access to the API endpoints. To access protected endpoints, include the access token in the `Authorization` header of the request.

For example:

```bash
curl -X GET "http://localhost:8000/protected-endpoint" \
     -H "Authorization: Bearer <access_token>"
```

To obtain an access token, use the `/login` endpoint with valid credentials.

## Development and Contributing

To contribute to the development of this project, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make the necessary changes and commit them.
4. Push the changes to your fork.
5. Submit a pull request.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.