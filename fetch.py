import sqlite3

conn = sqlite3.connect('playoffTeams.db')

cursor = conn.cursor()

query = """
    SELECT * 
    FROM teams;
"""

cursor.execute(query)
results = cursor.fetchall()

conn.close()

print(results)