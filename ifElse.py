username='sezen'
password='sude'

usernameInputed=input("Username: ")
passwordInputed=input("Password: ")

isLoggedin=(username==usernameInputed and password==passwordInputed)
if isLoggedin:
    print(f"Welcome {usernameInputed.capitalize()}")
elif username==usernameInputed and not password==passwordInputed:
    print("Password is wrong.")
else:
    print("Username or password is wrong.")
