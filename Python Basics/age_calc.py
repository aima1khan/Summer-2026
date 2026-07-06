z=int(input("What was the date of your birth :"))
y=int(input("In which month you were born : "))
x=int(input("In which year you were born : "))
a=2025-x
b=2026-x
c=12-y
d=30-z
print(f"You are {b} years old")
e=(a*12)+c
f=(e*30)+d
print(f"Your are {e} months old")
print(f"You are approx {f} days old")