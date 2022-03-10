import secrets

global get_token
get_token = True

# Variables of available characters for the password
lowercase = 'abcdefghijklmnopqrstuvwxyz'
caps = lowercase.upper()
characters = '!@#$%^&*()'

# Sets default variables and prompts user for input
def setup():
    global password
    global get_token
    
    x = 0
    password = []
    
    # Checks for first time launch
    if get_token == True:
        repeat = int(input('How many characters long do you want your password? '))
        get_token = False
        return main(x, repeat)
    
    # Prompts the user if they would like to generate another password
    else:
        again = input('Would you like to create another password? y/n: ')
        if again.lower() == 'y':
            repeat = int(input('How many characters long do you want your password? '))
            return main(x, repeat)
        else:
            exit


# Repeats password_gen(x, repeat) until it's reached the set characters
# After, it joins all the characters in the list into a singular string
def main(x, repeat):

    if x < repeat:
        x = x + 1
        return password_gen(x, repeat)

    # Prints the password and returns to setup()
    else:
        global password
        print(''.join(password))
        return setup()


# Adds the temp variable to the password list
def append_list(temp, x, repeat):
    global password
    
    password.append(temp)
    return main(x, repeat)


# Generates a list for the password
def password_gen(x, repeat):
    global password

    # Generates a secure random number
    num = secrets.randbelow(3)

    # Appends a random character from a variable depending on the number previously generated
    if num == 0:
        temp = secrets.choice(lowercase)
        return append_list(temp, x, repeat)

    elif num == 1:
        temp = secrets.choice(caps)
        return append_list(temp, x, repeat)

    else:
        temp = secrets.choice(characters)
        return append_list(temp, x, repeat)

setup()
