import psycopg2 as pg
connection = pg.connect(user="postgres",
                            password="postgres",
                            host="127.0.0.1",
                            port="5432",
                            database="finance_db")

cursor = connection.cursor()