# Football Database and Web Application

This project is a Flask-based web application that interacts with an SQLite database to store and display football-related data, including teams, players, matches, and goals. It also provides an interface for executing SQL queries on the database.

## Features
- **Database Initialization**: Creates and populates an SQLite database (`Football1.db`) with predefined football-related data.
- **Flask Web Interface**:
  - **Home Page**: Navigation links to different sections.
  - **Teams Page**: Displays all teams stored in the database.
  - **Players Page**: Displays all players stored in the database.
  - **Matches Page**: Displays all matches stored in the database.
  - **Goals Page**: Displays all goals stored in the database.
  - **SQL Query Interface**: Allows users to execute custom SQL queries.

## Installation
### Prerequisites
- Python 3.x
- Flask
- SQLite3

### Setup Instructions
1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Install dependencies:
   ```sh
   pip install flask
   ```
3. Initialize the database:
   ```sh
   python football_db.py
   ```
4. Run the Flask application:
   ```sh
   python app.py
   ```
5. Open a browser and visit:
   ```
   http://127.0.0.1:5000/
   ```

## Project Structure
```
/
├── app.py             # Flask application
├── football_db.py     # Database initialization script
├── templates/
│   ├── teams.html     # Displays team data
│   ├── players.html   # Displays player data
│   ├── matches.html   # Displays match data
│   ├── goals.html     # Displays goal data
│   ├── query.html     # Displays SQL query results
│   ├── query_form.html # Form for user SQL queries
└── README.md          # Project documentation
```

## Database Schema
### Tables
1. **Player Table (`player`)**
   - `pid` (Primary Key)
   - `name` (Text)
   - `position` (Text)
   - `age` (Integer)
2. **Team Table (`team`)**
   - `tid` (Primary Key)
   - `name` (Text)
   - `coach` (Text)
   - `founded` (Date)
   - `pid` (Foreign Key referencing `player.pid`)
3. **Matches Table (`matches`)**
   - `mid` (Primary Key)
   - `m_date` (Date)
   - `venue` (Text)
   - `result` (Text)
4. **Goal Table (`goal`)**
   - `gid` (Primary Key)
   - `pid` (Foreign Key referencing `player.pid`)
   - `mid` (Foreign Key referencing `matches.mid`)
   - `time` (Text)

## Usage
- Navigate through the web interface to explore teams, players, matches, and goals.
- Use the SQL query interface to execute custom database queries.


