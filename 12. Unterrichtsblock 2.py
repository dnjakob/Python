class tier:
    name = "Benny"
    fellfarbe = "schwarz"
    
    def futter(self):
        print("Ich liebe Knochen")

class familienmitglied:
    sohn = "Peter"
    alter =  18

    def abenteuer(self):
        print("Der lange Aal schlackert im Nebel der Schlacht")

class hund(tier, familienmitglied):

    def futter(self):
        super().futter()
        print("Ich liebe meinen Sohn", self.sohn,", der schon", self.alter,"Jahre alt ist und einen Hund besitzt mit dem Namen",self.name+".")
       
labrador = hund()
labrador.futter()
labrador.abenteuer()