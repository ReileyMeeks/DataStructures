//ReileyMeeks
//LinkedList in swift

import Foundation

class Node<T> {
    var value: T
    var next: Node?
    
    init(value: T) {
        self.value = value
    }
}

class LinkedList<T> {
    var head: Node<T>?
    
    // Method to insert a value at the end of the linked list
    func append(value: T) {
        let newNode = Node(value: value)
        
        if head == nil {
            head = newNode
        } else {
            var currentNode = head
            while currentNode?.next != nil {
                currentNode = currentNode?.next
            }
            currentNode?.next = newNode
        }
    }
    
    // Method to print the linked list
    func printList() {
        var currentNode = head
        while currentNode != nil {
            print(currentNode!.value)
            currentNode = currentNode?.next
        }
    }
}

// Testing the linked list
let list = LinkedList<Int>()
list.append(value: 10)
list.append(value: 20)
list.append(value: 30)
list.printList()

