def emoji_converter(x):
    b=a.split(" ")
    emoji={
        ":)" : "😊",
        ":(" : "😓"

    }    
    output=""
    for i in b:
        output+= emoji.get(i,i)+" "
    return output
a=input(">")
print(emoji_converter(a))


