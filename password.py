import secrets
import string

password = []
get_token = False

# Variables of available characters for the password
characters = list(string.ascii_letters + string.digits + string.punctuation)


# Sets default variables and prompts user for input
def setup(password, get_token):
    x = 0
    
    # Checks for first time launch
    if not get_token:
        password_length = int(input('How many characters long do you want your password? '))

        return main(password_length, password)
    
    # Prompts the user if they would like to generate another password
    else:
        again = input('\nWould you like to create another password? y/n: ')

        if again.lower() == 'y':
            password_length = int(input('\nHow many characters long do you want your password? '))

            return main(password_length, password)

        else:
            exit


# Repeats password_gen(x, repeat) until it's reached the set characters
# After, it joins all the characters in the list into a singular string
def main(passwprd_length, password):
    for i in range(passwprd_length):
        temp = secrets.choice(characters)
        password.append(temp)
    

    # Prints the password and returns to setup()
    print(''.join(password))
    password = []
    get_token = True

    return setup(password,get_token)

setup(password, get_token)
