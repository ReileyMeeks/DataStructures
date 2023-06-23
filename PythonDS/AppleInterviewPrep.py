#Array's
def find_three_integers(array, target_sum):
    n = len(array)
    
    # Sort the array in ascending order
    array.sort()
    
    # Iterate over each element as the first number in the triplet
    for i in range(n - 2):
        left = i + 1   # Pointer for the second number
        right = n - 1  # Pointer for the third number
        
        while left < right:
            current_sum = array[i] + array[left] + array[right]
            
            # Check if the sum matches the target sum
            if current_sum == target_sum:
                return True  # Found a triplet
                
            elif current_sum < target_sum:
                left += 1  # Increment left pointer for a larger sum
            
            else:
                right -= 1  # Decrement right pointer for a smaller sum
    
    return False  # No triplet found

# Example usage:
arr = [1, 4, 2, 8, 3, 9, 5]
target = 19

result = find_three_integers(arr, target)
print(result)  # Output: True

def merge_intervals(intervals):
    # Sort intervals based on the start time
    intervals.sort(key=lambda x: x[0])
    
    merged = []
    
    for interval in intervals:
        # If the merged list is empty or the current interval does not overlap with the previous interval
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
        else:
            # Update the end time of the last interval in the merged list
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged

# Example usage:
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
merged_intervals = merge_intervals(intervals)
print(merged_intervals)  # Output: [[1, 6], [8, 10], [15, 18]]

#LinkedLists
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers(l1, l2):
    dummy = ListNode(0)  # Dummy node to store the result
    current = dummy      # Pointer to traverse the result linked list
    carry = 0            # Carry value for addition
    
    while l1 or l2 or carry:
        sum = carry
        
        if l1:
            sum += l1.val
            l1 = l1.next
        
        if l2:
            sum += l2.val
            l2 = l2.next
        
        carry = sum // 10
        digit = sum % 10
        
        current.next = ListNode(digit)
        current = current.next
    
    return dummy.next

# Example usage:
# Create the first linked list: 2 -> 4 -> 3
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

# Create the second linked list: 5 -> 6 -> 4
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = add_two_numbers(l1, l2)

# Traverse the resulting linked list and print the values
while result:
    print(result.val)
    result = result.next

# Output: 7 -> 0 -> 8

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    dummy = ListNode(0)  # Dummy node to store the result
    current = dummy      # Pointer to traverse the result linked list
    
    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        
        current = current.next
    
    # Attach the remaining nodes from l1 or l2, if any
    current.next = l1 or l2
    
    return dummy.next

# Example usage:
# Create the first sorted linked list: 1 -> 2 -> 4
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

# Create the second sorted linked list: 1 -> 3 -> 4
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

result = merge_two_lists(l1, l2)

# Traverse the resulting linked list and print the values
while result:
    print(result.val)
    result = result.next

# Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4

#Trees
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_same_tree(p, q):
    if p is None and q is None:
        return True
    
    if p is None or q is None:
        return False
    
    if p.val != q.val:
        return False
    
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

# Example usage:
# Create the first binary tree:
#     1
#    / \
#   2   3
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

# Create the second binary tree:
#     1
#    / \
#   2   3
q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

result = is_same_tree(p, q)
print(result)  # Output: True

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def swap_children(root):
    if root is None:
        return None
    
    # Swap the left and right children of the current node
    root.left, root.right = root.right, root.left
    
    # Recursively swap the children for the left and right subtrees
    swap_children(root.left)
    swap_children(root.right)
    
    return root

# Example usage:
# Create the binary tree:
#      1
#     / \
#    2   3
#   / \   \
#  4   5   6
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

# Swap the children for each node in the tree
swapped_root = swap_children(root)

# Perform a breadth-first traversal to verify the swap
queue = [swapped_root]
while queue:
    node = queue.pop(0)
    print(node.val)
    if node.left:
        queue.append(node.left)
    if node.right:
        queue.append(node.right)

# Output: 1, 3, 2, 6, 5, 4

#Strings
def find_palindromic_substrings(string):
    def is_palindrome(substring):
        return substring == substring[::-1]

    palindromes = []
    n = len(string)

    for i in range(n - 1):
        for j in range(i + 2, n + 1):
            substring = string[i:j]
            if is_palindrome(substring) and len(substring) > 1:
                palindromes.append(substring)

    return palindromes

