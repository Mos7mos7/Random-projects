class comp:
    def __init__(self):
        print("Hello to complex number")

    def change(self,num):
        if num.find("+")!=-1 :
            real=float(num.split("+i")[0])
            img=float(num.split("+i")[1])
        else :
            real=float(num.split("-i")[0])
            img=-float(num.split("-i")[1])
        return[real,img]
    def add(self,num1,num2):
        r1=self.change(num1)[0]
        i1=self.change(num1)[1]
        r2=self.change(num2)[0]
        i2=self.change(num2)[1]
        resr=r1+r2
        resi=i1+i2
        if resi >0 :
                    print("add is "+str(resr)+" +i"+str(resi))
        else :
                    print("add is "+str(resr)+" -i"+str(resi))


    def subtract(self,num1,num2):
        r1=self.change(num1)[0]
        i1=self.change(num1)[1]
        r2=self.change(num2)[0]
        i2=self.change(num2)[1]
        resr=r1-r2
        resi=i1-i2
        if resi >0 :
                    print("subtract is "+str(resr)+" +i"+str(resi))
        else :
                    print("subtract is "+str(resr)+" -i"+str(resi))

    def divide(self,num1,num2):
        r1=self.change(num1)[0]
        i1=self.change(num1)[1]
        r2=self.change(num2)[0]
        i2=self.change(num2)[1]
        resr=(r1*r2 - i1*i2)/(r2*r2 + i2*i2)
        resi=(r1*i2 + r2*i1)/(r2*r2 + i2*i2)
        if resi >0 :
                    print("subtract is "+str(resr)+" +i"+str(resi))
        else :
                    print("subtract is "+str(resr)+" -i"+str(resi))
    def multiply(self,num1,num2):
        r1=self.change(num1)[0]
        i1=self.change(num1)[1]
        r2=self.change(num2)[0]
        i2=self.change(num2)[1]
        resr=r1*r2 - i1*i2
        resi=r1*i2 + r2*i1
        if resi >0 :
                    print("subtract is "+str(resr)+" +i"+str(resi))
        else :
                    print("subtract is "+str(resr)+" -i"+str(resi))

cmp=comp()
cmp.add("2+i2","2+i2")
#simple script to deal with complex nums
