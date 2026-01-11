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

    # Print the linked list
    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    # Delete the head node
    def deleteHead(self):
        if self.head is None:
            print("List is empty, cannot delete.")
            return
        temp = self.head
        self.head = self.head.next
        temp = None

    # Delete the tail node
    def deleteTail(self):
        if self.head is None:
            print("List is empty, cannot delete.")
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None

    # Delete a node at a specific position (1-indexed)
    def deleteAtPosition(self, position):
        if self.head is None:
            print("List is empty, cannot delete.")
            return
        if position == 1:
            temp = self.head
            self.head = self.head.next
            temp = None
            return
        temp = self.head
        for i in range(1, position - 1):
            if temp is None:
                print("Position out of bounds.")
                return
            temp = temp.next
        if temp is None or temp.next is None:
            print("Position out of bounds.")
            return
        nodeToDelete = temp.next
        temp.next = temp.next.next
        nodeToDelete = None

# Driver code
if __name__ == "__main__":
    list = LinkedList()

    # Insert nodes
    list.insertAtBeginning(5)
    list.insertAtBeginning(10)
    list.insertAtBeginning(15)

    print("Original Linked List:", end=" ")
    list.printList()  # Output: 15 10 5

    # Delete at position 2 (1-indexed)
    list.deleteAtPosition(2)
    print("Linked List after deleting at position 2:", end=" ")
    list.printList()  # Output: 15 5

    # Delete head
    list.deleteHead()
    print("Linked List after deleting head:", end=" ")
    list.printList()  # Output: 5

    # Delete tail (last remaining node)
    list.deleteTail()
    print("Linked List after deleting tail:", end=" ")
    list.printList()  # Output: List is empty