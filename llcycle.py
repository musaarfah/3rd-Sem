class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self,values=None):
        self.head=None
        

        if values is not None:
            if isinstance(values, (list, tuple, set)):
                for value in values:
                    self.insert_at_end(value)
            else:
                self.insert_at_end(values)





    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            new_node.next=self.head
        else:
            curr=self.head

            while curr.next != self.head:
                curr=curr.next

            curr.next=new_node
            new_node.next=self.head



    def display(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        print("Circular Linked List:")
        while True:
            print(current.data, end=" ")
            current = current.next
            if current == self.head:
                break
        print()


def main():
    l1=LinkedList([1,2,3,4,5])
    l2=LinkedList([6,7,8,9,9,10])
    l1.print_llist()




    


main()