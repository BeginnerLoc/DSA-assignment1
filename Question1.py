# Luke

class Node:
    def __init__(self, data=None):
        self.data: int = data
        self.next: Node = None
        
class LinkedList:
    tail: Node = None
    head: Node = None
    def __init__(self):
        self.head | None = None 
        self.tail | None = None
        
    def add(self, data):    
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
            
    def add_index(self, index, data):
        new_node = Node(data)
        prev_node = node_array[index-1]
        prev_node.next = new_node
        
            
            
node_array = []
ll = LinkedList()
ll.add(1)
node_array.append(1)
ll.add(2)
node_array.append(2)
ll.add(3)
node_array.append(3)