
correct_userid="admin"
correct_password="1234"

user_id=input("Enter User ID:")
password =input("Enter Password:")

if user_id == correct_userid and password == correct_password:
    print("Login successful!")
else:
    print("Invalid User ID or Password.")
     