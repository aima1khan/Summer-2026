b=input("phone : ")
a={
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
}
output =""
for c in b:
    output+=a.get(c,"!")+" "

print(output)