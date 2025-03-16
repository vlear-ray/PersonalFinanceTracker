import sqlite3

def create_tables():
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            description TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recurring_transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            amount REAL NOT NULL,
            frequency TEXT NOT NULL, -- 'weekly', 'bi-weekly', 'monthly', etc.
            start_date TEXT NOT NULL,
            category TEXT
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()