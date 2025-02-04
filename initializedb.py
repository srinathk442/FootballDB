import sqlite3

# Initialize database
# Function to create tables and insert data into the SQLite database
def initialize_db():
    conn = sqlite3.connect('Football1.db')  # Connect to SQLite
    cursor = conn.cursor()  # Create a cursor for executing SQL statements

    # Drop tables if they already exist to clear the database
    cursor.execute('DROP TABLE IF EXISTS player')
    cursor.execute('DROP TABLE IF EXISTS team')
    cursor.execute('DROP TABLE IF EXISTS matches')
    cursor.execute('DROP TABLE IF EXISTS goal')

    # Create tables if they don't already exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS player (
            pid INTEGER PRIMARY KEY,
            name TEXT,
            position TEXT,
            age INTEGER
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS team (
            tid INTEGER PRIMARY KEY,
            name TEXT,
            coach TEXT,
            founded DATE,
            pid INTEGER,
            FOREIGN KEY (pid) REFERENCES player(pid)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS matches (
            mid INTEGER PRIMARY KEY,
            m_date DATE,
            venue TEXT,
            result TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS goal (
            gid INTEGER PRIMARY KEY,
            pid INTEGER,
            mid INTEGER,
            time TEXT,
            FOREIGN KEY (pid) REFERENCES player(pid),
            FOREIGN KEY (mid) REFERENCES matches(mid)
        )
    ''')

    # Insert data into the "player" table with error handling
    player_data = [
        (1, 'Lionel Messi', 'Wide Forward', 34),
        (2, 'Florian Wirtz', 'Attacking Mid', 20),
        (3, 'Cristiano Ronaldo', 'Centre Forward', 38),
        (4, 'Virgil Van Dijk', 'Defender', 32),
        (5, 'Dominik Szoboszlai', 'Inverted Winger', 22)
    ]
    try:
        cursor.executemany("INSERT INTO player (pid, name, position, age) VALUES (?, ?, ?, ?)", player_data)
    except sqlite3.IntegrityError as e:
        print("Error inserting into 'player':", e)

    # Insert data into the "matches" table
    matches_data = [
        (1, '2024-03-10', 'Anfield', '1-1'),
        (2, '2023-08-21', 'Bernabeu', '4-1'),
        (3, '2015-09-17', 'Allianz Stadium', '2-4')
    ]
    try:
        cursor.executemany("INSERT INTO matches (mid, m_date, venue, result) VALUES (?, ?, ?, ?)", matches_data)
    except sqlite3.IntegrityError as e:
        print("Error inserting into 'matches':", e)

    # Insert data into the "goal" table
    goal_data = [
        (1, 5, 1, '64'),
        (2, 2, 2, '78'),
        (3, 1, 2, '69'),
        (4, 3, 2, '52'),
        (5, 2, 3, '88'),
        (6, 2, 3, '85')
    ]
    try:
        cursor.executemany("INSERT INTO goal (gid, pid, mid, time) VALUES (?, ?, ?, ?)", goal_data)
    except sqlite3.IntegrityError as e:
        print("Error inserting into 'goal':", e)

    # Insert data into the "team" table
    team_data = [
        (1, 'Liverpool', 'Jurgen Klopp', '1988-05-13', 1),
        (2, 'Paris Saint Germain', 'Luis Enrique', '2016-01-21', 2),
        (3, 'Real Madrid', 'Carlo Ancelotti', '1975-06-26', 3),
        (4, 'Bayer Leverkusen 04', 'Xabi Alonso', '2001-12-23', 4)
    ]
    existing_tids = set()  # Keep track of inserted `tid`s to avoid duplicates
    for tid, name, coach, founded, pid in team_data:
        if tid not in existing_tids:
            try:
                cursor.execute("INSERT INTO team (tid, name, coach, founded, pid) VALUES (?, ?, ?, ?, ?)", 
                               (tid, name, coach, founded, pid))
                existing_tids.add(tid)  # Add `tid` to avoid duplicates
            except sqlite3.IntegrityError as e:
                print("Error inserting into 'team':", e)

    # Commit the changes to make them permanent
    conn.commit()

    # Close the database connection
    conn.close()

# Run the function to initialize the database
initialize_db()
