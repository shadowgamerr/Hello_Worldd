logmessage =("_____HeLlo And Welcome To Our Program_____ \n  _____Please Register To Continue_____")
print(logmessage)

with open ("data.txt", mode="r") as f:
    f.readlines()

# Regsiter
userregister = input("Chose a Username")
passregister = input("Pick a Strong Password")

# Welcome Message
print("you have successfully registered")
print ("Please Log in!!!")

# Log in
userlogin = input("Enter your Username")
passlogin = input("Enter Your Password")

#check for information
if userlogin == userregister and passlogin == passregister:
    print ("you have been successfully logged in")
    with open("data.txt", mode='a') as file:
        file.write(userlogin+" ")
        file.write(passlogin)
else:
    print("Invalid Information!!!!!")




