def xando(eingabe):
    counterx=0
    countero=0
    for x in eingabe:
        print(x)
        if x == "x":
            counterx += 1
        else:
            countero += 1
    return [counterx, countero]

text = input("Gebe x und o ein ").lower()        
print("Es gibt",xando(text)[0],"x und",xando(text)[1],"y")