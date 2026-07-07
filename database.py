import sqlite3

DATABASE_NAME = "student.db"


def create_database():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            course TEXT,
            marks REAL,
            attendance TEXT,
            photo TEXT
        )
    """)

    conn.commit()
    conn.close()

    print("✅ Database Created Successfully")


if __name__ == "__main__":
    create_database()