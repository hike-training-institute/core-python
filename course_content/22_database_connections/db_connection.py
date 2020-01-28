import psycopg2 as pg

# connect() method creates a
# new database session and returns a connection object
connection = pg.connect(user = "postgres",
                          password = "postgres",
                          host = "127.0.0.1",
                          port = "5432",
                          database = "temp1")

# cursor() is used to traverse the records from the result set.
cursor = connection.cursor()

# execute() is used to run sql query
cursor.execute("select * from emp_details;")

# fetchall() - to get all values in list
all_rows = cursor.fetchall()

print(all_rows)


def function_1():
    # scraping the data from online
    return ('varun', 1234, 'IT employee', 23)

for records in function_1():
    cursor.execute("insert into emp_details values {}".format(function_1()))
    connection.commit()