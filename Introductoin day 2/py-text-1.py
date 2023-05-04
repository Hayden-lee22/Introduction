#my_text = "TEST2123"
#my_text = "2123"
#my_text = "TEST2123öü"
my_text = "this is a Test"


changed = my_text.upper()

print(my_text.upper())
print(my_text.capitalize())
print(my_text.lower())
print(my_text.isalpha())  # alpha = part of the alphabet 
print(my_text.isalnum())  # alnum = alphanumeric
print(my_text.split())    # Splits the string from spaces into a list 
print(my_text.split("T")) # Split the string from the "T" character (is case sensative)

long_text = '''It was poopy outside
Flop, dop pop 
The end.'''

print(long_text.split("\n"))

print("A nice kitten".replace("kitten", "dragon"))

desc = "A mage conjured an image of a dragon"
print(desc.replace(" mage ", " wizard ")) # need to be awear that "mage" is also in the word "image" and when the program is run it will remove all instances of "mage"
                                          # can be avoided by adding spaces on either side of words


text = "Hayden \"Reqw\" Peltonen"  # \ is the escape character in python 

text = "Rauli\n\tStr: 3\n\tInt: 2\n\tHP: 7"
print(text)

print("-----------")


print(len ("caramel ice"))
print(len(["water", "ice", "snow"]))   #[]
#print(len(0b001001)) can't do len for numbers


drinks = ["coffee", "tea", "water"]
print(drinks[0][2])  #First item in drinks, thired letter....

drinks.append("Juice")
drinks.append(7)
print("drinks")









