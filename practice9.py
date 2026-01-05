class BST:

    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None
    
    def insert(self, data):
        if self.key is None:
            self.key = data
            return 

        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

    def search(self, data):

        if self.key == data:
            print("Node is found")
            return 

        if self.key > data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not presesnt")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not present")
    
    def preorder(self):
        print(self.key, end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key, end=" ")
        if self.rchild:
            self.rchild.inorder()
    
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key, end=" ")


    def delete(self, data):

        if self.key is None:
            print("Tree is empty")
            return
        
        if self.key > data:
            if self.lchild:
                self.lchild = self.lchild.delete(data)
            else:
                print("not present")
        elif self.key < data:
            if self.rchild:
                self.rchild = self.rchild.delete(data)
            else:
                print("Not present")
        else:
            if self.rchild is None and self.lchild is None:
                return None
            
            if self.rchild is None:
                return self.lchild
            if self.lchild is None:
                return self.rchild

            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key)
        return self

    def min_mode(self):

        current = self
        while current.lchild:
            current = current.lchild
            print(current.key)

    def max_mode(self):

        current = self
        while current.rchild:
            current = current.rchild
            print(current.key)
            return current.key

    def kth_element(self, k):
        self.count = 0
        self.answer = None

        def inorder(node):
            if not node or self.answer is None:
                return 

            inoder(node.lchild)

            self.count += 1
            if self.answer == k:
                self.answer = node.key
                return

            inorder(node.rchild)
        
        inorder(self)
        return self.answer

    def height(self):

        left = -1
        right = -1

        if self.node is None:
            return -1

        if self.lchild:
            left = self.lchild.height()
        if self.rchild:
            right = self.rchild.height()

        return 1+max(left, right)


    def closest(self, target):

        node = self
        closest = self.key

        while node:
            if abs(target - node.key) < abs(target - closest):
                closest =  node.key

            if target < node.key:
                node = node.lchild
            elif target > node.key:
                node = node.rchild
            else:
                return node.key

        return closest








# GRAPH

class Graph:

    def __init__(self):
        self.graph = {}

    def add_vertex(self, u):

        if u not in self.graph:
            self.graph[u] = []
            return

    def add_edge(self, u, v):

        self.add_vertex(u)
        self.add_vertex(v)

        if u not in self.graph[v]:
            self.graph[v].append(u)
        if v not in self.graph[u]:
            self.graph[u].append(v)

    def display(self):
        for u in self.graph:
            print(u, "-->", self.graph[u])

def BFS(node, graph, visited):

    if node not in graph:
        print("Graph is not present")
        return
    
    queue = []
    queue.append(node)
    visited.add(node)

    while queue:
        current = queue.pop(0)
        print(current)

        for i in graph[current]:
            if i not in visited:
                queue.append(i)
                visited.add(i)

def DFS(node, graph, visited1):

    if node not in graph:
        print("Graph not present")
        return 

    stack = []
    stack.append(node)
    visited1.add(node)

    while stack:
        current = stack.pop()
        print(current)

        for i in graph[current]:
            if i not in visited1:
                stack.append(i)
                visited1.add(i)


class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word):
        node = self.root

        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    def startsWith(self, prefix):
        node = self.root

        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

    def print_all(self):

        def dfs(node, path):
            if node.is_end:
                print(path)

            for ch in sorted(node.children):
                dfs(node.children[ch], path+ch)
            
        dfs(self.root, "")
    
    def autocomplete(self, prefix):

        node = self.root

        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]
        
        result = []

        def dfs(node, path):
            if node.is_end:
                result.append(path)
            
            for ch in sorted(node.children):
                dfs(node.children[ch], path+ch)
        
        dfs(node, prefix)
        return result


    def lcp(self):

        node = self.root
        prefix = ""
        
        while True:
            if node.is_end or len(self.children) != 1:
                break

            ch = next(iter(node.children))
            prefix += ch
            node = node.children[ch]
        return prefix



