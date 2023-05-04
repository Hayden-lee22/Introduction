print("---Variables---")

#here we declear the variable amount_of_cats
#we also assign it the value 2
amount_of_cats = 2
print(amount_of_cats)

# here we are reusing the same variable
# #we reassign it the value 2 + 1 
amount_of_cats = amount_of_cats + 1
print(amount_of_cats)

# lets experiment
print(amount_of_cats + 99)
print(amount_of_cats)

print(type(amount_of_cats))


print("-----Dynamite----")
print()

# A string? Nice
spam = "eggs"
print(spam, type(spam))

spam = 42
print(spam, type(spam))

print()
print()
print("---Operators----")
print()
print()
print()


count = 1
print(count + 1)
print(type (count + 1))
# print(count + "spam")

# Decimals and ints are both numbers 

print(count + 1.7)
print(count + .3)
print(type (count + 7.))
print(count + True)

print("eggs" + "spam" + "spam" + "cherry")

print()
print()
print()
print("---Operators---")
print()
print()
print()

score = 10
print(score - 51)
print(score * 4)
print(score / 4)
print("----")
print(score % 1) # Modulus / Modulo / Reminder / Residual
print(score % 2)
print(score % 3)
print(score % 4)
print(score % 5)
print(score % 6)
print(score % 7)
print(score % 8)
print(score % 9)
print(score % 10)


print("-----Exponential-----")
print(score ** 2)
print(score ** 3)
print(score ** 4)

print("--Floor Division--")
print(score // 1)
print(score // 2)
print(score // 3)  # Divide and round the result down
print(score // 4)
print(score // 5)
print(score // 6)
print(score // 7)

print()
print()
print("---Assignment Operators-----")
print()
print()

score = 100
# score = score + 20 The old way
score += 30 #same as above, exxcept with 30 instead of 20
score -= 3
print(score)


my_name = "Batman"
my_name += " Spam"
print(my_name)


print()
print()
print("---Math Fun---")
print()
print()

print(max(2, 1, 4, 9, 1))
print(min(2, 1, 4, 9, 1, 0.1, -3))
print(abs(5))
print(abs(-41))  # "absolute" , distance from 0 
print(pow(3,4))  # "3 to the power of 4"
print(round(3.14159))
print(round(3.9)) 
print(round(3.49999999))
print(round(3.49999999,2))
print(round(13.415999999,2))



import math

# Instead of round
print(math.ceil(1.1)) #Rounding, but... always up!
print(math.ceil(1.2)) #Rounding, but... always up
print(math.ceil(1.8)) #Rounding, but...
print(math.ceil(1.9)) #Rounding, but...

print(math.floor(1.1)) #Rounding, but...always down
print(math.floor(1.2)) #Rounding, but...always down
print(math.floor(1.8)) #Rounding, but...always down
print(math.floor(1.9)) #Rounding, but...always down


print()
print()
print()
print()

my_name = input("What's your name traveller? ") 
print("Hello" , my_name)
print(type(my_name))

print()
print()
print()
print()
print()



money = input("How much you got? ")
money = float(money) #cast the money String value to a float
money = money * 3
print ("now you have" , money)










