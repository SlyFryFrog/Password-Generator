import secrets
import string

password = []
get_token = False

# Variables of available characters for the password
characters = list(string.ascii_letters + string.digits + string.punctuation)


# Sets default variables and prompts user for input
def setup(password, get_token):
    # Checks for first time launch
    if not get_token:
        print('Welcome to the Password Generator made by SlyFryFrog\n')
        password_length = int(input('Please enter the desired length of your password: '))

        return main(password_length, password)

    # Prompts the user if they would like to generate another password
    else:
        again = input('\nWould you like to create another password? y/n: ')

        if again.lower() == 'y':
            password_length = int(input('\nPlease enter the desired length of your password: '))

            return main(password_length, password)


# Repeats until it's reached the set characters
# After, it joins all the characters in the list into a singular string
def main(password_length, password):
    # Checks if user input is too short
    if password_length < 8:
        print(f'Sorry, but {password_length} is too short.')
        print('Please enter a value greater than 7 to create a more secure password.')
        get_token = True
        return setup(password, get_token)

    else:
        for i in range(password_length):
            temp = secrets.choice(characters)
            password.append(temp)

        # Prints the password and returns to set up()
        print(''.join(password))
        password = []
        get_token = True

        return setup(password, get_token)


setup(password, get_token)
