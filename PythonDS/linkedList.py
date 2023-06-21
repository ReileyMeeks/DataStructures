#Linked List in Python

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def display(self):
        if self.head is None:
            print("Linked list is empty.")
        else:
            current = self.head
            while current is not None:
                print(current.data, end=" ")
                current = current.next
            print()


# Example usage:
my_list = LinkedList()
my_list.append(5)
my_list.append(10)
my_list.append(15)
my_list.display()
