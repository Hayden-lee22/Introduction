my_name = input("Whats your name? ")
my_age = int(input("How old? "))   #Cast the result of intup to an interger

if (my_age <= 17):
    # Check the name
    # Nested conditionals

    if (my_name == "Veera"):        # Conditional statment 
        # Indentation is critical in Python!
        # It creates a section or sequence of code
        print("Hi Veera")
        print("Looking good!")
        score = 10 


    elif (my_name == "Rauli"):
        print("Heeeey Rauli")
        print("You poop")
        print("love you!")
        score = 99
    else:
        print("Who are you even?")
        score = 3


    print("SCORE: ", score)
else:
    print("Nope. Just for Kidz! ")

    



