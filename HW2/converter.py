#converter.py
#ECS32A
#
#Outputs integer and binary representations of a user-inputed character
character=input("Enter a character:") #Creates a Variable of a user-inputed character
number=int(ord(character)) #Creates a variable of integer of that chararcter
binary=bin(number) #Creates a variable of the binary representation of that character
print(character,"corresponds to the integer",number,"which is",binary,"in binary.")
