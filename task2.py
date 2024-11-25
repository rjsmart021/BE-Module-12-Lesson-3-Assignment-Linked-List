# Task 1
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# Task 2

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def delete_node(self, key):
        temp = self.head

        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                if self.head:
                    self.head.prev = None
                temp = None
                return

        while temp is not None:
            if temp.data == key:
                break
            temp = temp.next

        if temp is None:
            return

        if temp.next:
            temp.next.prev = temp.prev

        if temp.prev:
            temp.prev.next = temp.next

        temp = None

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")


# Task 3

if __name__ == "__main__":
    dll = DoublyLinkedList()
    
    # Inserting elements
    dll.insert_at_end(1)
    dll.insert_at_end(2)
    dll.insert_at_end(3)
    dll.insert_at_end(4)
    
    # Traversing the list
    print("Doubly Linked List after insertion:")
    dll.traverse()
    
    # Deleting a node
    dll.delete_node(2)
    
    # Traversing the list again
    print("Doubly Linked List after deletion of 3:")
    dll.traverse()
