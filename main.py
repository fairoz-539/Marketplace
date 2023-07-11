

def create_file(R_name, R_pwd):
    with open("user_details.txt", 'a') as file:
        file.write(R_name + " " + R_pwd + "\n")


def read_file(L_name, L_pwd):
    with open("user_details.txt", 'r') as file:
        for line in file:
            values = line.strip().split(" ")
            if len(values) >= 2:
                stored_word1, stored_word2 = values
                if stored_word1 == L_name and stored_word2 == L_pwd:
                    return True


class Market_place:
    def __init__(self):
        pass

    def register(self):
        print("Register for free to deal on with MarketPlace ")
        R_name = input("Enter your name: ")
        R_pwd = input("Enter your password: ")
        new_file = create_file(R_name, R_pwd)

    def login(self):
        print("Have an account already :) ! That's so cool login to float deeper ")
        L_name = input("Enter your name: ")
        L_pwd = input("Enter your password: ")
        if read_file(L_name, L_pwd) == True:
            return 0

    def buy_products(self):
        self.your_products = {}
        print("Welcome to the Buying Marketplace ! ")
        total = int(input("How many products do you want to buy:"))

        for i in range(total):
            p_name = input("Enter product names: ")
            values = int(input("Enter product price: "))
            self.your_products[p_name] = values
        return print("You have successfully bought ", self.your_products, " these products")

    def sell_products(self):
        self.sold_products = {}
        print("Welcome to the Selling Marketplace ! ")

        total = int(input("How many products do you want to sell: "))

        for i in range(total):
            s_name = input("Enter products name  ")
            s_price = int(input("Enter the price: "))
            self.sold_products[s_name] = s_price

        return print("You have successfully sold ", self.sold_products, " these products")


marketplace = Market_place()

print("WELCOME TO THE MARKETPLACE !")
choice = input("Do you have an account : (Yes/no) ").lower()
if choice == "yes":
    if marketplace.login() == 0:
        choice = input("Do you want to buy or sell the products: (buy/sell) : ").lower()
        if choice == "buy":
            marketplace.buy_products()
        elif choice == "sell":
            marketplace.sell_products()
        else:
            print("Market place is for only buying and selling !")
elif choice == "no":
    marketplace.register()
else:
    print("Please Enter a Valid response ")
