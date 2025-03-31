class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode

    def display(self):
        if not self.head:
            return "Empty list"
        current, result = self.head, ""
        while current:
            result += str(current.data) + " -> "
            current = current.next
        return result + "None"

# Caso de prueba
my_list = LinkedList()
my_list.insertAtEnd(10)
my_list.insertAtEnd(20)
my_list.insertAtEnd(30)
print(my_list.display())  # Esperado: "10 -> 20 -> 30 -> None"
