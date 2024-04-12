def encoder(password_to_encode): # this encodes stuff
    encoded_password = list(str(password_to_encode))

    for i in range(len(encoded_password)):
        if int(encoded_password[i]) < 7:
            encoded_password[i] = int(encoded_password[i]) + 3

        elif int(encoded_password[i]) == 7:
            encoded_password[i] = 0

        elif int(encoded_password[i]) == 8:
            encoded_password[i] = 1

        elif int(encoded_password[i]) == 9:
            encoded_password[i] = 2

    for i in range(len(encoded_password)):
        encoded_password[i] = str(encoded_password[i])

    return ''.join(encoded_password)

def Menu(): # prints the menu
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


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
