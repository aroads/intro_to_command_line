valid_password = False

#until we get a valid password
while not valid_password: 

    password = input("Please enter a password. I require 6-16 characters to be satiated.")

    length_valid = False
    special_character_valid = False

    special_character_check = "?" in password

    if len(password) < 16 and len(password) > 6:
        lenth_valid = True
    elif len(password) < 6: 
        print("Password too little, silly.")
    else: 
        print("Password must be between 8-16 characters, or I'll get mad.")

    if special_character_check: 
        special_character_valid = True
    else: 
        print("Give me a question mark or face the consequences.")

        
if special_character_valid and length_valid: 
    print("Your password has been set. Thank you for succeeding at such a simple task.")
    valid_password = True