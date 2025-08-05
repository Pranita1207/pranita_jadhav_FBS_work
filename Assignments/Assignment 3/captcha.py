import random

# Taking input for username and password
userid = input("Enter the username: ")
password = int(input("Enter the password: "))

# Generating and displaying captcha
captcha = random.randint(1111, 9999)
print(f'Captcha: {captcha}')

# Taking captcha input again
user_captcha = int(input("Enter the captcha again: "))

# Verifying login
if ("Komal Patil" == userid) and (99181225 == password):
    if (user_captcha == captcha):
        print('success! Access granted')
    else:
        print('captcha is wrong')