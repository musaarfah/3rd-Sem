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

    def insert_at_end(self,data):
        new_node=Node(data)

        current=self.head
        while current.ref is not None:
            current=current.ref
        current.ref=new_node

    def insert_after(self,key,data):
        new_node=Node(data)

        current=self.head
        while current is not None:
            if current.data==key:
                new_node.ref=current.ref
                current.ref=new_node
                break
            current=current.ref

    def insert_before(self,key,data):
        new_node=Node(data)
        

        current=self.head
        while current.ref is not None:
            if current.ref.data==key:
                new_node.ref=current.ref
                current.ref=new_node
                break
            current=current.ref

    def search(self,key):
        if self.head is None:
            print('List is empty')

        else:
            current=self.head
            while current is not None:
                if current.data==key:
                    return True
                current=current.ref

            return False



    def print_llist(self):
        if self.head is None:
            print('Linked List is empty')

        else:
            current=self.head
            while current is not None:
                print(current.data,end=' ')
                current=current.ref

    def remove_at_start(self):
        if self.head is None:
            return 'List is empty'
        current=self.head
        self.head=current.ref
        del current

    def remove_at_end(self):
        if self.head is None:
            return
        current=self.head
        current1=self.head
        while current.ref is not None:
            current1=current
            current=current.ref
        current1.ref=None

        del current

    def remove_before(self,key):
        if self.head is None:
            return
        current =self.head
        current1=self.head
        while current is not None:
            if current.ref.data==key:
                del current
                break





        
def main():
    l1=LinkedList()
    l1.insert_at_start(10)
    l1.insert_at_start(20)
    l1.insert_at_start(30)
    l1.insert_at_end(5)
    l1.insert_after(10,15)
    l1.insert_before(10,12)
    # l1.remove_at_end()
    # l1.remove_at_start()
    # print(l1.search(12))
    l1.print_llist()

main()