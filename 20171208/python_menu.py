# task: menu with dishes and price
# menu should be saved into a menu-file

import json

filename = "menu.json"

with open(filename, "r") as f:
    menu = json.load(f)

print "Welcome to my menu!"

while True:
    print "*" * 20
    print "n) exit program"
    print "a) add to menu"
    print "s) show menu"
    user_input = raw_input("Choose an option: ")

    if user_input.lower() == "n":
        with open(filename, "w") as f:
            json.dump(menu, f)
        break

    elif user_input.lower() == "a":
        dish = raw_input("Please enter new dish: ")
        price = raw_input("How much is it? ")

        menu[dish] = price

        new = raw_input("Do you want to enter another dish or show menu? Please enter y/n: ")

        if new.lower() == "n":
            break

    elif user_input.lower() == "s":
        for k, v in menu.items():
            print k, v

print "Thank you and goodbye."
