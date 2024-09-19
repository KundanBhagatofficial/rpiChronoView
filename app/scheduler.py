from app.database import Database
from datetime import datetime

class Scheduler:
    def __init__(self):
        self.db = Database('database.db')
        self.db.create_tables()

    def get_current_time(self):
        now = datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")

    def add_schedule(self, date, task, details):
        self.db.add_schedule(date, task, details)

    def get_today_tasks(self):
        current_date = datetime.now().strftime("%Y-%m-%d")
        return self.db.fetch_today_tasks(current_date)
