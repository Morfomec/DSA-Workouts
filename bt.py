# class Node:

#     def __init__(self, data):
#         self.data = data
#         self.lchild = None
#         self.rchild = None

# class BT:

#     def __init__(self):
#         self.root = None

#     def insert(self, data):
#         new_node = Node(data)

#         if not self.root:
#             self.root = new_node
#             return
        
#         queue = [self.root]

#         while queue:
#             current = queue.pop(0)

#             if not current.left:
#                 current.left = new_node
#                 return 
#             else:
#                 queue.append(current.left)
            
#             if not current.right:
#                 current.right = new_node
#                 return
#             else:
#                 queue.append(current.right)

#     def level_order(self):
#         if not self.root:
#             print("Root not present")
#             return
        
#         queue = [self.root]

#         while queue:
#             current = queue.pop(0)
#             print(current, end=" ")

#             if current.left:
#                 queue.append(current.left)
#             if current.right:
#                 queue.append(current.right)

#     # def inorder(self):

#     #     stack = []
#     #     current = self.root

#     #     while stack and current:
#     #         while current:
#     #             stack.append(current)
#     #             current = current.left

#     #         current = stack.pop()
#     #         print(current.data, end=" ")
#     #         current = current.right

#     def inorder(self):
#         stack = []
#         current = self.root
#         while stack or current: 
#             while current:
#                 stack.append(current)
#                 current = current.left

#             current = stack.pop()
#             print(current.data, end=" ")
#             current = current.right
        
#     def preorder(self):
#         if not self.root:
#             return 

#         stack = [self.root]

#         while stack:
#             current = stack.pop()
#             print(currnt.data, end=" ")

#             if current.right:
#                 stack.append(current.right)
#             if current.left:
#                 stack.append(current.left)

#     def postorder(self):

#         if not self.root:
#             return
        
#         stack = [self.root]
#         stack2 = []

#         while stack:
#             current = stack.pop()
#             stack2.append(current)

#             if current.left:
#                 stack2.append(current.left)
#             if current.right:
#                 stack2.append(current.right)

#         while stack2:
#             print(stack2.pop().data, end=" ")




    
# class Node:

#     def __init__(self, data):
#         self.data = data
#         self.lchild = None
#         self.rchild = None

# class BT:

#     def __init__(self):
#         self.root = None

#     def insert(self, data):
#         new_node = Node(data)

#         if not self.root:
#             self.root = new_node
#             return

#         queue = [self.root] 
#         while queue:
#             current = queue.pop(0)

#             if not current.lchild:
#                 current.lchild = new_node
#             else:
#                 queue.append(current.lchild)
#             if not current.rchild:
#                 current.rchild = new_node
#             else:
#                 queue.append(current.rchild)

#     def level_order(self):

#         if not self.root:
#             return

#         queue = [self.root]

#         while queue:
#             current = queue.pop(0)
#             print(current.data, end=" ")

#             if current.lchild:
#                 queue.append(current.lchild)
#             if current.rchild:
#                 queue.append(current.rchild)
            
#     def inorder(self):

#         stack = []
#         current = self.root

#         while stack and current:
#             while current:
#                 stack.append(current)
#                 current = current.lchild

#             current = stack.pop()
#             print(current.data, end=" ")
#             current = current.rchild()

#     def preorder(self):

#         stack = [self.root]
        

#         while stack:
#             current = stack.pop()
#             print(current.data, end=" ")

#             if current.lchild:
#                 stack.append(current.lchild)
#             if current.rchild:
#                 stack.append(current.rchild)


#     def postorder(self):

#         if not self.root:
#             return

#         stack = [self.root]
#         stack2 = []

#         while stack:
#             current = stack.pop()
#             stack2.append(current)

#             if current.lchild:
#                 stack2.append(current.lchild)
#             if current.rchild:
#                 stack2.append(current.rchild)

#         while stack2:
#             print(stack2.pop().data, end=" ")

class Node:

    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

class BT:

    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)

        if not self.root:
            self.root = new_node
            return

        queue = [self.root]
        while queue:
            current = queue.pop(0)

            if not current.lchild:
                current.lchild = new_node
                return
            else:
                queue.append(current.lchild)

            if not current.rchild:
                current.rchild = new_node
                return
            else:
                queue.append(current.rchild)

    def level_order(self):
        if not self.root:
            return

        queue = [self.root]
        
        while queue:
            current = queue.pop(0)
            print(current.data, end=" ")

            if current.lchild:
                queue.append(current.lchild)
            if current.rchild:
                queue.append(current.rchild)


    def inorder(self):

        stack = []
        current = self.root

        while current or stack:
            while current:
                stack.append(current)
                current = current.lchild

            current = stack.pop()
            print(current.data, end=" ")
            current = current.rchild

    
    def preorder(self):
        # if not self.order:
        #     return

        stack =[self.root]

        while stack:    
            current = stack.pop()
            print(current.data, end=" ")

            if current.rchild:
                stack.append(current.rchild)
            if current.lchild:
                stack.append(current.lchild)
    
    def postorder(self):

        stack = [self.root]
        stack2 = []

        while stack:
            current = stack.pop()
            stack2.append(current)

            if current.lchild:
                stack.append(current.lchild)
            if current.rchild:
                stack.append(current.rchild)
        
        while stack2:
            print(stack2.pop().data, end=" ")



b = BT()
b.insert(1)
b.insert(2)
b.insert(3)
b.insert(4)
b.insert(5)
b.insert(6)
b.insert(7)
b.inorder()
print()
b.level_order()
print()
b.postorder()
print()
b.preorder()