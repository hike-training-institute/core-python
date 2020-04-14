import cx_Oracle as cx
import os
# connection = cx.connect(user = "SYSTEM",
#                         password = "sambit",
#                         host = 'localhost',
#                         port = "1521",
#                         SID = 'xe',
#                         database = "personal_details")
connection = cx.connect("SYSTEM", "sambit", "localhost/xe")
cursor = connection.cursor()
# result= cursor.execute("CREATE TABLE personal_details (Name varchar2(50) NOT NULL, Age number, Restaurant varchar2(50), Role varchar2(50), UserName varchar2(50), Password varchar2(50))")
# result= cursor.execute ("CREATE TABLE food_prices (restaurant varchar2(50), items varchar2(50) NOT NULL, price number(10) NOT NULL)")

# result = cursor.execute("Insert into personal_details (Name, Age, Restaurant, Role, UserName, Password) values ('sambit',24,'sambit_hotels','owner','sambit','sambit123')")

# result= cursor.execute("Select Age from personal_details where Name = 'sambit' ")
# print(result)
# all_rows = cursor.fetchall()

cursor.execute("SELECT * FROM personal_details ")
head_rows = cursor.fetchmany(2)
remaining_rows = cursor.fetchall()
print(remaining_rows)
print(head_rows)
for each_row in remaining_rows:
    print("---->", head_rows)
    for each_col in remaining_rows:
        print(each_col)
#
# import cx_Oracle
# import os
# import sys
#
# print(sys.version)
# # print(os.environ['ORACLE_HOME'])
# print(os.environ['path'])
#
# con = cx_Oracle.connect('SYSTEM/sambit@localhost:1521/xe')
# print (con.version)
#
# con.close()