def check_complexity(password):
    if len(password) >= 8:
        if any((i.isupper() for i in password)) and any((i.islower() for i in password)) and any((i.isdigit() for i in password)) and any((not i.isalnum() for i in password)):
            print("Password is strong")
        else:
            if not any(i.isupper() for i in password):
                print("Password should contain at least one Capital letter")
    
            if not any(i.islower() for i in password):
                print("Password should contain at least one small letter")
            
            if not any(i.isdigit() for i in password):
                print("Password should contain at least one digit")

            if not any(not i.isalnum() for i in password):
                print("Password should contain at least one Special Character")
    else:
        print("Password Should be 8 characters long") 
    

password = input("Enter a Password: ")
check_complexity(password)
