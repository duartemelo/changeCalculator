# main.py - used to interact with the user, calls functions from functions.py
import functions as functions


option = 0
while option != "4": # 3 is exit
    print("Menu")
    option = input("1: Add or remove coin;\n2: Show coins;\n3: Calculate Change;\n4: Exit\n>> ")


    # ADD OR REMOVE COIN

    if option == "1": 
        try:
            if functions.add_coin_io():  # if coin is added with success
                print("Success.")
            else:  # if something went wrong when adding the coin
                print("Something went wrong.")
        except Exception as e:  # exception raised by called function
            print(e)

    # CHECK COINS
    
    elif option == "2":
        try:
            print("Available coins:")
            functions.print_coin_dict(functions.available_coins)
        except Exception as e:
            print(e)

    # CALCULATE CHANGE

    elif option == "3":
        try:
            change_list = functions.give_change_io()
            functions.print_coin_dict(change_list)
        except Exception as e:
            print(e)

