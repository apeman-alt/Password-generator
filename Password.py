#Josh Muszka
#Created Jan 29, 2022
#Last updated Jan 29, 2022
#A password generator, gives user the option to create their own custom password
#If user chooses custom password, program makes sure that it's between 6 and 16 characters, has at least one number, one lower case letter, one upper case letter, and one symbol

def check_number(password):

    #checks to see if there's a number in password
    for i in range(len(password)):
        letter = password[i]
        #compare each character in the password to the ASCII values for numbers 0-9
        if ord(letter) >= 48 and ord(letter) <= 57:
            return True
    
    return False

def check_symbol(password):

    for i in range(len(password)):
        letter = password[i]
        #compare each character in the password to the ASCII values for punctuation symbols
        #ASCII doesn't have all its punctuation combined into one section, so four separate if statements are needed
        if ord(letter) >= 33 and ord(letter) <= 47:
            return True
        if ord(letter) >= 58 and ord(letter) <= 64:
            return True
        if ord(letter) >= 91 and ord(letter) <= 96:
            return True
        if ord(letter) >= 123 and ord(letter) <= 126:
            return True
    return False

def check_uppercase(password):

    for i in range(len(password)):
        letter = password[i]
        #compare each character in the password to the ASCII values for capital letters
        if ord(letter) >= 65 and ord(letter) <= 90:
            return True
    return False

def check_lowercase(password):

    for i in range(len(password)):
        letter = password[i]
        #compare each character in the password to the ASCII values for lower case letters
        if ord(letter) >= 97 and ord(letter) <= 122:
            return True
    return False

def check_length(password):

    #check if password is correct length
    if len(password) < 6 or len(password) > 16:
        return False
    return True



print("Welcome to password setup")
print("Would you like to set a custom password or generate a random one?")
print("TYPE 0 for custom and 1 for random") #will add random password feature in the future

choice = input()
password = ""

while not choice == '0':
     print("Error: Please pick a valid option")
     choice = input()

#custom password
if choice == '0':
    print("Password must be between 6 and 16 characters, contain at least one number, one symbol, one lowercase, and one uppercase letter")
    password = input("Please enter your password: ")

    warning = "Password must" #string to let user know what they're missing from password (will be appended later according to what criteria is missing)

    contains_number = check_number(password)
    contains_symbol = check_symbol(password)
    contains_uppercase = check_uppercase(password)
    contains_lowercase = check_lowercase(password)
    correct_length = check_length(password)
    
    while not contains_number or not contains_symbol or not contains_uppercase or not contains_lowercase or not correct_length:
        if not contains_number:
            warning += " contain at least one number,"
        if not contains_symbol:
            warning += " contain at least one symbol,"
        if not contains_uppercase:
            warning += " contain at least one upper-case letter,"
        if not contains_lowercase:
            warning += " contain at least one lower-case letter,"
        if not correct_length:
            warning += " be between 6 and 16 characters long,"

        #remove comma at end of string
        warning += "#"
        warning = warning.replace(",#", "")

        print(warning) #tell user what's wrong with their password

        password = input("Please re-enter your password: ") #prompt to re-enter password

        #check password again
        warning = "Password must" #string to let user know what they're missing from password (will be appended later according to what criteria is missing)
        contains_number = check_number(password)
        contains_symbol = check_symbol(password)
        contains_uppercase = check_uppercase(password)
        contains_lowercase = check_lowercase(password)
        correct_length = check_length(password)

#if choice == 1:
#    print()

print("Your new password is: " + password)



