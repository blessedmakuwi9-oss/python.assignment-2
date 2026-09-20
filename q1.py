import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect("school.db")

# Create a cursor
cursor = connection.cursor()

# Create the students table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

# Insert data into the table
cursor.execute("""
INSERT INTO students (name, age)
VALUES (?, ?)
""", ("John", 20))

cursor.execute("""
INSERT INTO students (name, age)
VALUES (?, ?)
""", ("Mary", 21))

# Save the changes
connection.commit()

# Retrieve data from the table
cursor.execute("SELECT * FROM students")

# Display the retrieved data
rows = cursor.fetchall()

for row in rows:
    print(row)

# Close the database connection
connection.close()
