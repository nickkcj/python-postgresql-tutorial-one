import pandas as pd
from connection import conn

pd.set_option('display.max_columns', None)  # Show all columns

users_df = pd.read_sql_query("SELECT * FROM users", conn)
posts_df = pd.read_sql_query("SELECT * FROM posts", conn)

print(users_df.head())
print(posts_df.head())