class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        result = []
        while current is not None:
            result.append(f"{current.data}-->")
            current = current.next
        print(result)
    
    def insert(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node # head points to new_node
            return 
        
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node # connects to new_node , Placing new_node address in the last node 

    def length_of_linkedlist(self):
        count = 0
        current = self.head
        while current is not None:
            current = current.next
            count += 1
        return count
    
    def delete(self,data):
        current = self.head
        if current and current.data == data:
            self.head = self.head.next
            current = None
            return
        
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next



        if current is None:
            return
        
        prev.next = current.next
        current = None
        
    def insert_at_specific_position(self,position,data):
        current = self.head
        if position == 1:
            new_node = Node(data)
            new_node.next = self.head # new node connects with the head node
            self.head = new_node # Both head and new_node points to first node
            return
    
        count = 1
        while current and count < position - 1:
            current = current.next
            count += 1
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node
        


        


linkedlist = SinglyLinkedList()
linkedlist.insert(10)
linkedlist.insert(20)
linkedlist.insert(30)
linkedlist.insert(40)
linkedlist.insert(50)
linkedlist.insert(60)
linkedlist.display()
  


linkedlist.delete(10) # delete head node
linkedlist.display()


linkedlist.delete(60) # delete last node
linkedlist.display()


linkedlist.delete(40)
linkedlist.display() # delete specific node


linkedlist.insert_at_specific_position(1 , 15)
linkedlist.display()

linkedlist.insert_at_specific_position(3,25)
linkedlist.display()
