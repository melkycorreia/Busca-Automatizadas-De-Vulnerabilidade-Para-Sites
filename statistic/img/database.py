import sqlite3

def create_table():
    conn = sqlite3.connect('results.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS results
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  url TEXT,
                  seo INTEGER,
                  vulnerability INTEGER,
                  storage INTEGER,
                  spam INTEGER,
                  traffic INTEGER)''')
    conn.commit()
    conn.close()

def add_result(url, seo, vulnerability, storage, spam, traffic):
    conn = sqlite3.connect('results.db')
    c = conn.cursor()
    c.execute('''INSERT INTO results (url, seo, vulnerability, storage, spam, traffic)
                 VALUES (?, ?, ?, ?, ?, ?)''', (url, seo, vulnerability, storage, spam, traffic))
    conn.commit()
    conn.close()

def get_all_results():
    conn = sqlite3.connect('results.db')
    c = conn.cursor()
    c.execute('SELECT * FROM results')
    results = c.fetchall()
    conn.close()
    return results

def get_result_by_id(result_id):
    conn = sqlite3.connect('results.db')
    c = conn.cursor()
    c.execute('SELECT * FROM results WHERE id = ?', (result_id,))
    result = c.fetchone()
    conn.close()
    return result
