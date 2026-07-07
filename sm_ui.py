import tkinter as tk
from tkinter import ttk, filedialog, messagebox

import crud
import charts
import backup
import os

from theme import get_theme, toggle_theme


class StudentManagementUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1400x800")
        self.root.minsize(1200, 700)

        # Theme
        self.theme = get_theme()

        # Variables
        self.var_name = tk.StringVar()
        self.var_age = tk.StringVar()
        self.var_course = tk.StringVar()
        self.var_marks = tk.StringVar()
        self.var_attendance = tk.StringVar()
        self.var_photo = tk.StringVar()
        self.selected_student_id = None

        self.root.configure(bg=self.theme["window_bg"])

        self.create_header()
        self.create_main_frames()
        self.load_students()
        self.update_dashboard()

    # ==================================================
    # HEADER
    # ==================================================

    def create_header(self):

        self.header = tk.Frame(self.root, bg=self.theme["title_bg"], height=70)

        self.header.pack(fill="x")
        self.header.pack_propagate(False)

        title = tk.Label(
            self.header,
            text="🎓 STUDENT MANAGEMENT SYSTEM",
            bg=self.theme["title_bg"],
            fg=self.theme["title_fg"],
            font=("Segoe UI", 22, "bold"),
        )

        header_container = tk.Frame(self.header, bg=self.theme["title_bg"])

        header_container.pack(fill="both", expand=True)

        title = tk.Label(
            header_container,
            text="🎓 STUDENT MANAGEMENT SYSTEM",
            bg=self.theme["title_bg"],
            fg=self.theme["title_fg"],
            font=("Segoe UI", 22, "bold"),
        )

        title.pack(side="left", expand=True)

        tk.Button(
            header_container,
            text="🌙 Theme",
            font=("Segoe UI", 10, "bold"),
            command=self.change_theme,
        ).pack(side="right", padx=20)
        # ==================================================

    # DASHBOARD
    # ==================================================

    def create_dashboard(self):

        self.dashboard = tk.Frame(self.root, bg=self.theme["window_bg"], height=90)

        self.dashboard.pack(fill="x", padx=15, pady=(10, 0))

        # ---------- Card 1 ----------

        self.card_students = self.create_card(
            self.dashboard, "👨‍🎓 Total Students", "0"
        )

        self.card_students.pack(side="left", expand=True, fill="both", padx=5)

        # ---------- Card 2 ----------

        self.card_courses = self.create_card(self.dashboard, "📚 Courses", "0")

        self.card_courses.pack(side="left", expand=True, fill="both", padx=5)

        # ---------- Card 3 ----------

        self.card_average = self.create_card(self.dashboard, "📊 Average Marks", "0")

        self.card_average.pack(side="left", expand=True, fill="both", padx=5)

        # ---------- Card 4 ----------

        self.card_highest = self.create_card(self.dashboard, "🏆 Highest Marks", "0")

        self.card_highest.pack(side="left", expand=True, fill="both", padx=5)

        # ==================================================

    # DASHBOARD CARD
    # ==================================================

    def create_card(self, parent, title, value):

        frame = tk.Frame(parent, bg="white", bd=1, relief="solid")

        tk.Label(
            frame, text=title, bg="white", fg="#555555", font=("Segoe UI", 10, "bold")
        ).pack(pady=(12, 2))

        value_label = tk.Label(
            frame, text=value, bg="white", fg="#0D6EFD", font=("Segoe UI", 20, "bold")
        )

        value_label.pack()

        frame.value_label = value_label

        return frame

    # ==================================================
    # MAIN LAYOUT
    # ==================================================

    def create_main_frames(self):

        self.create_dashboard()

        self.container = tk.Frame(self.root, bg=self.theme["window_bg"])

        self.container.pack(fill="both", expand=True, padx=15, pady=15)

        # ---------------- LEFT PANEL ----------------

        self.left_frame = tk.Frame(
            self.container, bg=self.theme["frame_bg"], width=380, relief="ridge", bd=2
        )

        self.left_frame.pack(side="left", fill="y", padx=(0, 10))

        self.left_frame.pack_propagate(False)

        # ---------------- RIGHT PANEL ----------------

        self.right_frame = tk.Frame(
            self.container, bg=self.theme["frame_bg"], relief="ridge", bd=2
        )

        self.right_frame.pack(side="right", fill="both", expand=True)

        # ---------------- TITLES ----------------

        left_title = tk.Label(
            self.left_frame,
            text="Student Details",
            bg=self.theme["frame_bg"],
            fg=self.theme["text"],
            font=("Segoe UI", 16, "bold"),
        )

        left_title.pack(pady=15)

        right_title = tk.Label(
            self.right_frame,
            text="Student Records",
            bg=self.theme["frame_bg"],
            fg=self.theme["text"],
            font=("Segoe UI", 16, "bold"),
        )

        right_title.pack(pady=15)
        self.create_search_frame()
        self.create_table()

        self.create_student_form()
        self.create_action_buttons()

    # ==================================================
    # STUDENT FORM
    # ==================================================

    def create_student_form(self):

        form = tk.Frame(self.left_frame, bg=self.theme["frame_bg"])

        form.pack(fill="x", padx=20)
        # Name

        tk.Label(
            form,
            text="Student Name",
            bg=self.theme["frame_bg"],
            fg=self.theme["text"],
            font=("Segoe UI", 10, "bold"),
        ).pack(anchor="w", pady=(5, 3))

        tk.Entry(form, textvariable=self.var_name, font=("Segoe UI", 11)).pack(fill="x")

        # Age

        tk.Label(
            form,
            text="Age",
            bg=self.theme["frame_bg"],
            fg=self.theme["text"],
            font=("Segoe UI", 10, "bold"),
        ).pack(anchor="w", pady=(15, 3))

        tk.Entry(form, textvariable=self.var_age, font=("Segoe UI", 11)).pack(fill="x")

        # Course

        tk.Label(
            form,
            text="Course",
            bg=self.theme["frame_bg"],
            fg=self.theme["text"],
            font=("Segoe UI", 10, "bold"),
        ).pack(anchor="w", pady=(15, 3))

        self.course_box = ttk.Combobox(
            form, textvariable=self.var_course, state="readonly", font=("Segoe UI", 10)
        )

        self.course_box["values"] = (
            "Python",
            "Java",
            "C++",
            "Web Development",
            "Data Science",
            "AI",
        )

        self.course_box.pack(fill="x")

        # Marks

        tk.Label(
            form,
            text="Marks",
            bg=self.theme["frame_bg"],
            fg=self.theme["text"],
            font=("Segoe UI", 10, "bold"),
        ).pack(anchor="w", pady=(15, 3))

        tk.Entry(form, textvariable=self.var_marks, font=("Segoe UI", 11)).pack(
            fill="x"
        )

        # Attendance

        tk.Label(
            form,
            text="Attendance",
            bg=self.theme["frame_bg"],
            fg=self.theme["text"],
            font=("Segoe UI", 10, "bold"),
        ).pack(anchor="w", pady=(15, 3))

        self.attendance_box = ttk.Combobox(
            form,
            textvariable=self.var_attendance,
            state="readonly",
            font=("Segoe UI", 10),
        )

        self.attendance_box["values"] = ("Present", "Absent")

        self.attendance_box.pack(fill="x")

        # Photo

        tk.Label(
            form,
            text="Photo",
            bg=self.theme["frame_bg"],
            fg=self.theme["text"],
            font=("Segoe UI", 10, "bold"),
        ).pack(anchor="w", pady=(15, 3))

        photo_frame = tk.Frame(form, bg=self.theme["frame_bg"])

        photo_frame.pack(fill="x")

        tk.Entry(photo_frame, textvariable=self.var_photo, font=("Segoe UI", 10)).pack(
            side="left", fill="x", expand=True
        )

        tk.Button(photo_frame, text="Browse", command=self.browse_photo).pack(
            side="left", padx=5
        )

    # ==================================================
    # PHOTO
    # ==================================================

    def browse_photo(self):

        filename = filedialog.askopenfilename(
            title="Select Student Photo",
            filetypes=[("Image Files", "*.png *.jpg *.jpeg"), ("All Files", "*.*")],
        )

        if filename:
            self.var_photo.set(filename)

    # ==================================================
    # ACTION BUTTONS
    # ==================================================

    def create_action_buttons(self):

        button_frame = tk.Frame(self.left_frame, bg=self.theme["frame_bg"])

        button_frame.pack(fill="x", padx=20, pady=20)

        add_btn = tk.Button(
            button_frame,
            text="➕ Add",
            bg="#198754",
            fg="black",
            font=("Segoe UI", 10, "bold"),
            cursor="hand2",
            relief="flat",
            height=2,
            command=self.add_student,
        )

        add_btn.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        update_btn = tk.Button(
            button_frame,
            text="✏️ Update",
            bg="#0D6EFD",
            fg="black",
            font=("Segoe UI", 10, "bold"),
            cursor="hand2",
            relief="flat",
            height=2,
            command=self.update_student,
        )

        update_btn.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        delete_btn = tk.Button(
            button_frame,
            text="🗑 Delete",
            bg="#DC3545",
            fg="black",
            font=("Segoe UI", 10, "bold"),
            cursor="hand2",
            relief="flat",
            height=2,
            command=self.delete_student,
        )

        delete_btn.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        clear_btn = tk.Button(
            button_frame,
            text="🧹 Clear",
            bg="#6C757D",
            fg="black",
            font=("Segoe UI", 10, "bold"),
            cursor="hand2",
            relief="flat",
            height=2,
            command=self.clear_fields,
        )

        clear_btn.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        tk.Button(
            button_frame,
            text="💾 Backup",
            bg="#6F42C1",
            fg="black",
            font=("Segoe UI", 10, "bold"),
            cursor="hand2",
            relief="flat",
            height=2,
            command=self.backup_database,
        ).grid(row=2, column=0, padx=5, pady=5, sticky="ew")

        tk.Button(
            button_frame,
            text="📂 Restore",
            bg="#FD7E14",
            fg="black",
            font=("Segoe UI", 10, "bold"),
            cursor="hand2",
            relief="flat",
            height=2,
            command=self.restore_database,
        ).grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)

        # ==================================================
        # BUTTON FUNCTIONS (Temporary)
        # ==================================================

    def add_student(self):

        crud.add_student(
            self.var_name.get(),
            int(self.var_age.get()),
            self.var_course.get(),
            float(self.var_marks.get()),
            self.var_attendance.get(),
            self.var_photo.get(),
        )

        self.load_students()
        self.update_dashboard()
        self.clear_fields()

    def update_student(self):

        if self.selected_student_id is None:
            return

        crud.update_student(
            self.selected_student_id,
            self.var_name.get(),
            int(self.var_age.get()),
            self.var_course.get(),
            float(self.var_marks.get()),
            self.var_attendance.get(),
            self.var_photo.get(),
        )

        self.load_students()
        self.update_dashboard()
        self.clear_fields()

    def delete_student(self):

        if self.selected_student_id is None:
            messagebox.showwarning("Warning", "Please select a student first.")
            return

            confirm = messagebox.askyesno(
                "Confirm Delete", "Are you sure you want to delete this student?"
            )
        if confirm:
            crud.delete_student(self.selected_student_id)

            self.load_students()
            self.update_dashboard()
            self.clear_fields()

            messagebox.showinfo("Success", "Student deleted successfully.")

    def clear_fields(self):

        self.var_name.set("")
        self.var_age.set("")
        self.var_course.set("")
        self.var_marks.set("")
        self.var_attendance.set("")
        self.var_photo.set("")
        self.selected_student_id = None

        # ==================================================

    # SEARCH PANEL
    # ==================================================

    def create_search_frame(self):

        self.var_search = tk.StringVar()

        search_frame = tk.Frame(self.right_frame, bg=self.theme["frame_bg"])

        search_frame.pack(fill="x", padx=15, pady=10)

        tk.Label(
            search_frame,
            text="Search Student",
            bg=self.theme["frame_bg"],
            fg=self.theme["text"],
            font=("Segoe UI", 11, "bold"),
        ).pack(side="left", padx=(0, 10))

        tk.Entry(
            search_frame, textvariable=self.var_search, font=("Segoe UI", 11), width=30
        ).pack(side="left", padx=5)

        tk.Button(
            search_frame,
            text="🔍 Search",
            width=10,
            font=("Segoe UI", 10, "bold"),
            command=self.search_student,
        ).pack(side="left", padx=4)

        tk.Button(
            search_frame,
            text="📋 Show All",
            width=7,
            font=("Segoe UI", 10, "bold"),
            command=self.show_all_students,
        ).pack(side="left", padx=4)

        tk.Button(
            search_frame,
            text="📊 Excel",
            width=7,
            font=("Segoe UI", 10, "bold"),
            command=self.export_excel,
        ).pack(side="left", padx=4)

        tk.Button(
            search_frame,
            text="📄 PDF",
            width=7,
            font=("Segoe UI", 10, "bold"),
            command=self.export_pdf,
        ).pack(side="left", padx=4)

        tk.Button(
            search_frame,
            text="📈 Charts",
            width=7,
            font=("Segoe UI", 10, "bold"),
            command=self.open_chart_window,
        ).pack(side="left", padx=4)

    # ==================================================
    # SEARCH BUTTON FUNCTIONS (Temporary)
    # ==================================================

    def search_student(self):
        print("Search Clicked")

    def show_all_students(self):
        self.load_students()

    # ==================================================
    # STUDENT RECORD TABLE
    ## ==================================================

    def create_table(self):

        table_frame = tk.Frame(self.right_frame, bg=self.theme["frame_bg"])

        table_frame.pack(fill="both", expand=True, padx=15, pady=(5, 15))

        # Scrollbars
        scroll_y = tk.Scrollbar(table_frame, orient="vertical")
        scroll_x = tk.Scrollbar(table_frame, orient="horizontal")

        # Treeview
        self.student_table = ttk.Treeview(
            table_frame,
            columns=("ID", "Name", "Age", "Course", "Marks", "Attendance", "Photo"),
            show="headings",
            yscrollcommand=scroll_y.set,
            xscrollcommand=scroll_x.set,
        )

        scroll_y.config(command=self.student_table.yview)
        scroll_x.config(command=self.student_table.xview)

        scroll_y.pack(side="right", fill="y")
        scroll_x.pack(side="bottom", fill="x")

        self.student_table.pack(fill="both", expand=True)

        # Headings
        self.student_table.heading("ID", text="ID")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Age", text="Age")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Marks", text="Marks")
        self.student_table.heading("Attendance", text="Attendance")
        self.student_table.heading("Photo", text="Photo")

        # Column Widths
        self.student_table.column("ID", width=60, anchor="center")
        self.student_table.column("Name", width=180)
        self.student_table.column("Age", width=70, anchor="center")
        self.student_table.column("Course", width=150)
        self.student_table.column("Marks", width=80, anchor="center")
        self.student_table.column("Attendance", width=120, anchor="center")
        self.student_table.column("Photo", width=300)
        self.student_table.bind("<<TreeviewSelect>>", self.get_selected_row)

    # ==================================================
    # LOAD STUDENTS
    # ==================================================

    def load_students(self):

        records = crud.get_all_students()

        self.student_table.delete(*self.student_table.get_children())

        for row in records:
            self.student_table.insert("", "end", values=row)

        # ==================================================

    # UPDATE DASHBOARD
    # ==================================================

    def update_dashboard(self):

        total_students, total_courses, avg_marks, highest_marks = (
            crud.get_dashboard_stats()
        )

        self.card_students.value_label.config(text=str(total_students))
        self.card_courses.value_label.config(text=str(total_courses))
        self.card_average.value_label.config(text=str(avg_marks))
        self.card_highest.value_label.config(text=str(highest_marks))

    # ==================================================
    # GET SELECTED ROW
    # ==================================================

    def get_selected_row(self, event):

        selected = self.student_table.focus()

        if not selected:
            return

        values = self.student_table.item(selected, "values")

        if not values:
            return

        self.selected_student_id = values[0]

        self.var_name.set(values[1])
        self.var_age.set(values[2])
        self.var_course.set(values[3])
        self.var_marks.set(values[4])
        self.var_attendance.set(values[5])
        self.var_photo.set(values[6])

        # ==================================================

    # EXPORT TO EXCEL
    # ==================================================

    def export_excel(self):

        filename = filedialog.asksaveasfilename(
            defaultextension=".xlsx", filetypes=[("Excel File", "*.xlsx")]
        )

        if filename:

            crud.export_to_excel(filename)

            messagebox.showinfo("Success", "Excel file exported successfully.")

    # ==================================================
    # EXPORT TO PDF
    # ==================================================

    def export_pdf(self):

        filename = filedialog.asksaveasfilename(
            defaultextension=".pdf", filetypes=[("PDF File", "*.pdf")]
        )

        if filename:

            crud.export_to_pdf(filename)

            messagebox.showinfo("Success", "PDF file exported successfully.")

        # ==================================================

    # CHART WINDOW
    # ==================================================

    def open_chart_window(self):

        chart_window = tk.Toplevel(self.root)

        chart_window.title("Charts")

        chart_window.geometry("320x300")

        chart_window.resizable(False, False)

        tk.Label(chart_window, text="Select Chart", font=("Segoe UI", 16, "bold")).pack(
            pady=20
        )

        tk.Button(
            chart_window,
            text="📊 Student Marks",
            width=25,
            command=self.show_marks_chart,
        ).pack(pady=8)

        tk.Button(
            chart_window,
            text="📚 Students per Course",
            width=25,
            command=self.show_course_chart,
        ).pack(pady=8)

        tk.Button(
            chart_window,
            text="🥧 Attendance Chart",
            width=25,
            command=self.show_attendance_chart,
        ).pack(pady=8)

        tk.Button(
            chart_window,
            text="📈 Average Marks",
            width=25,
            command=self.show_average_chart,
        ).pack(pady=8)

    def show_marks_chart(self):

        records = crud.get_all_students()

        charts.show_marks_chart(records)

    def show_course_chart(self):

        records = crud.get_all_students()

        charts.show_course_statistics(records)

    def show_attendance_chart(self):

        records = crud.get_all_students()

        charts.show_attendance_chart(records)

    def show_average_chart(self):

        records = crud.get_all_students()

        charts.show_average_marks_by_course(records)

    def backup_database(self):

        filename = filedialog.asksaveasfilename(
            title="Save Database Backup",
            defaultextension=".db",
            filetypes=[("Database Files", "*.db")],
        )

        if filename:

            backup.backup_database("student.db", filename)

            messagebox.showinfo("Success", "Database backup created successfully.")

    def restore_database(self):

        filename = filedialog.askopenfilename(
            title="Select Backup File", filetypes=[("Database Files", "*.db")]
        )

        if filename:

            backup.restore_database(filename, "student.db")

            self.load_students()

            self.update_dashboard()

            messagebox.showinfo("Success", "Database restored successfully.")

        # ==================================================

    # THEME
    # ==================================================

    def change_theme(self):

        toggle_theme()

        messagebox.showinfo(
            "Theme",
            "Theme changed successfully.\nPlease restart the application to see the changes.",
        )
