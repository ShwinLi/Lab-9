from menu import Menu
from encoder import encoder

if __name__ == "__main__":
    while True:
        Menu()
        menu_option = int(input("Please enter an option: "))

        if menu_option == 1:
            password_to_encode = int(input("Please enter your password to encode: "))
            encoder(password_to_encode)
            print("Your password has been encoded and stored!")

        if menu_option == 2:
            print(f"The encoded password is {encoder(password_to_encode)}, and the original password is {password_to_encode}.")

        if menu_option == 3:
            break
