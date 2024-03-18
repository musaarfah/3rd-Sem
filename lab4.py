class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class MyStack:
    def __init__(self):
        self.head=None
        self.count=0

    def display(self):
        if not self.head:
            print('stack is empty')
            return
        curr=self.head
        while curr:
            print(curr.data,end=' ')
            curr=curr.next

    
    def push(self,data):
        newNode = Node(data)
        newNode.next=self.head
        self.head=newNode
        self.count+=1

    def pop(self):
        if not self.isempty():
            data=self.head.data

            self.head=self.head.next
            self.count-=1
            return data
        else:
            return('Empty stack')
    
    def peek(self):
        return self.head.data
        
    
    def isempty(self):
        if self.head is None:
            return True
        return False
    
    def size(self):
        return self.count
    
class MyQueue:
    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0

    def display(self):
        if not self.head:
            print('stack is empty')
            return
        curr=self.head
        while curr:
            print(curr.data,end=' ')
            curr=curr.next


    def  enqueue(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=self.tail=newNode
            self.count+=1
        
        else:
            self.tail.next=newNode
            self.tail=newNode
            self.count+=1

    def dequeue(self):
        if self.head is None:
            print('Queue is empty')
            return
        
        else:
            data=self.head.data
            self.head=self.head.next
            self.count-=1

            return data
        
    def peek(self):
         return self.head.data
        
    def size(self):
        print(self.count)
        return
    
class ListBaseCircularQueue:
    def __init__(self, size):
        self.size = size
        self.head = self.tail = 0
        self.count = 0
        self.queue = [] * size

    def enqueue(self, data):
        if self.count == self.size:
            raise IndexError("CircularQueue is full")

        self.queue.append(data)
        self.tail = (self.tail + 1) % self.size
        self.count += 1

    def dequeue(self):
        if not self.queue or self.count == 0:
            raise IndexError("CircularQueue is empty")
        

        dequeued_data = self.queue[0]
        self.queue=self.queue[1:]
       
        self.count -= 1

        return dequeued_data

    def isempty(self):
        return self.count == 0

    def size(self):
        return self.count

    def display(self):
        if not self.queue or self.count == 0:
            print("CircularQueue is empty")
            return

        for i in range(len(self.queue)):
            if self.queue[i] is not None:
                print(self.queue[i],end=' ')

        print()

class CircularQueue:
    def __init__(self,size):
        self.size=size
        self.head=None
        self.tail=None
        self.count=0

    def display(self):
        if not self.head:
            print('stack is empty')
            return
        
        curr=self.head
        print(curr.data,end=' ')
        curr=curr.next
        while curr!=self.head and curr is not None:
            print(curr.data,end=' ')
            curr=curr.next

    


    def enqueue(self,data):
        newNode=Node(data)

        if self.head is None:
            self.head=self.tail=newNode

        else:
            if self.size<=self.count:
                self.tail.next=newNode
                newNode.next=self.head
                self.tail=newNode
                self.count+=1
            else:
                return('Stack is full')


        

        

def paranthesesEQUATIONcheck(string):
    opening_parantheses = '[{('
    closing_parantheses = ')]}'
    
    pair = {')': '(', ']': '[', '}': '{'}
    dt = MyStack()

    for i in range(len(string)):
        if string[i] in opening_parantheses:
            dt.push(string[i])

        elif string[i] in closing_parantheses:
            if not dt.isempty() and dt.peek() == pair[string[i]]:
                dt.pop()
            else:
                return False

    if not dt.isempty():
        return False
    else:
        return True
    

def reverse_string(string):
    word=string.split()
    for i in range(len(word)):
        dt=MyStack()
        for j in range(len(word[i])):
            dt.push(word[i][j])
        for k in range(dt.size()):
            print(dt.pop(),end='')
        print(end=" ")
    
def main():
    # s1=MyStack()
    # s1.push(7)
    # s1.push(2)
    # s1.push(3)
    # s1.display()
    # # s1.pop()
    # # print('\nAfter popping an element from stack')
    # # s1.display()
    # s1.peek()
    # print()
    # # s1.size()
    # print('\n After Reverse')



    # q1=MyQueue()
    # q1.enqueue(1)
    # q1.enqueue(2)
    # q1.enqueue(3)
    # q1.display()
    # q1.peek()
    # print(" ")
    # # q1.dequeue()
    # # q1.display()

    # print(paranthesesBalancecheck('{[()}'))
    
    # print(paranthesesEQUATIONcheck('(faiq))'))

    # reverse_string('Welcome to DSA')


    q2=ListBaseCircularQueue(9)
    q2.enqueue(5)
    q2.enqueue(6)
    q2.enqueue(7)
    q2.display()

  

main()