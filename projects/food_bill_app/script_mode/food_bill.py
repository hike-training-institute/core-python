from details import food_prices, personal_details

def show_billing_options(restaurant):
    print('\n')
    print("Here is your hotel menu, Enjoy your meal ....")
    for i, j in food_prices[restaurant].items():
        print (i, ':', j)

def validate_user(user, pwd):

    for item in personal_details:
        if item["user"] == user and item["pass"] == pwd:
            return item["user"], item["restaurant"]
    else :
        return None, None

def get_user_credentials():

    user = input("enter your username : ")
    pwd = input("enter your password : ")

    return user, pwd


if __name__ == "__main__":
    def first(count):
        user, pwd= get_user_credentials()
        valid_user, restaurant = validate_user(user, pwd)

        if valid_user:
            show_billing_options(restaurant)
        else :
            if count < 3:
                print("User not found, Try again ...")
                count+=1
                first(count)
            else :
                print("You have exceeded the maximum 3 number of attempts.....Exiting.......")
                exit()
    count =1
    first (count)