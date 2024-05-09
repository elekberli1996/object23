
listimiz=[10,2,3,40,5,6]

class numune(): 
    def __init__(self):
        self.list=[] 
        self.bizimargumnt=6 
        print(f"{list} {self.bizimargumnt} yarandi")

    def ekle(self,a):
        self.list=a
        print(self.list)
        print(self.bizimargumnt)

    def ededlerintoplami(self):
        b=False
        for i in range(len(self.list)):
            for j in range(i+1,len(self.list)):
                if(self.list[i]+self.list[j]==self.bizimargumnt):
                    print(f"{i}  ve {j} indeksleri cemi veriyin edede beraberdir")
                    b=True
        if b==False:
            print(-1)
   

cl=numune()
cl.ekle(listimiz)
cl.ededlerintoplami()