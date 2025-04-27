from faker import Faker
import random
from connection import cur, conn

fake = Faker()

def create_users(n=10):
    for _ in range(n):
        cur.execute(
            """
            INSERT INTO users (username, password, email)
            VALUES (%s, %s, %s)
            """,
            (fake.user_name(), fake.password(), fake.email())
        )

create_users(10)


def create_posts(n=10):
    for _ in range(n):
        cur.execute(
            """
            INSERT INTO posts (title, content)
            VALUES (%s, %s)
            """,
            (fake.sentence(), fake.text())
        )

create_posts(10)

conn.commit()