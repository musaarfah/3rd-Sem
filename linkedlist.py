class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_start(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.ref=self.head
            self.head=new_node

    def print_llist(self):
        if self.head is None:
            print('Linked List is empty')

        else:
            current=self.head
            print(current)
            while current is not None:
                print(current.data,end=' ')
                current=current.ref


        
def main():
    l1=LinkedList()
    l1.insert_at_start(10)
    l1.print_llist()