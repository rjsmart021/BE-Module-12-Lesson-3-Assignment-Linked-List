#Task 1

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Task 2

class SinglyLinkedList:
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

    def delete_node(self, key):
        temp = self.head

        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return

        prev.next = temp.next
        temp = None

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Task 3

if __name__ == "__main__":
    sll = SinglyLinkedList()
    
    # Inserting elements
    sll.insert_at_end(1)
    sll.insert_at_end(2)
    sll.insert_at_end(3)
    sll.insert_at_end(4)
    
    # Traversing the list
    print("Linked List after insertion:")
    sll.traverse()
    
    # Deleting a node
    sll.delete_node(3)
    
    # Traversing the list again
    print("Linked List after deletion of 3:")
    sll.traverse()
