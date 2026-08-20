import sqlite3

def init_db():
    # Connect to the db (create a file 'shortener.db' if not exists)
    conn = sqlite3.connect("shortener.db")
    cursor = conn.cursor()

    # Create the table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_url TEXT NOT NULL,
            short_hash TEXT UNIQUE
        )
    """)

    # Save changes and finish the connection
    conn.commit()
    conn.close()
    print("🗄️ Database init successfull!")

# Execution the function when run this file
if __name__ == "__main__":
    init_db()