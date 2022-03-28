import random

def genPassword(length):
    default = "abcdefghijklmnopqrstuvwxyz1234567890,./;[]\-="
    string = ""
    
    for i in range(length):
        string = string + random.choice(default)
        
    return string

length = int(input("Input Panjang Password: "))

print("Password is: " , genPassword(length))
