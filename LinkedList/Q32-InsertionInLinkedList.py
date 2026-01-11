class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning of the linked list
    def insertAtBeginning(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode

    # Insert at the end of the linked list
    def insertAtEnd(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = newNode

    # Insert at a specific position in the linked list (1-indexed)
    def insertAtPosition(self, value, position):
        newNode = Node(value)
        if position == 1:
            newNode.next = self.head
            self.head = newNode
            return
        temp = self.head
        for i in range(1, position - 1):
            if temp is None:
                print("Position out of bounds.")
                return
            temp = temp.next
        if temp is None:
            print("Position out of bounds.")
            return
        newNode.next = temp.next
        temp.next = newNode

    # Print the linked list
    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()

# Driver code
if __name__ == "__main__":
    list = LinkedList()

    # Insert at beginning
    list.insertAtBeginning(5)
    list.insertAtBeginning(10)
    list.insertAtBeginning(15)

    print("Linked List after inserting at beginning:", end=" ")
    list.printList()  # Output: 15 10 5

    # Insert at end
    list.insertAtEnd(20)
    list.insertAtEnd(25)

    print("Linked List after inserting at end:", end=" ")
    list.printList()  # Output: 15 10 5 20 25

    # Insert at position
    list.insertAtPosition(12, 2)  # Inserting 12 at position 2 (1-indexed)
    print("Linked List after inserting at position 2:", end=" ")
    list.printList()  # Output: 15 12 10 5 20 25