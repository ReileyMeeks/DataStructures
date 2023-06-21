//Stack in swift

import Foundation

struct Stack<T> {
    private var elements = [T]()
    
    mutating func push(_ element: T) {
        elements.append(element)
    }
    
    mutating func pop() -> T? {
        return elements.popLast()
    }
    
    func peek() -> T? {
        return elements.last
    }
    
    func isEmpty() -> Bool {
        return elements.isEmpty
    }
    
    func count() -> Int {
        return elements.count
    }
}

//Test
var stack = Stack<Int>()
stack.push(1)
stack.push(27)
stack.push(3)

//stack: 1, 27, 3
//top: 3
stack.count() // 3
stack.peek() // 3
stack.pop() // 3
stack.pop() // 27
stack.count() // 1
stack.isEmpty() // false
stack.pop() // 1
stack.isEmpty() // true
