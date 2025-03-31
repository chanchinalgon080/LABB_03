class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_next(self):
        return self.next
    
    def set_next(self, next_node):
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(new_node)
        self.length += 1

    def insert_at_position(self, position, data):
        if position < 0 or position > self.length:  
            return False
        
        new_node = Node(data)
        
        if position == 0:
            new_node.set_next(self.head)
            self.head = new_node
        elif position == self.length:
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(new_node)
        else:
            current = self.head
            for _ in range(position - 1):
                current = current.get_next()
            new_node.set_next(current.get_next())
            current.set_next(new_node)
        
        self.length += 1
        return True

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.get_next()
        print("None")

linked_list = LinkedList()
linked_list.add_node(10)
linked_list.add_node(20)
linked_list.add_node(30)

print("Lista original:")
linked_list.print_list()  


linked_list.insert_at_position(3, 40)
print("Lista después de insertar 40 en la posición 3 (final):")
linked_list.print_list()  
