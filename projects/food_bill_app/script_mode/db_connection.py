import psycopg2 as pg

def testuser(user, pwd):
    # connect() method creates a new database session and returns a connection object
    connection = pg.connect(user = "postgres",
                              password = "postgres",
                              host = "127.0.0.1",
                              port = "5433",
                              database = "postgres")
    cursor = connection.cursor()
    username = 'username'
    cursor.execute("Select * from personal_details where {} = '{}' and {} = '{}' ".format('username',user, 'password', pwd))
    data = cursor.fetchone()
    # if data[0] == 'sambit':
    #     print("beautiful")
    # print(data)
    if data :
        return data [4] , data[5], data[2]
    else :
        return None, None, None
# user = 'sambit'
# abc = testuser(user)
# print(abc)