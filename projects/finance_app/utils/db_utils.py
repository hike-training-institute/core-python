import psycopg2 as pg

# connect() method creates a
# new database session and returns a connection object
connection = pg.connect(user = "postgres",
                          password = "postgres",
                          host = "127.0.0.1",
                          port = "5432",
                          database = "dvdrental")

cursor = connection.cursor()