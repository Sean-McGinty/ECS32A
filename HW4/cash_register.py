print("Cash register")
total=0
item_number=0
while True:
    price=str(input("Enter the price of an item:"))
    if price=="":
        total_str = "${:.2f}".format(total)
        break
    total+=float(price)
    total_str = "${:.2f}".format(total)
    item_number+=1



print("You entered",item_number,"items totaling", total_str)
