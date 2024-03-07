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
        data=self.head.data

        self.head=self.head.next
        self.count-=1
        return data
    
    def peek(self):
        print(self.head.data)
        return
    
    def isempty(self):
        if self.head is None:
            return True
        return False
    
    def size(self):
        print(self.count)
        return
    



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
        print(self.head.data)
        return
        
    def size(self):
        print(self.count)
        return




        

def main():
    s1=MyStack()
    s1.push(7)
    s1.push(2)
    s1.push(3)
    s1.display()
    # s1.pop()
    # print('\nAfter popping an element from stack')
    # s1.display()
    s1.peek()
    print()
    # s1.size()


    q1=MyQueue()
    q1.enqueue(1)
    q1.enqueue(2)
    q1.enqueue(3)
    q1.display()
    q1.peek()
    print(" ")
    # q1.dequeue()
    # q1.display()


main()

