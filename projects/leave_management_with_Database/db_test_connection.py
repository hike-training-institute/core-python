import pymysql

# DB configuration
hostname = "localhost"
username = "test_user"
password = "Test@123"
database = "employees"

# Open database connection
db = pymysql.connect(hostname, username, password, database)

# The below code part is more simple one by one statements -------
# prepare a cursor object using cursor() method
# cursor = db.cursor()

# execute SQL query using execute() method.
# cursor.execute("SELECT * FROM employees")

# fetch data from the database.
# data = cursor.fetchone()


# The below code part involves using the with statement ------
try:
    with db.cursor() as cursor:
        cursor.execute("SELECT * FROM employees limit 5;")
        data = cursor.fetchone()

    if data:
        print("The database connection is working")
    elif data is None:
        print("Check the database configurations and see if table isnt empty")

except Exception as e:
    print("Error:" + str(e))
