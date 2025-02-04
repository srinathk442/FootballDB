import sqlite3

conn = sqlite3.connect('Football1.db')  # Connect to SQLite
cursor = conn.cursor()

# Create tables
cursor.execute('''CREATE TABLE IF NOT EXISTS player (
                    pid INT PRIMARY KEY,
                    name CHAR(50),
                    position VARCHAR(20),
                    age INT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS team (
                    tid INT PRIMARY KEY,
                    name VARCHAR(30),
                    coach CHAR(50),
                    founded DATE,
                    pid INT,
                    FOREIGN KEY (pid) REFERENCES player(pid))''')

cursor.execute('''CREATE TABLE IF NOT EXISTS matches (
                    mid INT PRIMARY KEY,
                    m_date DATE,
                    venue VARCHAR(30),
                    result VARCHAR(20))''')

cursor.execute('''CREATE TABLE IF NOT EXISTS goal (
                    gid INT PRIMARY KEY,
                    pid INT,
                    mid INT,
                    time CHAR(20),
                    FOREIGN KEY (pid) REFERENCES player(pid),
                    FOREIGN KEY (mid) REFERENCES matches(mid))''')

# Insert data into player table
player_data = [
    (1, 'Lionel Messi', 'Wide Forward', 34),
    (2, 'Florian Wirtz', 'Attacking Mid', 20),
    (3, 'Cristiano Ronaldo', 'Centre Forward', 38),
    (4, 'Virgil Van Dijk', 'Defender', 32),
    (5, 'Dominik Szoboszlai', 'Inverted Winger', 22)
]
cursor.executemany("INSERT INTO player (pid, name, position, age) VALUES (?, ?, ?, ?)", player_data)

# Insert data into matches table
matches_data = [
    (1, '2024-03-10', 'Anfield', '1-1'),
    (2, '2023-08-21', 'Bernabeu', '4-1'),
    (3, '2015-09-17', 'Allianz Stadium', '2-4')
]
cursor.executemany("INSERT INTO matches (mid, m_date, venue, result) VALUES (?, ?, ?, ?)", matches_data)

# Insert data into goal table
goal_data = [
    (1, 5, 1, '64'),
    (2, 2, 2, '78'),
    (3, 1, 2, '69'),
    (4, 3, 2, '52'),
    (5, 2, 3, '88'),
    (6, 2, 3, '85')
]
cursor.executemany("INSERT INTO goal (gid, pid, mid, time) VALUES (?, ?, ?, ?)", goal_data)

# Insert data into team table
team_data = [
    (1, 'Liverpool', 'Jurgen Klopp', '1988-05-13', 1),
    (2, 'Paris Saint Germain', 'Luis Enrique', '2016-01-21', 2),
    (3, 'Real Madrid', 'Carlo Ancelotti', '1975-06-26', 3),
    (4, 'Bayer Leverkusen 04', 'Xabi Alonso', '2001-12-23', 4)
]
existing_tids = set()
for tid, name, coach, founded, pid in team_data:
    if tid not in existing_tids:
        cursor.execute("INSERT INTO team (tid, name, coach, founded, pid) VALUES (?, ?, ?, ?, ?)", 
                       (tid, name, coach, founded, pid))
        existing_tids.add(tid)

# Commit the changes
conn.commit()

# Close the connection
conn.close()
