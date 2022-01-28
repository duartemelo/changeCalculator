# dictionary with available coins:
# key is the coin
# value is the amount of coin available
available_coins = {}


# function with the inputs to add a coin
def add_coin_io():
    coin = int(input("Coin to add:"))
    amount_of_coin = int(input("Amount of coin to add:"))
    return add_coin(coin, amount_of_coin)


# function to add a coin to available_coins
def add_coin(coin, amount_of_coin):
    if available_coins.get(coin) is None:  # if the coin exists but has no value (never happens..)
        available_coins[coin] = amount_of_coin
    else:
        if available_coins[coin] + amount_of_coin < 0:  # if the remaining amount of coins is negative
            raise Exception("Cannot have negative amount of a coin.")
        else:  # if the remaining amount of coins is not negative
            available_coins[coin] += amount_of_coin
    return True


# function with the inputs to give change
def give_change_io():

    price = int(input("Price of product:"))
    given_money = int(input("Given money:"))

    while price > given_money:
        print("Price is bigger than given money.")
        price = int(input("Price of product:"))
        given_money = int(input("Given money:"))

    return give_change(price, given_money)


# function to give change
# price = price of a product, or final price of some purchase
# given_money = money given by someone to pay that purchase
def give_change(price, given_money):
    change = given_money - price  # change calculus

    stock_var_copy = available_coins.copy()  # copy of available_coins to work with it

    change_coins = {}  # creating a dictionary that will have the change coins and their values (amount)

    while change > 0:
        # this try was created since the user can try to give change with no coins added
        try:
            # gets the highest coin in stock_var_copy (starts with the highest coin available)
            current_coin = max(stock_var_copy)
        except:
            raise Exception("Unable to retrieve change")
        while current_coin <= change:
            if change_coins.get(current_coin) is None:
                change_coins[current_coin] = 1
            else:
                change_coins[current_coin] += 1
            change -= current_coin
        del (stock_var_copy[current_coin])  # deletes that coin from stock_var_copy (we will not want it anymore)

    return change_coins


# method that prints a coin dictionary
def print_coin_dict(coin_dict):

    for key in coin_dict:
        print(f"{coin_dict[key]} coin(s) of {key}.")