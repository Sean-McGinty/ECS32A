#change.py
#Sean McGinty
#
#Convert Change to Different Numbers of Coins
Number_Quarters=0
Number_Dimes=0
Number_Nickels=0
Number_Pennies=0

change=int(input("Enter change:"))
if change % 25 == 0:
    Number_Quarters=change//25
else:
    change_after_quarters=change-(change//25)*25
    if change_after_quarters % 10 == 0:
        Number_Dimes =change_after_quarters//10
        Number_Quarters=change//25
    else:
        change_after_quarters_and_dimes=change_after_quarters-(change_after_quarters//10)*10
        if change_after_quarters_and_dimes % 5 ==0:
            Number_Nickels  =change_after_quarters_and_dimes//5
            Number_Dimes    =change_after_quarters//10
            Number_Quarters =change//25
        else:
            Number_Quarters =change//25
            Number_Dimes    =change_after_quarters//10
            Number_Nickels  =change_after_quarters_and_dimes//5
            Number_Pennies  =change_after_quarters_and_dimes - (change_after_quarters_and_dimes//5)*5

print("Quarters:",Number_Quarters)
print("Dimes:",Number_Dimes)
print("Nickels:",Number_Nickels)
print("Pennies:",Number_Pennies)
