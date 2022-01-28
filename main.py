# main.py - used to interact with the user, calls functions from functions.py
import functions as f


option = 0
while option != "3": # 3 is exit
    print("Menu")
    option = input("1: Add or remove coin;\n2: Calculate Change;\n3: Exit.\n>>")
    if option == "1":  # add or remove coin
        try:
            if f.add_coin_io():  # if coin is added with success
                print("Success.")
            else:  # if something went wrong when adding the coin
                print("Something went wrong.")
        except Exception as e:  # exception raised by called function
            print(e)
    elif option == "2":  # calculate change
        try:
            change_list = f.give_change_io()
            f.print_coin_dict(change_list)
        except Exception as e:
            print(e)
