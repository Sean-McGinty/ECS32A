Bill=float(input("Enter total bill:"))
for i in range (15,26,1):
    Tip_Amount=(i/100)*Bill
    tip_str = "${:.2f}".format(Tip_Amount)
    print(str(i)+"% is",tip_str)
