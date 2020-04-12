#divide.py
#ECS32A
#
#Integer Division Calculator
Dividend=int(input("Enter a number:")) #User inputs Dividend and Saves as a Variable
Divisor=int(input("Enter a number to divide that by:")) #User inputs Divisor and Saves as a Variable
quotient=Dividend//Divisor #Performs Floored Division of Dividend/Divisor
remainder=Dividend%Divisor #Calculatates Remainder after Division
print(Dividend,"divided by",Divisor,"is",quotient,"with",remainder,"remaining")
