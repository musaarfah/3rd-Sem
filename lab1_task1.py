class Term:
    def __init__(self,var,coeff,pow):
        self.var=var
        self.coeff=coeff
        self.pow=pow

    def __str__(self):
        return f"{self.coeff}{self.var}^{self.pow}"
    

class Polynomial:
    def __init__(self):
        self.terms=[]

    def addTerms(self,coeff,pow):
        term=Term('x',coeff,pow)
        self.terms.append(term)

    def getDegree(self):
        degrees=[]
        for i in range(len(self.terms)):
            degrees.append(self.terms[i].pow)
        degree=max(degrees)
        print(degree)

    def getCoeff(self,power):
        for i in range(len(self.terms)):
            if self.terms[i].pow==power:
                print(self.terms[i].coeff)

    def evaluate(self,value):
        terms=0
        for i in range(len(self.terms)):
          
            x =(self.terms[i].coeff)
            y =value ** (self.terms[i].pow)
            
            v=x * y
            terms +=v
        
           

        
        print(terms)

    def __add__(self,p2):
        pass

    def derivative(self):
        new_terms=[]
        for i in range(len(self.terms)):
            z=self.terms[i].coeff*self.terms[i].pow
            powerr=self.terms[i].pow-1

            new=Term('x',z,powerr)
            new_terms.append(new)

        stringg=''
        for i in range(len(new_terms)):
            if new_terms[i].pow==0:
                stringg+=f"+ {new_terms[i].coeff}"
            elif new_terms[i].pow==1:
                stringg+=f"+{new_terms[i]}x"
            elif new_terms[i].pow>1:
                stringg+=f" + {new_terms[i]}"

        print(stringg)

    def clear(self):
        new_t=[]
        for i in range(len(self.terms)):
            neww=Term('x',0,self.terms[i].pow)
            new_t.append(neww)

        stringgg=''
        for i in range(len(new_t)):
            if new_t[i].pow==0:
                stringgg+=f"+ {new_t[i].coeff}"
            elif new_t[i].pow==1:
                stringgg+=f"+{new_t[i]}x"
            elif new_t[i].pow>1:
                stringgg+=f" + {new_t[i]}"

        print(stringgg)

    def set_coeff(self,new_coeff,new_pow):
        for i in range(len(self.terms)):
            term = self.terms[i]
            if term.pow == new_pow:
                term.coeff = new_coeff
        print ('Set')

        
    def __mul__(self):
        pass
    def __sub__(self):
        pass
    def __antiDer__(self):
        pass




        
    def __str__(self):
        string=''
        for i in range(len(self.terms)):
            if self.terms[i].pow==0:
                string+=f"+ {self.terms[i].coeff}"
            elif self.terms[i].pow==1:
                string+=f"+{self.terms[i]}x"
            elif self.terms[i].pow>1:
                string+=f" + {self.terms[i]}"

        return string
        

p1=Polynomial()
p1.addTerms(4,5)
p1.addTerms(7,3)
p1.addTerms(-1,2)
p1.addTerms(9,0)

# print(p1)
# p1.getDegree()
# p1.getCoeff(3)

# p1.evaluate(2)

# p1.derivative()

# p1.clear()

# p1.set_coeff(8,8)