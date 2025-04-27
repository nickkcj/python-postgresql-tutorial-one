from connection import conn, cur
# CRUD: Create, Read, Update, Delete

# Create
cur.execute("INSERT INTO posts (title, content) " \
            "VALUES ('My First Post', 'Creating a blog is fun!')")


# Read
cur.execute("SELECT * FROM posts WHERE title='My First Post'")
print(cur.fetchone())

# Update
cur.execute("UPDATE posts SET content='Creating a blog is awesome!' " \
            "WHERE title='My First Post'")

# Delete
cur.execute("DELETE FROM posts WHERE title='My First Post'")

conn.commit()



