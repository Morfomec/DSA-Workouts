class BT:

    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self, value):
        if self.key is None:
            self.key = value
            return
        
        queue = [self]

        while queue:
            current = queue.pop(0)
            
            if not current.lchild:
                current.lchild = BT(value)
                return
            else:
                queue.append(current.lchild)
            
            if not current.rchild:
                current.rchild = BT(value)
                return
            else:
                queue.append(current.rchild)
    
    def search(self, value):

        queue = [self]

        while queue:
            current = queue.pop(0)

            if current.key == value:
                # print("Found")
                return True

            if current.lchild:
                queue.append(current.lchild)
            if current.rchild:
                queue.append(current.rchild)

        return False

    def level_order(self):

        queue = [self]

        while queue:
            current = queue.pop(0)

            print(current.key, end=" ")
            if current.lchild:
                queue.append(current.lchild)
            if current.rchild:
                queue.append(current.rchild)

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
            seen.add(current.key)

            if current.lchild:
                queue.append((current.lchild, current))
            if current.rchild:
                queue.append((current.rchild, current))

    
    def height(self):

        def check(node):
            if not node:
                return 0

            left = check(node.lchild)
            right = check(node.rchild)

            return 1 + max(left, right)
        
        return check(self)



    def is_balanced(self):

        def check(node):

            if not node:
                return 0

            left = check(node.lchild)
            right = check(node.rchild)

            if left == - 1:
                return -1

            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return 1+max(left, right)

        return check(self) != -1


    def identical(self, other):

        def check(n1, n2):
            if not n1 and not n2:
                return True
            
            if not n1 or not n2:
                return False
            
            if n1.key != n2.key:
                return False

            return (
                check(n1.lchild, n2.lchild) and
                check(n1.rchild, n2.rchild)
            )

        return check(self, other)

    # def identical(self, other):

    #     def check(n1, n2):

    #         if not n1 and not n2:
    #             return True

    #         if not n1 or not n2:
    #             return False

    #         if n1.key != n2.key:
    #             return False

    #         return (
    #             check(n1.lchild, n2.lchild) and
    #             check(n2.lchild, n2.lchild)
    #         )
    #     return check(self, other)



    def find_leaves(self):

        leaves = []   

        def check(node):

            if not node:
                return

            if not node.lchild and not node.rchild:
                leaves.append(node.key)
                return
            check(node.lchild)
            check(node.rchild)
        check(self)
        return leaves



    def find_leaves(self):

        leaves = []

        def check(node):

            if not node:
                return 

            if not node.lchild and not node.rchild:
                leaves.append(node.key)
                return 

            check(node.lchild)
            check(node.rchild)
        check(self)
        return leaves

    

# def are_identical(root1, root2):

#     if not root1 and not root2:
#         return True

#     if not root1 or not root2:
#         return False

#     if root1.key != root2.key:
#         return False

#     return(
#         are_identical(root1.lchild, root2.lchild) and
#         are_identical(root1.rchild, root2.rchild)
#     )






    

b = BT(10)
b.insert(1)
b.insert(2)
b.insert(3)
b.insert(3)
b.insert(4)
b.insert(4)
b.insert(5)
b.insert(5)

b2 = BT(22)
b2.insert(2)
b2.insert(21)
b2.insert(12)
b2.insert(24)
b2.insert(23)

# b.insert(6)
if b.search(110):
    print("Found")
else:
    print("Not Found")
b.level_order()
print()
# b.inorder()
print()
# remove_duplicates(b)
b.remove_duplicates()
b.level_order()
print()
print("Height:",b.height())
if b.is_balanced():
    print("Tree balanced")
else:
    print("Not balanced")
b2.level_order()
print()

if b2.identical(b):
    print("They are identical")
else:
    print("They are not")

print(b.identical(b2))
print(b2.find_leaves())


print("------------------------------")



class BTT:

    def __init__(self, key):

        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self, data):
        if not self.key:
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
                queue.append(current.rchild)

    def search(self, value):

        queue = [self]

        while queue:
            current = queue.pop(0)

            if current.key == value:
                # print("Found")
                return True

            if current.lchild:
                queue.append(current.lchild)
            if current.rchild:
                queue.append(current.rchild)

    def level_order(self):

        queue =[self]

        while queue:
            current = queue.pop(0)
            print(current.key)

            if current.lchild:
                queue.append(current.lchild)
            if current.rchild:
                queue.append(current.rchild)


    def preorder(self):

        print(self.key, end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

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
            seen.add(current.key)

            if current.lchild:
                queue.append((current.lchild, current))
            if current.rchild:
                queue.append((current.rchild, current))
    
    def height(self):

        def check(node):
            if not node:
                return 0

            left  = check(node.lchild)
            right = check(node.rchild)

            return 1 + max(left, right)
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

            return 1 + max(left, right)
        return check(self) != -1

    def find_leaves(self):
        
        leaves = []

        def check(node):
            if not node:
                return
            if not node.lchild and not node.rchild:
                leaves.append(node.key)
                return
            check(node.lchild)
            check(node.rchild)
        check(self)
        return leaves

    def identical(self, other):

        def check(n1, n2):
            if not n1 and not n2:
                return True
            
            if not n1 or not n2:
                return False

            if n1.key != n2.key:
                return False

            return(
                check(n1.lchild, n2.lchild) and
                check(n2.rchild, n2.rchild)
            )
        return check(self, other)



# def identical(root1, root2):

#     if not root1 and not root2:
#         return True

#     if not root1 or not root2:
#         return False

#     if root1.key != root2.key:
#         return False

#     return(
#         identical(root1.lchild, root2.lchild) and
#         identical(root1.rchild, root2.rchild)
#     )



bb =BTT(11)
bb.insert(12)
bb.insert(13)
bb.insert(16)
bb.insert(14)
bb.insert(15)
bb.insert(16)
bb.insert(16)
bb.insert(16)
# print(bb.search(12))
if bb.search(14):
    print("Found")
else:
    print("Not found")
bb.level_order()
print()
bb.preorder()
print()
print("Height:",bb.height())
if bb.is_balanced():
    print("Yes balanced")
else:
    print("Not balanced")
bb.remove_duplicates()
bb.level_order()
print()
print(bb.find_leaves())

bc =BTT(1)
bc.insert(12)

if bb.identical(bc):
    print("Yes it is identical")
else:   
    print("Nooo")


