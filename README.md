# Smart Attendance System - Face Recognition Based
### Overview
The Smart Attendance System is a Python application that uses face recognition technology to automate attendance tracking. It provides a user-friendly interface for registering users, taking attendance through face recognition, and viewing attendance records.

Features
User Registration: Capture and store user details along with facial templates

Face Recognition Login: Authenticate users using facial recognition

Attendance Marking: Automatically mark attendance when a registered face is recognized

Attendance Records: View and analyze attendance history with statistics

Responsive UI: Modern and intuitive graphical user interface

## Technologies Used
Python 3.x

OpenCV (for face detection and recognition)

Tkinter (for GUI)

PIL/Pillow (for image processing)

SQLite (for database storage)

NumPy (for numerical operations)

## Installation
Prerequisites
Python 3.6 or higher

pip package manager

# Usage
### Main Menu: 
Choose between "Login" or "Register New User"

### Registration:

Fill in user details (name, enrollment number, etc.)

Capture face image using webcam

Submit registration

### Login:

Enter name and enrollment number

System will verify using face recognition

### Dashboard:

Take attendance (face recognition based)

View attendance records and statistics

## Database Schema
The system uses SQLite database with the following tables:

### users: 
Stores user information and facial templates

### attendance:
Records attendance timestamps and status

### Contributing
Contributions are welcome! Please follow these steps:

Fork the repository

Create a new branch (git checkout -b feature-branch)


# Screenshots

![Screenshot (306)](https://github.com/user-attachments/assets/d3067c66-d9b6-40e0-97e2-5c4ef569ea67)

![Screenshot (308)](https://github.com/user-attachments/assets/3ae7b804-30fd-4b94-827c-f90f4c792fe8)


![Screenshot (309)](https://github.com/user-attachments/assets/06476f5f-51cc-403c-8109-c879cb96dd9a)


## Future Enhancements
Add multi-face detection for group attendance

Implement machine learning for improved face recognition

Add email/SMS notifications for attendance

Develop mobile companion app

Commit your changes (git commit -m 'Add new feature')

Push to the branch (git push origin feature-branch)

Create a new Pull Request
