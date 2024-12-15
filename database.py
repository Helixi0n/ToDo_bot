import sqlite3


def init_db():
    connection = sqlite3.connect("data.db")
    cursor = connection.execute(
        """
	CREATE TABLE IF NOT EXISTS tasks (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		user_id INTEGER NOT NULL,
		task_text TEXT NOT NULL,
		status BOOLEAN DEFAULT 0
        )
	"""
    )
    connection.commit()
    connection.close()


def get_connection():
    return sqlite3.connect("data.db")
