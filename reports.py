from openpyxl import Workbook
from openpyxl.styles import Font

from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle
)

from reportlab.lib import colors

def export_excel(records, filename):

    workbook = Workbook()

    worksheet = workbook.active

    worksheet.title = "Students"

    headings = [
        "ID",
        "Name",
        "Age",
        "Course",
        "Marks",
        "Attendance",
        "Photo"
    ]

    worksheet.append(headings)

    for cell in worksheet[1]:
        cell.font = Font(bold=True)

    for record in records:
        worksheet.append(record)

    workbook.save(filename)


def export_pdf(records, filename):

    pdf = SimpleDocTemplate(filename)

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

    for record in records:

        data.append([
            record[0],
            record[1],
            record[2],
            record[3],
            record[4],
            record[5]
        ])

    table = Table(data)

    table.setStyle(
        TableStyle([
            ("GRID",(0,0),(-1,-1),1,colors.black),
            ("BACKGROUND",(0,0),(-1,0),colors.grey),
            ("TEXTCOLOR",(0,0),(-1,0),colors.white)
        ])
    )

    pdf.build([table])

def calculate_grade(marks):

    if marks >= 80:
        return "A"

    elif marks >= 60:
        return "B"

    elif marks >= 40:
        return "C"

    else:
        return "F"
    
def create_report_card(student):

    return {
        "name": student[1],
        "age": student[2],
        "course": student[3],
        "marks": student[4],
        "attendance": student[5],
        "grade": calculate_grade(student[4])
    }