class MinHeap:

    def __init__(self):
        self.heap = []

    def insert(self, data):
        self.heap.append(data)
        self._move_up(len(self.heap)-1)

    def remove(self, data):
        if not self.heap:
            return 

        min_val = self.heap[0]
        last = self.heap.pop()

        if self.heap:
            self.heap[0] = last
            self._move_down(0)
        return min_val

    def build(self, arr):

        self.heap = arr[:]
        for i in range(len(self.heap) //2-1, -1, -1):
            self._move_down(i)
            
    def _move_up(self, index):
        parent = (index-1) //2
        while index > 0:
            if self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break
    def _move_down(self, index):
        size = len(self.heap)
        
        while True:
            lchild = (index*2) + 1
            rchild = (index*2) + 2
            smallest = index

            if lchild < size and self.heap[lchild] < self.heap[smallest]:
                smallest = lchild

            if rchild < size and self.heap[rchild] < self.heap[smallest]:
                smallest = rchild

            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest


class MaxHeap:

    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._move_up(len(self.heap)-1)

    def remove(self):

        if not self.heap:
            return
        
        max_val = self.heap[0]
        last = self.heap.pop()

        if self.heap:
            self.heap[0] = last
            self._move_down(0)
        return max_val

    def build(self, arr):

        self.heap = arr[:]
        for i in range(len(self.heap)//2-1, -1, -1):
            self._move_down(i)

    def _move_up(self, index):

        
        while index > 0:
            parent = (index-1) //2
            if self.heap[index] > self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index= parent
            else:
                break
        
    def _move_down(self, index):
        size= len(self.heap)

        while True:
            lchild = (index * 2) + 1
            rchild = (index * 2) + 2
            largest = index

            if lchild < size and self.heap[lchild] > self.heap[largest]:
                largest = lchild

            if rchild < size and self.heap[rchild] > self.heap[largest]:
                largest = rchild
            
            if largest == index:
                break

            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest


def kth_smallest(nums, k):

    max_heap = []

    for num in nums:
        heapq.heappush(max_heap, -num)

        if len(max_heap) > 1:
            heapq.heappop(max_heap)
    return -max_heap[0]

import heapq



def freq_count(nums, k):

    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    min_heap = []

    for num, count in freq.items():
        heapq.heapush(min_heap, (count, num))
    
        if len(min_heap) > 1:
            heapq.heappop(min_heap)

    return [num for count, num in min_heap]


class BT:

    def __init__(self, key):

        self.key = key
        self.lchild = lchild
        self.rchild = rchild

    def insert(self, data):

        if self.key is None:
            self.key = data
            return

        queue = [self]
        
        while queue:
            current = queue.pop(0)

            if not current.lchild:
                current.lchild = BT(data)
                return
            else:
                queue.append(current.lchild)

            if not current.rchild:
                current.rchild = BT(data)
                return
            else:
                queue.append(current.lchild)

    def search(self, data):
        if self.key == data:
            print("node found")
            return

        queue = [self]

        while queue:
            current = queue.pop(0)

            if current.key == data:
                return True
            
            if current.lchild:
                queue.append(current.lchild)
            if current.rchild:
                queue.append(curren.rchild)

        return False


    def search_bt(self, target):
        if self.key is None:
            print("Tree is empty")
            return

        queue = [self]

        while queue:
            current = queue.pop(0)

            if current == target:
                print("Found")
                return
            
            if current.lchild:
                queue.append(current.lchild)
            if current.rchild:
                queue.append(current.rchild)

            
        print("Taget not Found")


    def inorder(self):

        if self.lchild:
            self.lchild.inorder()
        print(self.key, end=" ")
        if self.rchild:
            self.rchild.inorder()
        
    def preorder(self):

        print(self.key, end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def postorder(self):

        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key, end=" ")
    
    def level_order(self):

        queue = [self]

        while queue:
            current = queue.pop(0)

            print(current.key, end=" ")
            if current.lchild:
                queue.append(current.lchild)
            if current.rchild:
                queue.append(current.rchild)


    
    def remove_duplicates(self):

        seen = set()
        queue = [(self, None)]

        while queue:
            current, parent = queue.pop(0)

            if current.key in seen:
                if parent:
                    if parent.lchild == current:
                        parent.lchild = None
                    else:
                        parent.rchild = None
                continue
            else:
                seen.add(current.key)

            if current.lchild:
                queue.append(current.lchild, current)
            if current.rchild:
                queue.append(current.rchild, current)

    def remove_duplicates(self):

        seen = set()
        queue = [(self, None)]

        while queue:
            current, parent = queue.pop(0)

            if current.key in seen:
                if parent:
                    if parent.lchild == current:
                        parent.lchild=None
                    else:
                        paret.rchild = None
            else:
                seen.add(current.key)

            if current.lchild:
                queue.append(current.lchild, current)
            if current.rchild:
                queue.append(current.rchild, current)

    def remove_duplicates(self):

        seen = set()
        queue = [(self, None)]

        while queue:
            current = queue.pop(0)

            if current.key in seen:
                if parent:
                    if parent.lchild == current:
                        parent.lchild = None

                    else:
                        parent.rchild = None
                    
            else:
                seen.add(current.key)

            if current.lchild:
                queue.append(current.lchild, current)
            if current.rchild:
                queue.append(current.rchild, current)

    def is_balance(self):

        def check(node):
            if not node:
                return 0

            left_height = check(node.lchild)
            if left_height == -1:
                return -1

            right_height = check(node.rchild)
            if right_height == -1:
                return -1

            if abs(left_height - right_height) > 1:
                return - 1

            return 1+max(left_height, right_height)
        return check(self) != 1

    def is_balanced(self):

        def check(node):
            if not node:
                return 0

            left_height = check(node.lchild)
            if left_height == -1:
                return -1

            right_height = check(node.rchild)
            if right_height == -1:
                return -1

            if abs(left_height - right_height) >1:
                return -1

            return 1 + max(left_height, right_height)

        return check(self) != 1

    def is_balance(self):

        def check(node):
            if not node:
                return

            left = -1
            right = -1

            left = check(node.lchild)
            if left == -1:
                return -1

            right = check(node.rchild)
            if right == -1:
                return -1

            if abs(left - right) > 1:
                reutn -1
            
            return 1 + max(left, right)
        return check(self)


# --------------------------------------------


class BST:
    
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None
    
    def insert(self, data):
        if self.key is None:
            self.key = data
            return

        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

    def search(self, data):
        if self.key == data:
            print("FOund")
            return

        if self.key > data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Not found")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Not fount")
        
    def delete(self, data):

        if self.key is None:
            print("Tree not present")
            return
        
        if self.key > data:
            if self.lchild:
                self.lchild = self.lchild.delete(data)
                return 
            else:
                print("Not found")

        elif self.key < data:
            if self.rchild:
                self.rchild = self.rchild.delete(data)
                return
            else:
                print("Not found")
        else:
            if self.lchild is None and self.rchild is None:
                return
            
            if self.lchild is None:
                return self.rchild
            
            if self.rchild is None:
                return self.lchild

            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key)
        return self

    def min_node(self):
        current = self
        while current.lchild:
            current = current.lchild
        print(cuurent.key)

    def max_node(self):
        current = self
        while current.rchild:
            current = current.rchild
        print(current.rchild)

    def kth_element(self, k):

        self.count = 0
        self.answer = None

        def inorder(node):
            if not node or self.answer is not None:
                return

            inoder(node.lchild)

            self.count += 1
            if self.count == k:
                self.answer = node.key
                return

            inorder(node.rchild)

        inorder(self)
        return self.answer


    def height(self):
        
        def check(node):

            if not node:
                return 0

            left = check(node.lchild)
            right = check(node.rchild)

            return 1+max(left, right)
        return check(self)
        
    def is_balance(self):



        def check(node):
            if not node:
                return 0

            left = -1
            right= -1

            left = check(node.lchild)
            if left == -1:
                return -1

            right = check(node.rchild)
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

        return check(self) != -1

    def closest(self, target):

        node = self
        closest = self.key

        while node:
            if abs(target - node.key) < abs(target - closest):
                closest = node.key

            if target < node.key:
                node = node.lchild
            elif target > node.key:
                node = node.rchild
            else:
                return node.key
        return closest

