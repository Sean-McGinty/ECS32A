initial_value=int(input("Enter an initial Roth IRA deposit amount:"))
APR=int(input("Enter an annual percent rate of return:"))
current_value=initial_value
i=0
while current_value<initial_value*2:
    current_value=current_value +   current_value*(APR / 100)/12
    current_value_formatted= "${:.2f}".format(current_value)
    i+=1
    print("Value after month","{:.0f}:".format(i),current_value_formatted)
print("It will take","{:.0f}".format(i),"months to double your investment with a","{:.0f}%".format(APR), "return.")
