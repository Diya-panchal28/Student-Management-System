import tkinter as tk

from database import create_database
from sm_ui import StudentManagementUI


def main():
    # Create database if it doesn't exist
    create_database()

    # Create main window
    root = tk.Tk()

    # Start application
    StudentManagementUI(root)

    root.mainloop()


if __name__ == "__main__":
    main()