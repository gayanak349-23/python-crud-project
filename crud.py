import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="#gayana23",
    database="logindb1"
)

cursor = conn.cursor()

print("Connected successfully")

# READ
cursor.execute("SELECT * FROM students")
print("READ Operation:")
for row in cursor.fetchall():
    print(row)

# CREATE
sql = "INSERT INTO students VALUES (%s,%s,%s,%s,%s)"
val = (8, "Arun", 21, "BCA", None)
cursor.execute(sql, val)
conn.commit()
print("Inserted successfully")

# UPDATE
cursor.execute(
    "UPDATE students SET StudentAge=%s WHERE StudentID=%s",
    (22, 8)
)
conn.commit()
print("Updated successfully")

# DELETE
cursor.execute(
    "DELETE FROM students WHERE StudentID=%s",
    (8,)
)
conn.commit()
print("Deleted successfully")

# FINAL READ
cursor.execute("SELECT * FROM students")
print("Final Table:")
for row in cursor.fetchall():
    print(row)

