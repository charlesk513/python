# student form

print("You are most welcome, feel free to fill this simple identification form!\n")
sir_name = input('Input your surname: ')
first_name = input('Input your first name: ')
print('')
course_opted = input('Course done: ')
print('')
emailAccount = input('Your email: ')
print('')
password = input('Your password: ')
print('')
password2 = input('Repeat your password: ')
print('')
if (password == password2):
    print("Go on with your authetification!")
else:
     print("Mismatching passwords!, go back!")
     
print(f"We've sent a message to {emailAccount}, check to enroll with us\n")
print(f"You are most welcome {first_name} to join MUST community! Big up, succeed we must.\n")


