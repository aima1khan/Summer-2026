fruit = "banana"
a = "n" in fruit
print(a)

b = "abn" in fruit
print(b)

c = "ban" in fruit
print(c)

d="ABC"
e=d.capitalize()
print(e)

f=d.lower()
print(f)

g=fruit.find("a")
print(g)
#if a letter is not present it return -1
h=fruit.find("c")
print(h)

i=fruit.replace("a","e")#it will replace all "a" with "e" 
print(i)

#stripping whitespaces
j="    Heloo G    "
k=j.lstrip()
print(k)

l=j.rstrip()
print(l)

m=j.strip()
print(m)

#Prefixes
n=fruit.startswith("b")
print(n)
o=fruit.startswith("B")
print(o)

