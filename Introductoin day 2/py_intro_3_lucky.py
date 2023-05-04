import random 

lucky = random.randint(0,5) #Chaos

password = input("Welcome to casino Py! Password?")

if password != "Swordfish":     # != is a negation, if Not true
    print("Access denied")
else:
    if lucky == 5:
        print("You win big!") 
    elif lucky >=3:
        print("You win small!")
    elif lucky == 0: 
        print("You lose big!")
    else:
        print("You lose a bit")



