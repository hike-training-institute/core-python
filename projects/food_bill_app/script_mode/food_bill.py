from details import food_prices, personal_details
import logging
from configs.log_configs import food_bill_logger as f_log
f_log.setLevel(logging.DEBUG)

def show_billing_options(restaurant):
    f_log.warning("Here is your hotel menu, Enjoy your meal ....")
    for i, j in food_prices[restaurant].items():
        f_log.debug ("{} : {}".format(i, j))

def validate_user(user, pwd):
    for item in personal_details:
        if item["user"] == user and item["pass"] == pwd:
            return item["user"], item["restaurant"]
    else :
        f_log.warning("Entered Invalid User and Password...")
        return None, None

def get_user_credentials():
    restaurant = None
    f_log.warning("Getting user inputs")
    user = input("enter your username : ")
    pwd = input("enter your password : ")

    return user, pwd


if __name__ == "__main__":

    user, pwd= get_user_credentials()
    valid_user, restaurant = validate_user(user, pwd)

    if valid_user:
        f_log.info("User is valid...")
        show_billing_options(restaurant)

    else :
        f_log.warning("User not found, Try again ...")

