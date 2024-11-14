# test_data_structures.py
import unittest
from data_structures import BinarySearchTree, HashTable, Stack, Queue
from sorting_algorithms import bubble_sort, merge_sort, binary_search

class TestDataStructures(unittest.TestCase):
    def test_binary_search_tree(self):
        bst = BinarySearchTree()
        test_values = [5, 3, 7, 1, 9, 4, 6]
        
        # Test insertion
        for value in test_values:
            bst.insert(value)
        
        # Test in-order traversal
        self.assertEqual(bst.inorder_traversal(), [1, 3, 4, 5, 6, 7, 9])
    
    def test_hash_table(self):
        ht = HashTable()
        
        # Test insertion and retrieval
        ht.insert("key1", "value1")
        ht.insert("key2", "value2")
        
        self.assertEqual(ht.get("key1"), "value1")
        self.assertEqual(ht.get("key2"), "value2")
        
        # Test updating existing key
        ht.insert("key1", "new_value")
        self.assertEqual(ht.get("key1"), "new_value")
        
        # Test key error for non-existent key
        with self.assertRaises(KeyError):
            ht.get("nonexistent_key")
    
    def test_stack(self):
        stack = Stack()
        
        # Test push and pop
        stack.push(1)
        stack.push(2)
        stack.push(3)
        
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.peek(), 1)
        
        # Test empty stack
        stack.pop()
        with self.assertRaises(IndexError):
            stack.pop()
    
    def test_queue(self):
        queue = Queue()
        
        # Test enqueue and dequeue
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.peek(), 3)
        
        # Test empty queue
        queue.dequeue()
        with self.assertRaises(IndexError):
            queue.dequeue()

class TestSortingAlgorithms(unittest.TestCase):
    def test_bubble_sort(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        sorted_arr = bubble_sort(arr.copy())
        self.assertEqual(sorted_arr, sorted(arr))
    
    def test_merge_sort(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        sorted_arr = merge_sort(arr.copy())
        self.assertEqual(sorted_arr, sorted(arr))
    
    def test_binary_search(self):
        arr = [11, 12, 22, 25, 34, 64, 90]
        self.assertEqual(binary_search(arr, 25), 3)
        self.assertEqual(binary_search(arr, 12), 1)
        self.assertEqual(binary_search(arr, 99), -1)

if __name__ == '__main__':
    unittest.main()