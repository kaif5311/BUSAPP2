import sqlite3

conn = sqlite3.connect('sql_app.db')
cursor = conn.cursor()

print("--- ALL ROUTES ---")
cursor.execute("SELECT * FROM routes;")
for row in cursor.fetchall():
    print(row)

print("\n--- ALL SCHEDULES ---")
cursor.execute("SELECT * FROM schedules;")
for row in cursor.fetchall():
    print(row)

conn.close()
