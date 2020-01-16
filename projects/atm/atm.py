"""

This script is a Skeleton for replicating ATM machine Basic Functionalites
Completing this script shall give a Strong Understanding of Python Programming

"""

from openpyxl import load_workbook

user_options  = {1 : 'check_balance',
                  2 : 'withdraw_amount',
                  3 : 'deposit_amount'}




def choose_option():
    """
    # TODO : Show user_options to User and receive 1 input from user
    :return: user input
    """
    pass

def load_excel(read_only = True):
    """
    function to read excel sheet line by line
    :return:
    """
    wb = load_workbook('bank_accounts.xlsx', read_only=read_only )
    sheet = wb.active
    return sheet


def validate_user():
    """
    Validate the Username and Password using data from Excel Sheet
    :return:  True if Valid credentials , else False
    """
    excel = load_excel()
    pass


def check_balance():
    pass

def withdraw_amount():
    pass

def deposit_amount():
    pass


def atm_functionalities():
    option = choose_option()
    if option == 1 :
        check_balance()
    elif option == 2:
        withdraw_amount()
    elif option == 3:
        deposit_amount()
    else:
        print("Invalid Input option")

def retry():
    """
    retry validate_user for 3 times and Exit if failed after 3 times
    :return:
    """
    pass

def atm_run():
    validation = validate_user()
    if validation :
        atm_functionalities()
    else:
        #TODO : retrying 3 times only
        retry()



if __name__ == "__main__":
    atm_run()
    # load_excel()