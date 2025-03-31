class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def get_next(self):
        return self.next

    def set_next(self, next_node):
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0  # Asegurar que length esté definido

    def insert_at_end(self, data):
        
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            
            while current.get_next() is not None:
                current = current.get_next()
            
            current.set_next(new_node)
        
        self.length += 1
        return True

    def display(self):
        if not self.head:
            return "Empty list"
        current, result = self.head, ""
        while current:
            result += str(current.data) + " -> "
            current = current.get_next()
        return result + "None"

my_list = LinkedList()
my_list.insert_at_end(5)
my_list.insert_at_end(10)
my_list.insert_at_end(15)

print(my_list.display())
