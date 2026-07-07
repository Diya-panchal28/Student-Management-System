# Student-Management-System
A Python-based Student Management System built with Tkinter and SQLite. It supports CRUD operations, student record management, dashboard analytics, search, PDF &amp; Excel export, charts, database backup &amp; restore, and light/dark theme support through a user-friendly desktop interface.
# 🎓 Student Management System

A modern **Student Management System** built with **Python**, **Tkinter**, and **SQLite** for efficiently managing student records through an intuitive desktop interface. The application enables users to perform complete CRUD operations, maintain student information, generate reports, visualize data with charts, manage database backups, and switch between light and dark themes.

## ✨ Features

* ➕ Add new student records
* ✏️ Update existing student information
* 🗑️ Delete student records
* 🔍 Search students by ID, name, course, or attendance
* 📋 Display all student records in a table
* 📊 Dashboard showing:

  * Total Students
  * Total Courses
  * Average Marks
  * Highest Marks
* 📈 Data visualization using Matplotlib:

  * Student Marks Chart
  * Students per Course
  * Attendance Distribution
  * Average Marks by Course
* 📄 Export student records to PDF
* 📊 Export student records to Excel
* 💾 Database Backup and Restore
* 🌙 Light/Dark Theme Support
* 🖼️ Student Photo Path Management
* 🗃️ SQLite database for data storage

## 🛠️ Technologies Used

* Python 3
* Tkinter
* SQLite
* Matplotlib
* OpenPyXL
* ReportLab

## 📂 Project Structure

```text
Student-Management-System/
│── main.py              # Application entry point
│── sm_ui.py             # User interface
│── crud.py              # Database CRUD operations
│── database.py          # Database creation
│── reports.py           # PDF & Excel reports
│── charts.py            # Data visualization
│── backup.py            # Database backup & restore
│── theme.py             # Light/Dark theme
│── student.db           # SQLite database (generated automatically)
```

## 🚀 How to Run

1. Clone the repository.
2. Install the required libraries:

```bash
pip install matplotlib openpyxl reportlab
```

3. Run the application:

```bash
python main.py
```

## 📊 Modules Included

* Student Registration
* Student Record Management
* Dashboard Analytics
* Search Functionality
* Excel Export
* PDF Export
* Charts & Statistics
* Database Backup & Restore
* Theme Switching

## 🎯 Learning Outcomes

This project demonstrates practical implementation of:

* GUI development with Tkinter
* SQLite database integration
* CRUD operations
* File handling
* Data visualization
* Report generation
* Desktop application development
* Modular Python programming

## 👨‍💻 Author

**Diya Panchal**

If you found this project helpful, consider giving the repository a ⭐.
