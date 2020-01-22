import pymysql
from db_test_connection import db


def login():
    username = input("Username:")
    password = input("Password:")
    authenticated = check_password(username, password)
    if authenticated:
        print("Hello, " + username + " " + password)
        menu_choice = show_menu()
        user_choice(menu_choice, authenticated)
    else:
        print("Wrong credentials")


def check_password(username, password):
    try:
        with db.cursor() as cursor:
            cursor.execute(
                "SELECT last_name, emp_no FROM employees WHERE first_name=%s",
                (username),
            )
            data = cursor.fetchone()
            emp_id = data[1]
            if password == data[0]:
                return emp_id
            else:
                return None
    except Exception as e:
        print("Error:" + str(e))


def show_menu():
    print("=================")
    print("Leave options")
    print("=================")
    print("1.Leaves utilized")
    print("2.Leaves yet to be used")
    print("3.Take Leave")
    menu_choice = int(input("Choose one menu:"))
    return menu_choice


def user_choice(menu_choice, emp_id):
    if menu_choice == 1:
        leaves_utilized(emp_id)
    elif menu_choice == 2:
        leaves_balance(emp_id)
    elif menu_choice == 3:
        take_leave(emp_id)
    else:
        print("Invalid choice")


def get_leaves_balance(emp_id):
    try:
        with db.cursor() as cursor:
            cursor.execute(
                "SELECT balance_leave FROM employees WHERE emp_no=%s", (emp_id)
            )
            data = cursor.fetchone()
            balance_leave = data[0]
            return balance_leave

    except Exception as e:
        print("Error:" + str(e))


def leaves_balance(emp_id):
    balance_leave = int(get_leaves_balance(emp_id))
    print(f"You have {balance_leave} leaves remaining")


def leaves_utilized(emp_id):
    balance_leave = int(get_leaves_balance(emp_id))
    if balance_leave <= 5:
        used_leaves = 5 - balance_leave
        print(f"You have used {used_leaves} leaves")
    else:
        print("Something's wrong")


def take_leave(emp_id):
    balance_leave = int(get_leaves_balance(emp_id))
    if balance_leave == 0:
        print("You dont have anymore leaves left")
    else:
        balance_leave -= 1
        updateStatement = "UPDATE employees SET balance_leave =%s WHERE emp_no=%s"
        val = (balance_leave, emp_id)
        db.cursor().execute(updateStatement, val)
        db.commit()
        leaves_balance(emp_id)


if __name__ == "__main__":
    login()
