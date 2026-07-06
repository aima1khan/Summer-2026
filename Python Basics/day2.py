a=input("What is your First name : ")
c=input("What is your last name : ")
x=input("What year were you born in ? :")
y=2025-int(x)
z=int(input("What is your weight(in kg) : "))
b=2.205*z
print("====Personal Profile====")
print(f"Name : {a} {c}")
print(f"Age : {y} years old")
print(f"Weight : {b} pounds")
print(a[0:-2])
d= a + " " + c + " is a coder"
print(d)
e=f"{a} {c} is a coder"
print(e)
print(f"Length of string is : {len(e)}") 
print(e.upper()) #Upper case
print(e.lower()) #Lower case
print(e.find("a")) #Find a character(it will show index of a character in a string)
print(e.replace("coder" , "programmer"))
print(e)
#To check for a string(word) present in a string(string)
print("Aimal" in e) #True
print("Programmer" in e) #False
g=b*(-1)
print(round(g))
print(abs(g))