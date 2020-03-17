from details import food_prices, personal_details

def show_billing_options(restaurant):
    pass

def validate_user(user, pwd):
    valid_user=None
    restaurant = None
    return valid_user, restaurant

def get_user_credentials():
    restaurant = None
    user = input("enter your username :")
    pwd = input("enter your password :")

    return user, pwd


if __name__ == "__main__":
    user, pwd= get_user_credentials()
    valid_user, restaurant = validate_user(user, pwd)

    if valid_user:
        show_billing_options(restaurant)

