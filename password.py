import secrets
import string

password = []
temp = ''
get_token = False

# Variables of available characters for the password
characters = list(string.ascii_letters + string.digits + string.punctuation)

# Sets default variables and prompts user for input
def setup(password, get_token):
    x = 0
    
    # Checks for first time launch
    if not get_token:
        repeat = int(input('How many characters long do you want your password? '))

        return main(x, repeat, password)
    
    # Prompts the user if they would like to generate another password
    else:
        again = input('\nWould you like to create another password? y/n: ')

        if again.lower() == 'y':
            repeat = int(input('\nHow many characters long do you want your password? '))

            return main(x, repeat, password)

        else:
            exit


# Repeats password_gen(x, repeat) until it's reached the set characters
# After, it joins all the characters in the list into a singular string
def main(x, repeat, password):

    if x < repeat:
        x = x + 1

        return append_list(temp, x, repeat, password)

    # Prints the password and returns to setup()
    else:
        print(''.join(password))
        password = []
        get_token = True

        return setup(password,get_token)


# Adds the temp variable to the password list
def append_list(temp, x, repeat, password):
    temp = secrets.choice(characters)
    password.append(temp)

    return main(x, repeat, password)

setup(password, get_token)