#graph

class Graph:

    def __init__(self):
        self.graph = {}

    def add_vertex(self, u):
        if not self.graph:
            self.graph[u] = []
            return

    def add_edge(self, u, v):

        self.add_vertex(u)
        self.add_vertex(v)

        if u not in self.graph[v]:
            self.graph[v].append(u)
        if v not in self.graph[u]:
            self.graph[u].append(u)

    def display(self):

        for u in self.graph:
            print(u, "-->", self.graph[u])

def BFS(node, graph, visited):

    if node not in graph:
        print("Graph not present")
        return 
    
    queue =[]
    queue.append(node)
    visited.add(node)

    while queue:
        current = queue.pop(0)
        print(current)

        for i in graph[current]:
            if i not in visited:
                queue.append(i)
                visited.add(i)


def DFS(node, graph, visited1):

    if node not in graph:
        print("Graph not present")
        return 

    stack =[]
    stack.append(node)
    stack.add(node)

    while stack:
        current = stack.pop()
        print(current)

        for i in graph[current]:
            if i not in visited1:
                stack.append(i)
                visited1.add(i)


# Trie

class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word):

        node = self.root

        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    def startsWith(self, prefix):
        node = self.root

        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

    def print_all(self):

        def dfs(node, path):
            if node.is_end:
                print(path)

            for ch in sorted(node.children):
                dfs(node.children[ch], path + ch)

        dfs(self.root, "")

    def autocomplete(self, prefix):

        node =self.root
        
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]
        
        result = []

        def dfs(node, path):
            if node.is_end:
                result.append(path)

            for ch in sorted(node.children):
                dfs(node.children[ch], path +ch)
        dfs(node, prefix)
        return result
    
    def lcp(self):

        node = self.root
        prefix = ""

        while True:
            if node.is_end or len(node.children) != 1:
                break

            ch = next(iter(node.children))
            prefix += ch
            node = node.children[ch]

        return prefix

