price = 254 
print(price)
print(hex(price))


print("------")
print(hex(0))
print(hex(1))
print(hex(2))
print(hex(9))
print(hex(10))
print(hex(11))

print("------")
red=0xAA
print(red)

print("----BINARY----")
print(bin(1))
print(bin(2))
print(bin(3))
print(bin(4))
# print(bin(5.1)) Does not work in Binary because of decimal point, python wont show it. 

print()
print()
print()
print()
print()
print()
print()

mask1 = 0b1000
mask2 = 0b1011

print(bin(mask1 & mask2)) #Binary and operator   (ampersand symbol)
print(bin(mask1 | mask2))  #Binary or operator   (pipe symbol)
print(bin(mask1 ^ mask2))  #Binary XOR operator  (caret symbol)








