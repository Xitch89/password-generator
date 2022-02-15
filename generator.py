import random

masage = 'Password save'
password = ''
choice = input("Choose to use the standard character set or your own, enter standard or own: ")

if choice == "standard":
    def password_from_client_str():
        global password
        foundation = "01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ&*(){}[]|/\?!@#$%^abcdefghijklmnopqrstuvwxyz"
        pass_len = int(input('enter password length: '))
        password = "".join(random.sample(foundation, pass_len))
        print ('Your new password: ', password)
    password_from_client_str()
else:
    def password_from_client_str():
        global password
        foundation = input("Enter your character set: ")
        pass_len = int(input('enter password length: '))
        password = "".join(random.sample(foundation, pass_len))
        print ('Your new password: ', password)
    password_from_client_str()

def save_pass():
    with open('password.txt', 'a') as f:
        for line in password:
            f.write(line)
            f.close
        print (masage)
save_pass()