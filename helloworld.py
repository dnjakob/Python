def xando(eingabe):
    counterx=0
    countero=0
    for x in eingabe:
        print(x)
        if x == "x":
            counterx += 1
        else:
            countero += 1
    return "Es gibt",counterx,"xs und",countero,"os"

text = input("Gebe x und o ein ").lower()        
print(xando(text))