#Heap

class MinHeap:

    def __init__(self):
        self.heap = []

    def insert(self, data):
        self.heap.append(data)
        self._move_up(len(self.heap)-1)

    def remove(self):

        if self.heap is None:
            return 

        min_val = self.heap[0]
        last = self.heap.pop()

        if self.heap:
            self.heap[0] = last
            self._move_down(0)

        return min_val
    
    def _move_up(self, index):

        while index > 0:
            parent = (index -1) //2
            if self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] ==
                index = parent
            else:
                break

    def build(self, arr):
        self.heap = arr[:]
        for i in range(len(self.heap) // 2-1, -1, -1):
            self._move_down(i)

    def _move_down(self, index) :
        size = len(self.heap)
        while True:
            lchidl = (index *2) + 1
            rchild = (index * 2) + 2
            smallest = index

import heapq

def kth_smallest(nums, k):

    max_heap = []

    for num in nums:
        heapq.heappush(max_heap, -num)

        if len(max_heap) > k:
            heapq.heappop(max_heap)
    return -max_heap[0]
     
def fre(nums, k):

    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0)+1

    min_heap = []

    for num, count in freq.items():
        heapq.heappush(min_heap,(count, num))

        if len(min_heap) > 1:
            heapq.heappop(min_heap)

    return [num for count, num in min_heap]


def insert(self, data):

    if self.key is none:
        self.key = data

    queue = [self]
    while queue:
        current

        if not current.lchuld
            BT
        else:
            queue.append()