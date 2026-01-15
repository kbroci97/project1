import sqlite3

conn = sqlite3.connect('playoffTeams.db')

cursor = conn.cursor()

query = """
    INSERT INTO teams (city, name)
    VALUES ("Buffalo", "Bills"),
           ("Denver", "Broncos"),
           ("Houston", "Texans"),
           ("New England", "Patriots"),
           ("San Francisco", "49ers"),
           ("Seattle", "Seahawks"),
           ("Los Angeles", "Rams"),
           ("Chicago", "Bears");
"""

cursor.execute(query)
conn.commit()
conn.close()