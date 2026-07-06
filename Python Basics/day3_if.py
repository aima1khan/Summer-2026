house_price =1000000
print(f"House Price : {house_price} $")
buyer_credit=int(input("Enter Your Budget/Credit : "))
salary=int(input("Enter Yoyr monthly salary (in $) : "))

if buyer_credit<house_price and salary<1000:
    a=house_price*0.2
    house_price=house_price-a
    print(f"Your Discounted(20%) House Perice is : {house_price}") 

elif buyer_credit>house_price or salary>1000:
    a=house_price*0.1
    house_price=house_price-a
    print(f"Your Discounted(10%) House Price : {house_price} ")
else :
    print("You don't have enough credit to buy a house")