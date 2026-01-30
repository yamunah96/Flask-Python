from customer import*
from database import*
from register import*

status = False
print("Welcome to Mohit Banking Project")

while True:
    try:
        register = int(input("1. SignUp\n"
                             "2. SignIn: "))
        if register == 1 or register == 2:
            if register == 1:
                signUp()
            if register == 2:
                user = signIn()
                status=True
                break
            else:
                print("Please Enter Valid Input From Options")

    except ValueError:
        print("Invalid Input Try Again with Numbers")