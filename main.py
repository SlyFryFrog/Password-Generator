import secrets
import string

# Sets default variables and prompts user for input
def setup(password, get_token, characters):
    # Checks for new password request
    if not get_token:
        try: 
            password_length = int(input('Please enter the desired length of your password: '))
            return password_gen(password_length, password, characters)

        except:
            print("Invalid response, please a number.")
            return setup(password, get_token, characters)


    # Prompts the user if they would like to generate another password
    else:
        again = input('\nWould you like to create another password? y/n: ')

        if again.lower() == 'y':
            password_length = int(input('\nPlease enter the desired length of your password: '))

            return password_gen(password_length, password, characters)


# Repeats until it's reached the set characters
# After, it joins all the characters in the list into a singular string
def password_gen(password_length, password, characters):
    # Checks if user input is too short
    if password_length < 8:
        print(f'Sorry, but {password_length} is too short.')
        print('Please enter a value greater than 7 to create a more secure password.')
        get_token = True
        return setup(password, get_token, characters)

    else:
        for i in range(password_length):
            temp = secrets.choice(characters)
            password.append(temp)

        # Prints the password and returns to set up()
        print(''.join(password))
        password = []
        get_token = True

        return setup(password, get_token, characters)



if __name__ == '__main__':
    password = []
    get_token = False

    # Variables of available characters for the password
    characters = list(string.ascii_letters + string.digits + string.punctuation)

    print('Welcome to the Password Generator made by SlyFryFrog\n')

    setup(password, get_token, characters)