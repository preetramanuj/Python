#Bill management
item_list=[]
total_amount=0
item_no=int(input("Enter number of item:"))
for i in range(1,item_no+1):
    temp=float(input(f"Your iteam Price {i}:")) 
    item_list.append(temp)
    total_amount += temp
    print(total_amount)
total_amount=total_amount+(total_amount*18)/100
print(total_amount)

#Discount
cupan_code="E20"
choice=input("If you have coupen code:")
if(choice == "Yes" or choice == "yes" or choice == "YES"  ):
    customer_cupan_code=input("Enter coupen code:")
    if(customer_cupan_code == cupan_code):
        total_discouted=(total_amount*10)/100
        total_amount=total_amount-total_discouted
        total_amount=total_amount+(total_amount*18)/100
        print("Your amount after discount is",total_amount,":")
        total_discouted_list=[]
        total_discouted_list.append(total_amount)
elif(choice == "No" or choice == "no" or choice == "NO" ):
    print("Your total amount is:",total_amount)
else:
    print("Invalid Choice")

#carry Bag
carry_bag=input("You want carry bag:")
if(carry_bag=="Yes" or carry_bag == "YES" or carry_bag == "yes"):
    if total_amount in total_discouted_list:
        grand_total=total_amount+20
        print("Your Grand Total is",grand_total,":")
elif(carry_bag=="No" or carry_bag == "NO" or carry_bag == "no"):
    grand_total=total_amount+20
    print("Your Grand Total is",grand_total,":")
else:
    print("Invalid Choice")




    


                 
