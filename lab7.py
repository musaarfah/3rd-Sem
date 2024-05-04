class HashTable:
    def __init__(self, size):
        self.table = [None] * size
        self.size=size
        self.n=0

    def isEmpty(self):
        if self.n==0:
            return True
        return False
    
    def isFull(self):
        if self.n==self.size:
            return True
        return False
    
    def loadFactor(self):
        return (self.n/self.size)
    
    def __del__(self):
        print('Del implemented')

    

    def getHashValue(self, name):
        temp = 0
        for char in name:
            temp += ord(char)
        index=temp % self.size
        return index
    
    def insert(self,name):
        hashh=self.getHashValue(name)

        if self.isFull():
            return False
        
        else:

            if self.table[hashh] is None:
                self.table[hashh]=name
                self.n+=1
            else:
                index=hashh+1


                while self.table[hashh] is not None and index<self.size:

    
                    if self.table[index] == None:
                        self.table[index]=name
                        self.n+=1
                        return True
                    index+=1

    def search(self,name):
        seq=[]

        index=self.getHashValue(name)
        
  
        
        while self.table[index] is not None and index<self.size:
            seq.append(index)
            if self.table[index]==name:
                print(seq)
                return True
            index+=1

    def remove(self,name):
        index=self.getHashValue(name)

        while self.table[index] is not None and index<self.size:
            if self.table[index]==name:
                self.n-=1
                self.table[index]=None
                return True
            index+=1
        
        
        


    def print(self):
        for i in range(self.size):
            if self.table[i] is None:
                print('empty',end=' ')
            else:
                print(f'{self.table[i]} : {self.table.index(self.table[i])}',end=' ' )


def main():
    # hash1=HashTable(6)


    # hash1.insert('ali')
    # hash1.insert('ahmad')
    # hash1.insert('hussain')
    # hash1.print()
    # print(' ')
    # # print(hash1.search('ali'))
    # hash1.remove('ali')
    # hash1.print()

    size=int(input('Enter Size:'))

    hash1=HashTable(size)
    valid_options={'i','d','dl','s','r','q'}

    while True:
        print(f'i)insert\ts)search\td)Display\tdl)Display Load Factor\tr)Remove\tq)Quit')

        user_input=input('Enter Operation :')
        if user_input not in valid_options:
            print('Choose from valid option')
            print(f'i)insert\ts)search\td)Display\tdl)Display Load Factor\tr)Remove\tq)Quit')

    
        

        if user_input=='s':
            name=input('Enter Name:')
            hash1.search(name)


        if user_input=='i':
            name=input('Enter Name:')
            hash1.insert(name)

        if user_input=='d':
            hash1.print()
            print(' ')

        if user_input=='dl':
            print(hash1.loadFactor())

        if user_input=='r':
            name=input('Enter Name:')
            hash1.remove(name)

        if user_input=='q':
            break
        

main()
                

                        

                