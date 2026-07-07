import matplotlib.pyplot as plt


def show_marks_chart(records):
    """
    Display a bar chart of student marks.
    """

    if not records:
        return

    names = []
    marks = []

    for record in records:
        names.append(record[1])
        marks.append(record[4])

    plt.figure(figsize=(8, 5))

    plt.bar(names, marks)

    plt.title("Student Marks")

    plt.xlabel("Students")

    plt.ylabel("Marks")

    plt.ylim(0, 100)

    plt.tight_layout()

    plt.show()


def show_course_statistics(records):
    """
    Display number of students in each course.
    """

    if not records:
        return

    course_count = {}

    for record in records:

        course = record[3]

        if course in course_count:
            course_count[course] += 1
        else:
            course_count[course] = 1

    plt.figure(figsize=(7, 5))

    plt.bar(course_count.keys(), course_count.values())

    plt.title("Students per Course")

    plt.xlabel("Course")

    plt.ylabel("Number of Students")

    plt.tight_layout()

    plt.show()


def show_attendance_chart(records):
    """
    Display attendance distribution.
    """

    if not records:
        return

    present = 0
    absent = 0

    for record in records:

        if record[5] == "Present":
            present += 1
        else:
            absent += 1

    plt.figure(figsize=(6, 6))

    plt.pie([present, absent], labels=["Present", "Absent"], autopct="%1.1f%%")

    plt.title("Attendance Distribution")

    plt.show()


def show_average_marks_by_course(records):
    """
    Display average marks for each course.
    """

    if not records:
        return

    course_data = {}

    for record in records:

        course = record[3]
        marks = record[4]

        if course not in course_data:
            course_data[course] = []

        course_data[course].append(marks)

    courses = []
    averages = []

    for course, marks_list in course_data.items():
        courses.append(course)
        averages.append(sum(marks_list) / len(marks_list))

    plt.figure(figsize=(8, 5))

    plt.bar(courses, averages)

    plt.title("Average Marks by Course")

    plt.xlabel("Course")

    plt.ylabel("Average Marks")

    plt.ylim(0, 100)

    plt.tight_layout()

    plt.show()
