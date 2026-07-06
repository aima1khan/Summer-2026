n=5
while n>0:
    print(n)
    n=n-1

a=0
while a<21:
    if a%2==0:
        a=a+1
        continue
    print(a)
    a=a+1

#to find largest number
a=[15,223,3798,4,65,88,70]
l=a[0]
for i in a:
    if i>l:
        l=i

print(l)