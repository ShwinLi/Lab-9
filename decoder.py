def decoder(encoded_password):
    decoded_password = list(str(encoded_password))

    for i in range(len(decoded_password)):
        if int(decoded_password[i]) >= 3:
            decoded_password[i] = int(decoded_password[i]) - 3

        elif int(decoded_password[i]) == 0:
            decoded_password[i] = 7

        elif int(decoded_password[i]) == 1:
            decoded_password[i] = 8

        elif int(decoded_password[i]) == 2:
            decoded_password[i] = 9

    for i in range(len(decoded_password)):
        decoded_password[i] = str(decoded_password[i])

    return ''.join(decoded_password)
