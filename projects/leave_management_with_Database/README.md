## Prerequisites:

You need a MySQL database server (5.0+) with root privileges.

```
sudo apt-get install mysql-server
```

You need to install a MySQL Python Connector 

```python
pip install pymysql
```

In case of using python 3+ then use:

```python
pip3 install pymysql
```



## SQL user setup:

Login the mysql shell as the root user.

```
sudo mysql -u root
```

Then run on mysql console to create test user with all permissions

```
GRANT ALL PRIVILEGES ON *.* TO 'test_user'@'localhost' IDENTIFIED BY 'test@123';
```



## Installation:

1. Download the repository 
2. Change directory to the repository
3. To Import the leave_management.sql to your local MySQL Database.

 Run from terminal

```
mysql -u test_user -p employees < leave_management.sql
```


