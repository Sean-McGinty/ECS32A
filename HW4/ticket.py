age=int(input("Enter age:"))
if age<3:
    print("Price: FREE")
elif age>=65:
    print("Price: $39.95")
elif age>=3 and age<=12:
    print("Price: $29.95")
elif age>=7 and age<=13:
    print("Price: $39.95")
else:
    College_ID=input("College ID? (y/n)")
    if College_ID=="y":
        print("Price: $39.95")
    else:
        print("Price: $49.95")