# Example usage:
input_string = "abcbaabccba"
result = find_palindromic_substrings(input_string)
print(result)  # Output: ['abcba', 'bcb', 'cbaabc']

def reverse_words(sentence):
    # Reverse the entire sentence
    sentence.reverse()
    
    start = 0
    for end in range(len(sentence)):
        if sentence[end] == ' ':
            # Reverse each word
            reverse_word(sentence, start, end - 1)
            start = end + 1
    
    # Reverse the last word
    reverse_word(sentence, start, len(sentence) - 1)
    
    return sentence

def reverse_word(sentence, start, end):
    while start < end:
        sentence[start], sentence[end] = sentence[end], sentence[start]
        start += 1
        end -= 1

# Example usage:
input_sentence = list("Hello, world!")
result = reverse_words(input_sentence)
print(''.join(result))  # Output: "world! Hello," (reversed order of words)

#Dynamic Programming
def find_max_sum_subarray(arr, k):
    window_sum = 0
    max_sum = 0

    # Calculate the sum of the first 'k' elements
    for i in range(k):
        window_sum += arr[i]

    # Update the maximum sum
    max_sum = window_sum

    # Slide the window and update the maximum sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum

# Example usage:
input_array = [2, 1, 5, 1, 3, 2]
k = 3
result = find_max_sum_subarray(input_array, k)
print(result)  # Output: 9 (maximum sum of subarray [5, 1, 3])

#Backtracking
def print_combinations(target):
    def backtrack(remain, current_combination, start):
        if remain == 0:
            print(current_combination)
            return
        if remain < 0:
            return

        for i in range(start, target + 1):
            current_combination.append(i)
            backtrack(remain - i, current_combination, i)
            current_combination.pop()

    backtrack(target, [], 1)

# Example usage:
target = 5
print_combinations(target)

#Graphs
class Node:
    def __init__(self, val=None):
        self.val = val
        self.neighbors = []

def clone_graph(node):
    if node is None:
        return None

    visited = {}

    def dfs(original_node):
        if original_node in visited:
            return visited[original_node]

        clone_node = Node(original_node.val)
        visited[original_node] = clone_node

        for neighbor in original_node.neighbors:
            clone_neighbor = dfs(neighbor)
            clone_node.neighbors.append(clone_neighbor)

        return clone_node

    return dfs(node)

# Example usage:
# Create the original graph:
#   1 --> 2
#   |     |
#   v     v
#   3 --> 4
original_node1 = Node(1)
original_node2 = Node(2)
original_node3 = Node(3)
original_node4 = Node(4)
original_node1.neighbors = [original_node2, original_node3]
original_node2.neighbors = [original_node4]
original_node3.neighbors = [original_node4]

# Clone the graph
cloned_node = clone_graph(original_node1)

# Perform a breadth-first traversal to verify the cloning
queue = [cloned_node]
visited = set()

while queue:
    node = queue.pop(0)
    print(node.val)
    visited.add(node)
    for neighbor in node.neighbors:
        if neighbor not in visited:
            queue.append(neighbor)

# Output: 1, 2, 3, 4 (cloned graph traversal)

#Sorting/Search
def search_rotated_array(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid

        # Check if the left half is sorted
        if arr[start] <= arr[mid]:
            if arr[start] <= target < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        # Otherwise, the right half is sorted
        else:
            if arr[mid] < target <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1

    return -1

# Example usage:
input_array = [4, 5, 6, 7, 0, 1, 2]
target = 0
result = search_rotated_array(input_array, target)
print(result)  # Output: 4 (index of the target number)

def merge_intervals(intervals):
    # Sort the intervals based on the start time
    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        # If the merged list is empty or the current interval does not overlap with the last interval in the merged list,
        # add the current interval to the merged list
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
        else:
            # Otherwise, there is an overlap, so merge the current interval with the last interval in the merged list
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged

# Example usage:
input_intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
result = merge_intervals(input_intervals)
print(result)  # Output: [[1, 6], [8, 10], [15, 18]] (merged intervals)

