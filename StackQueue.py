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



def paranthesesBalancecheck(string):
    dt=MyStack()
    for i in range(len(string)):
        if string[i]=='{' or string[i]=='[' or string[i]=='(' :
            dt.push(string[i])

        elif string[i]=='}' or string[i]==']' or string[i]==')' :
            dt.pop()

    if not dt.isempty():
        return  False
    else:
        return True
    
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
    
def reverse_stack(stack):
        reversed_st=MyStack()

        for i in range(stack.size()):
            reversed_st.push(stack.pop())
            

        return reversed_st


def main():
    s1=MyStack()
    s1.push(7)
    s1.push(2)
    s1.push(3)
    s1.display()
    # # s1.pop()
    # # print('\nAfter popping an element from stack')
    # # s1.display()
    # s1.peek()
    # print()
    # # s1.size()
    print('\n After Reverse')

    s2=reverse_stack(s1)
    s2.display()


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
    
    # print(paranthesesEQUATIONcheck('[2+{3-(4*9)}]'))


main()

