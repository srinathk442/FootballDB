from flask import Flask, render_template, request
import sqlite3

# Initialize Flask app
app = Flask(__name__, template_folder='templates')  # Specify the folder for templates

# Connect to SQLite database
def connect_db():
    return sqlite3.connect('Football1.db')  # Connect to the SQLite database

# Home page
@app.route('/')
def home():
    return '''
    <div style="text-align: center;">
        <h1>Welcome to the Football Data Page</h1>
        <p>Use the links below to explore:</p>
        <ul style="list-style-type: none;">
            <li><a href="/teams">Teams</a></li>
            <li><a href="/players">Players</a></li>
            <li><a href="/matches">Matches</a></li>
            <li><a href="/goals">Goals</a></li>
            <li><a href="/query">SQL Query</a></li>
        </ul>
    </div>
    '''

# Display all teams
@app.route('/teams')
def teams():
    conn = connect_db()  # Connect to the database
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM team")  # Get all records from 'team'
    teams = cursor.fetchall()  # Fetch all results
    conn.close()
    return render_template('teams.html', teams=teams)  # Render a template to display teams

# Display all players
@app.route('/players')
def players():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM player")
    players = cursor.fetchall()
    conn.close()
    return render_template('players.html', players=players)  # Render a template to display players

# Display all matches
@app.route('/matches')
def matches():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM matches")
    matches = cursor.fetchall()
    conn.close()
    return render_template('matches.html', matches=matches)

# Display all goals
@app.route('/goals')
def goals():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM goal")
    goals = cursor.fetchall()
    conn.close()
    return render_template('goals.html', goals=goals)  # Render a template to display goals

# Interactive SQL query form
@app.route('/query', methods=['GET', 'POST'])
def query():
    if request.method == 'POST':
        sql_query = request.form['sql_query']  # Get the SQL query from the form
        conn = connect_db()  # Connect to the database
        cursor = conn.cursor()
        try:
            cursor.execute(sql_query)  # Execute the query
            results = cursor.fetchall()  # Fetch all results
        except sqlite3.Error as e:
            results = [f"Error executing query: {e}"]  # Handle errors
        conn.close()  # Close the connection
        return render_template('query.html', results=results)  # Display query results

    # Render a form for user input
    return render_template('query_form.html')  # Form for SQL queries

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
