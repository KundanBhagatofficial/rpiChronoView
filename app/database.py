import sqlite3

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS schedules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            task TEXT NOT NULL,
            details TEXT
        )
        """)
        self.connection.commit()

    def add_schedule(self, date, task, details):
        self.cursor.execute("INSERT INTO schedules (date, task, details) VALUES (?, ?, ?)", (date, task, details))
        self.connection.commit()

    def fetch_today_tasks(self, current_date):
        self.cursor.execute("SELECT * FROM schedules WHERE date = ?", (current_date,))
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()
