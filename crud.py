import sqlite3
from openpyxl import Workbook
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
import shutil

DATABASE_NAME = "student.db"


# ==========================
# CONNECT DATABASE
# ==========================

def connect_db():
    return sqlite3.connect(DATABASE_NAME)


# ==========================
# ADD STUDENT
# ==========================

def add_student(name, age, course, marks, attendance, photo):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO students
        (name, age, course, marks, attendance, photo)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        name,
        age,
        course,
        marks,
        attendance,
        photo
    ))

    conn.commit()
    conn.close()


# ==========================
# GET ALL STUDENTS
# ==========================

def get_all_students():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            name,
            age,
            course,
            marks,
            attendance,
            photo
        FROM students
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


# ==========================
# UPDATE STUDENT
# ==========================

def update_student(student_id, name, age, course, marks, attendance, photo):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE students
        SET
            name=?,
            age=?,
            course=?,
            marks=?,
            attendance=?,
            photo=?
        WHERE id=?
    """, (
        name,
        age,
        course,
        marks,
        attendance,
        photo,
        student_id
    ))

    conn.commit()
    conn.close()


# ==========================
# DELETE STUDENT
# ==========================

def delete_student(student_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (student_id,)
    )

    conn.commit()
    conn.close()


# ==========================
# SEARCH STUDENTS
# ==========================

def search_students(keyword):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            name,
            age,
            course,
            marks,
            attendance,
            photo
        FROM students
        WHERE
            CAST(id AS TEXT) LIKE ?
            OR name LIKE ?
            OR course LIKE ?
            OR attendance LIKE ?
    """, (
        f"%{keyword}%",
        f"%{keyword}%",
        f"%{keyword}%",
        f"%{keyword}%"
    ))

    rows = cursor.fetchall()

    conn.close()

    return rows


# ==========================
# DASHBOARD STATISTICS
# ==========================

def get_dashboard_stats():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM students")
    total_students = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(DISTINCT course) FROM students")
    total_courses = cursor.fetchone()[0]

    cursor.execute("SELECT AVG(marks) FROM students")
    avg_marks = cursor.fetchone()[0]

    if avg_marks is None:
        avg_marks = 0

    cursor.execute("SELECT MAX(marks) FROM students")
    highest_marks = cursor.fetchone()[0]

    if highest_marks is None:
        highest_marks = 0

    conn.close()

    return (
        total_students,
        total_courses,
        round(avg_marks, 2),
        highest_marks
    )


# ==========================
# EXPORT TO EXCEL
# ==========================

def export_to_excel(filename):

    students = get_all_students()

    workbook = Workbook()

    sheet = workbook.active
    sheet.title = "Students"

    sheet.append([
        "ID",
        "Name",
        "Age",
        "Course",
        "Marks",
        "Attendance",
        "Photo"
    ])

    for student in students:
        sheet.append(student)

    workbook.save(filename)
    
# ==========================
# EXPORT TO PDF
# ==========================

def export_to_pdf(filename):

    students = get_all_students()

    pdf = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph("<b>Student Management System Report</b>", styles["Title"])
    elements.append(title)

    data = [
        [
            "ID",
            "Name",
            "Age",
            "Course",
            "Marks",
            "Attendance"
        ]
    ]

    for student in students:

        data.append([
            student[0],
            student[1],
            student[2],
            student[3],
            student[4],
            student[5]
        ])

    table = Table(data)

    table.setStyle(TableStyle([

        ("BACKGROUND", (0,0), (-1,0), colors.darkblue),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),

        ("GRID", (0,0), (-1,-1), 1, colors.black),

        ("BACKGROUND", (0,1), (-1,-1), colors.beige),

        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),

        ("ALIGN", (0,0), (-1,-1), "CENTER"),

        ("BOTTOMPADDING", (0,0), (-1,0), 10),

    ]))

    elements.append(table)

    pdf.build(elements)
# ==========================
# BACKUP DATABASE
# ==========================

def backup_database(destination):

    shutil.copyfile(DATABASE_NAME, destination)


# ==========================
# RESTORE DATABASE
# ==========================

def restore_database(source):

    shutil.copyfile(source, DATABASE_NAME)