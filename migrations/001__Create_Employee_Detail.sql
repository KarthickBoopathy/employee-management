CREATE TABLE IF NOT EXISTS employee_details (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	email TEXT NOT NULL UNIQUE,
	experience INTEGER NOT NULL,
	designation TEXT NOT NULL
)