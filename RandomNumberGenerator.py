import random
random_integer = random.randint(1, 100)
#print(random_integer)
a = int(input("Enter any number between 1 and 100: "))
while(random_integer != a):
    if(a>=(random_integer-10) and a<=(random_integer+10)):  
        print("Hot")
        a = int(input("Enter the number again: "))
    else:   
        print("Cold")
        a = int(input("Enter the number again: "))
if(random_integer == a):
    print("You guessed it correctly!!")
