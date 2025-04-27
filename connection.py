import psycopg2

try:
    # Connect to the blog database directly
    conn = psycopg2.connect(
        dbname="blog",
        user="postgres",
        password="password",
        host="localhost",
    )
    print("Connected to existing blog database")
except psycopg2.OperationalError:
    # If blog database doesn't exist, create it
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="password",
        host="localhost",
    )
    conn.autocommit = True
    cur = conn.cursor()
    
    # Creating the Database
    cur.execute("CREATE DATABASE blog")
    print("Created new blog database")
    cur.close()
    conn.close()
    
    # Connect to the newly created blog
    conn = psycopg2.connect(
        dbname="blog",
        user="postgres",
        password="password",
        host="localhost",
    )

cur = conn.cursor()

# Creating the tables
cur.execute("""
    CREATE TABLE IF NOT EXISTS posts (
        id SERIAL PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        content TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL,
        email VARCHAR(100) NOT NULL UNIQUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

conn.commit()



