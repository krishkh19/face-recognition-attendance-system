import sqlite3
import os
from datetime import datetime


class Database:
    def __init__(self):
        # Create database directory if it doesn't exist
        if not os.path.exists('data'):
            os.makedirs('data')

        self.conn = sqlite3.connect('data/attendance.db')
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()

        # Create users table
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS users
                       (
                           id
                           INTEGER
                           PRIMARY
                           KEY
                           AUTOINCREMENT,
                           name
                           TEXT
                           NOT
                           NULL,
                           enrollment
                           TEXT
                           UNIQUE
                           NOT
                           NULL,
                           college
                           TEXT
                           NOT
                           NULL,
                           class
                           TEXT
                           NOT
                           NULL,
                           section
                           TEXT
                           NOT
                           NULL,
                           face_template
                           BLOB
                           NOT
                           NULL,
                           registration_date
                           TEXT
                           DEFAULT
                           CURRENT_TIMESTAMP
                       )
                       ''')

        # Create attendance table
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS attendance
                       (
                           id
                           INTEGER
                           PRIMARY
                           KEY
                           AUTOINCREMENT,
                           user_id
                           INTEGER
                           NOT
                           NULL,
                           date
                           TEXT
                           NOT
                           NULL,
                           time
                           TEXT
                           NOT
                           NULL,
                           status
                           TEXT
                           DEFAULT
                           'Present',
                           FOREIGN
                           KEY
                       (
                           user_id
                       ) REFERENCES users
                       (
                           id
                       )
                           )
                       ''')

        self.conn.commit()

    def register_user(self, name, enrollment, college, class_, section, face_template):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                           INSERT INTO users (name, enrollment, college, class, section, face_template)
                           VALUES (?, ?, ?, ?, ?, ?)
                           ''', (name, enrollment, college, class_, section, face_template))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def verify_login(self, name, enrollment):
        cursor = self.conn.cursor()
        cursor.execute('''
                       SELECT id, face_template
                       FROM users
                       WHERE name = ?
                         AND enrollment = ?
                       ''', (name, enrollment))
        return cursor.fetchone()

    def get_user_info(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute('''
                       SELECT name, enrollment, college, class, section
                       FROM users
                       WHERE id = ?
                       ''', (user_id,))
        return cursor.fetchone()

    def mark_attendance(self, user_id, datetime_str):
        try:
            # Split datetime into date and time components
            dt = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
            date = dt.strftime("%Y-%m-%d")
            time = dt.strftime("%H:%M:%S")

            cursor = self.conn.cursor()

            # Check if attendance already marked for today
            cursor.execute('''
                           SELECT id
                           FROM attendance
                           WHERE user_id = ? AND date = ?
                           ''', (user_id, date))

            if cursor.fetchone():
                return False, "Attendance already marked for today"

            # Insert new attendance record
            cursor.execute('''
                           INSERT INTO attendance (user_id, date, time)
                           VALUES (?, ?, ?)
                           ''', (user_id, date, time))

            self.conn.commit()
            return True, "Attendance marked successfully"
        except Exception as e:
            return False, str(e)

    def get_attendance(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute('''
                       SELECT u.name,
                              u.enrollment,
                              u.college,
                              u.class,
                              u.section,
                              a.date,
                              a.time,
                              a.status
                       FROM attendance a
                                JOIN users u ON a.user_id = u.id
                       WHERE a.user_id = ?
                       ORDER BY a.date DESC, a.time DESC
                       ''', (user_id,))
        return cursor.fetchall()

    def close(self):
        self.conn.close()