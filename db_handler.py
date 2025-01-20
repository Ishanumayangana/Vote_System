import sqlite3

# Connect to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('data/votes.db')
    return conn

# Initialize the database (creating the votes table)
def init_db():
    conn = get_db_connection()
    conn.execute('CREATE TABLE IF NOT EXISTS votes (candidate TEXT, count INTEGER)')
    conn.commit()
    conn.close()

# Record a vote for a candidate
def record_vote(candidate):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM votes WHERE candidate=?', (candidate,))
    row = cursor.fetchone()
    
    if row:
        new_count = row[1] + 1
        cursor.execute('UPDATE votes SET count=? WHERE candidate=?', (new_count, candidate))
    else:
        cursor.execute('INSERT INTO votes (candidate, count) VALUES (?, ?)', (candidate, 1))
    
    conn.commit()
    conn.close()

# Get voting results
def get_results():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM votes')
    rows = cursor.fetchall()
    conn.close()
    
    # Convert the results to a list of dictionaries
    results = [{'Candidate': row[0], 'Votes': row[1]} for row in rows]
    return results
