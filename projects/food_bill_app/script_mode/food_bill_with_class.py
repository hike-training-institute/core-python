from details_with_class import Detail
class Func() :
    def show_billing_options(self, restaurant):
        print("Here is your hotel menu, Enjoy your meal ....")
        for i, j in Detail.food_prices[restaurant].items():
            print (i, ':', j)
    def validate_user(self, user, pwd):
        for item in Detail.personal_details:
            if item["user"] == user and item["pass"] == pwd:
                return item["user"], item["restaurant"]
        else:        ####Important -else is for for loop. once all iteration done and not found any match this else will get executed.
            return None, None

    def get_user_credentials(self):
        user = input("enter your username : ")
        pwd = input("enter your password : ")
        return user, pwd

class Food_bill(Func):
    def first(self, count):
        user, pwd = self.get_user_credentials()
        valid_user, restaurant= self.validate_user(user, pwd)
        if valid_user:
            self.show_billing_options(restaurant)
        else:
            if count < 3:
                print("User not found, Try again ...")
                count += 1
                self.first(count)
            else:
                print("You have exceeded the maximum 3 number of attempts.....Exiting.......")
                exit()
count = 1
abc = Food_bill()
abc.first(count)