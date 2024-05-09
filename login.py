print ("Welcome, kindly create a new account")

firstname1 = input ("Enter your First Name: ")
lastname1 = input ("Enter your Last Name: ")
email1 = input ("Enter your Email: ")
address1 = input ("Enter your address: ")
number1 = input ("Enter your phone number: ")
username1 = input ("Enter your username: ")
password1 = input ("Enter your password: ")
password11 = input ("Confirm your password: ")

print ("Account created successfully!!")
print ("Log in now...")


username2 = input ("Enter your username: ")
password2 = input ("Enter your password: ")

if username2 == username1 and password2 == password1:
    print ("Voila! Logged in successfully")
    
elif username2 != username1:
    print ("Oops! Invalid username")
    
elif password2 != password1:
    print ("Oops! Invalid password")
    
else:
    print ("Sorry! Something went wrong")
    

