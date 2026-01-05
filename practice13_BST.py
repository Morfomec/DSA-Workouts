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
            return 

        if self.key > data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Not present")

        else:
            if self.rchild:
                self.rchild.search(data)
            else:print("not preset")

    def delete(self, data):
        if self.key is None:
            return 

        if self.key > data:
            if self.lchild:
                self.lchild = self.lchild.delete(data)
                return 
            else:
                print("Tree not present")
        elif self.key < data:
            if self.rchild:
                self.rchild = self.rchild.delete(data)
                return
            else:
                print("Not present")

        else:
            if not self.lchild and not self.rchild:
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
        current = self.key
        while current:
            current = current.key
        print(current.key)

    def min_node(self):
        current = self
        while current.lchild:
            current = current.lchild
        print(current.key)
    
    def max_node(self):
        current = self
        while current.rchild:
            current = curret.rchild
        print(current.rchild)
    

    def kth_element(self, k):

        self.count = 0
        self.answer = None

        def inorder(node):

            if not node or self.answer is not None:
                return 
            
            inorder(node.lchild)

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

    def height(self):

        def check(node):
            if not node:
                return 0

            left = check(node.lchild)
            right = check(node.rchild)
            return 1+max(left, right)
        return check(self)

    def is_balanced(self):

        def check(node):
            if not node:
                return 0

            left = check(node.lchild)
            if left == -1:
                return -1

            right = check(node.rchild)
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return 1+max(left, right)
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


            

b = BST(10)
b.insert(12)
b.insert(13)
b.insert(11)
b.insert(14)
b.insert(17)
b=b.delete(10)
print(b.kth_element(1))
print("height:", b.height())
if b.is_balanced():
    print("Balanced")
else:
    print("Not balanced")
print(b.closest(50))