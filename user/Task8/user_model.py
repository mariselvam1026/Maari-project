import psycopg2
from sqlalchemy.orm import query

con = psycopg2.connect(database="maridb", user="postgres", password="mari", host="127.0.0.1", port="5432")
print('con',con)
print("Database opened successfully")


def get_all_users(self):
    query = 'select * from final'
    