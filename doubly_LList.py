class Node:
    def __init__(self,data) :
        self.data = data
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self,values=None) -> None:
        self.head = None
        self.tail=None

        if values is not None:
            if isinstance(values,(list,tuple,set)):
                for value in values:
                    self.insert_at_tail(value)
            else:
                self.insert_at_tail(values)


    def print_dll(self):
        if self.head is None:
            print('Linked List is Empty')
        else:
            current=self.head
            while current is not None:
                print(current.data,end=' ')
                current=current.next
            print()

    
    def insert_at_head(self,data):
        new_node=Node(data)

        if self.head is None:
            self.head=self.tail=new_node
            return
        else:
            self.head.prev=new_node
            new_node.next=self.head
            self.head=new_node


    
    def insert_at_tail(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=self.tail=new_node
            return
        else:
            new_node.prev=self.tail
            self.tail.next=new_node
            self.tail=new_node

    
    def insert_after(self,key,data):
        if self.head is None:
            print('List is Empty')
            return
        elif self.head is not None:
            new_node=Node(data)
            current=self.head

            while current is not None:
                if current.data == key:
                    new_node.prev=current
                    new_node.next=current.next
                    if current.next is not None:
                        current.next.prev=new_node
                    else:
                        self.tail=new_node
                    current.next=new_node
                current=current.next
        else:
            print('Key Not in List')
            return
        
    
    def insert_before(self,key,data):
        if self.head is None:
            print('List is empty')
            return
        elif self.head is not None:
            new_node=Node(data)
            current=self.head

            while current is not None:
                if current.data == key:
                    new_node.next=current
                    new_node.prev=current.prev
                    if current.prev is not None:
                        current.prev.next=new_node
                    else:
                        self.head=new_node
                    current.prev=new_node
                current=current.next

        else:
            print('Key Not found')
            return
        
    def remove_at_head(self):
        current=self.head

        self.head.prev=None
        self.head=self.head.next

        del current

    def remove_at_tail(self):
        current = self.tail

        self.tail=self.tail.prev
        self.tail.next=None

        del current

    def remove_before(self,key):
        if self.head is None:
            print('List is empty')
            return
        
        elif self.head.data==key:
            print('cant remove before first node')
            return
        
        
        elif self.head is not None:
            current=self.head.next
            while current is not None:
                if current.data==key:
                        current.prev=current.prev.prev
                        if current.prev is not None:
                            current.prev.next=None
                        else:
                            self.head=current

                current=current.next
        else:
            print('Key not found')
            return





def main():
    l1=DoublyLinkedList([2,3,4,5])
    
    l1.insert_at_head(1)
    l1.insert_at_tail(6)
    l1.insert_after(6,9)
    # l1.insert_before(1,17)
    l1.print_dll()
    # l1.remove_at_head()
    # l1.remove_at_tail()
    l1.remove_before(4)
    l1.print_dll()


main()


    




