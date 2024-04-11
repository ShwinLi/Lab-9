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


