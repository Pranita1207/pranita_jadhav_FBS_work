userid='admin'
password='1234'

for i in range(3):
    u=input("Enter the user id:")
    p=input("Enter the password:")
    
    if u== userid and p== password:
        print('Login Successful')
        break
    else:
        print('Invalid .Try Again')
else:
    print('You have used your 3 attempts. Access DEnied')