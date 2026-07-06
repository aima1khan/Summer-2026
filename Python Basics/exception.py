try:
    age =int(input("Age :"))
    income=int(input("Income :"))
    risk=income/age
    print(f"Risk : {risk}")

except ValueError:
    print("Invalid Input")

except ZeroDivisionError:
    print("Age Can't Be Zero")
