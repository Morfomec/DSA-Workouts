class BST:

    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None


    def insert(self, data):
        if self.key is None:
            self.key = data
            return

        if self.key == data:
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

        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not present in tree")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not present in tree")

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

    def delete(self, data, curr):

        if self.key is None:
            print("Tree is empty")
            return

        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data, curr)
            else:
                print("Given Node is not present in the tree")
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data, curr)
            else:
                print("Given Node is not present in the tree")
        else:
            if self.lchild is None:
                temp = self.rchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp

            if self.rchild is None:
                temp = self.lchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp

            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key, curr)
        return self
    
    def min_node(self):
        current = self
        while current.lchild:
            current = current.lchild
        print("Node with smallest key is:", current.key)

    def max_node(self):
        current = self
        while current.rchild:
            current = current.rchild
        print("Node with  highest key is:", current.key)



def count(node):
    if node is None:
        return 0

    return 1 + count(node.lchild) + count(node.rchild)
     

root = BST(10)
list1 = [10, 20, 30, 101, 2, 12]
# list1 = [1, 2]
for i in list1:
    root.insert(i)  

root.search(10)
root.search(10)
print("Preorder")
root.preorder()
print("\nInorder")
root.inorder()
print("\nPostorder")
root.postorder()
print()
if count(root) > 1:
    root.delete(10, root.key)
else:
    print("Cant perform delete")
root.inorder()
print()
print(count(root))
root.min_node()
root.max_node()



# class BST:

#     def __init__(self, key):
#         self.key = key
#         self.lchild = None
#         self.rchild = None

#     def insert(self, data):
#         if self.key is None:
#             self.key = data
#             return
#         if self.key == data:
#             return
#         if self.key > data:
#             if self.lchild:
#                 self.lchild.insert(data)
#             else:
#                 self.lchild = BST(data)
#         else:
#             if self.rchild:
#                 self.rchild.insert(data)
#             else:
#                 self.rchild = BST(data)
    
#     def search(self.data):

#         if self.key == data:
#             print("Node is found")
#             return

#         if self.key > data:
#             if self.lchild:
#                 self.key.search(data)
#             else:
#                 print("Node is not present in the tree")
#         else:
#             if self.rchild:
#                 self.key.search(data)
#             else:
#                 print("Node is not present in the tree")

#     def preorder(self):

#         print(self.key, end=" ")
#         if self.lchild:
#             self.lchild.preorder()
#         if self.rchild:
#             self.rchild.preorder()

#     def inorder(self):

#         if self.lchild:
#             self.lchild.inoder()     
#         print(self.key, end=" ")
#         if self.rchild:
#             self.rchild.inorder()
        
#     def postorder(self):

#         if self.lchild:
#             self.lchild.postorder()
#         if self.rchild:
#             self.rchild.postorder()
#         print(self.key, end=" ")

#     def delete(self, data, curr):

#         if self.key is None:
#             return

#         if self.key > data:
#             if self.lchild:
#                 self.lchild = self.lchild.delete(data)
#             else:
#                 print("Given node is not present in the tree")
#         elif self.key < data:
#             if self.rchild:
#                 self.rchild = self.rchild.delete(data)
#             else:
#                 print("Given node is not present in the tree")
#         else:
#             if self.lchild is None:
#                 temp = self.lchild
#                 if data == curr:
#                     self.key = temp.key
#                     self.lchild = temp.lchild
#                     self.rchild = temp.rchild
#                     temp = None
#                     return
#                 self = None
#                 return temp

#             if self.rchild is None:
#                 temp = self.rchild
#                 if data == curr:
#                     self.key = temp.key
#                     self.lchild = temp.lchild
#                     self.rchild = temp.rchild
#                     temp = None
#                     return 
#                 self = None
#                 return temp
#             node = self.rchild
#             while node.lchild:
#                 node = node.lchild
#             self.key = node.key
#             self.rchild = self.rchild.delete(node.key)
#         return self



class BST:

    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None
    
    def insert(self, data):
        if not self.key:
            self.key = data
            return
        if self.key == data:
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

    def insert(self, data):

        if not self.key:
            self.key = data
            return

        if self.key == data:
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
                print("Give node not found")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Given node not found")

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

    # def deletion(self, data):

    #     if not self.key:
    #         return 

    #     if self.key > data:
    #         if self.lchild:
    #             self.lchild = self.lchild.delete(data)
    #         else:
    #             print("Given node not present in the tree")
    #     elif self.key < data:
    #         if self.rchild:
    #             self.rchild = self.rchidl.delete(data)
    #         else:
    #             print("Not")

    #     else:
    #         if self.lchild is None:
    #             temp = self.lchild
    #             self = None
    #             return temp
    #         if self.rchild is None:
    #             temp = self.rchild
    #             self = None
    #             return temp
    #         node = self.rchild
    #         while node.lchild:
    #             node = node.lchild
    #         self.key = node.key
    #         self.rchild = self.rchild.delete(data)
    #     return self
            
    def deletion(self, data):

        if not self:
            return 

        if self.key > data:
            if self.lchild:
                self.lchild = self.lchild.deletion(data)
            else:
                print("Not")
        elif self.key < data:
            if self.rchild:
                self.rchild = self.rchild.deletion(data)
            else:
                print("Not")
        else:
            if self.lchild is None:
                temp = self.rchild
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                self = None
                return temp
            node = self.rchild
            while node.lchild:
                node = node.lchild

            self.key = node.key
            self.rchild = self.rchild.deletion(data)
        return self

    def min_node(self):
        current = self
        while current.lchild:
            current = current.lchild
        print("Smallest:", current.key)

    def max_node(self):
        current = self
        while current.rchild:
            current = current.rchild
        print("Largest:",current.key)

    # def height(self):
    #     left_height = -1
    #     right_height = -1
    #     if self is None:
    #         return -1
    #     if self.lchild:
    #         left_height = self.lchild.height()
    #     if self.rchild:
    #         right_height = self.rchild.height()

    #     return 1 + max(left_height, right_height)

    def height(self):

        lt_height = -1
        rt_height = -1

        if self is None:
            return -1
        
        if self.lchild:
            lt_height = self.lchild.height()
        if self.rchild:
            rt_height = self.rchild.height()

        return 1 + max(lt_height, rt_height)


    # def closest(self, target):

    #     node = self
    #     closest_value = self.key

    #     while node:
    #         if abs(target - node.key) < abs(target - closest_value):
    #             closest_value = node.key

    #         if target < node.key:
    #             node = node.lchild
    #         elif target > node.key:
    #             node = node.rchild
    #         else:
    #             return node.key
        
    #     return closest_value

    def closest(self, target):

        node = self
        closest_value = self.key


        while node:

            if abs(target - node.key) < abs(target - closest_value):
                closest_value = node.key

            if target < node.key:
                node = node.lchild
            elif target > node.key:
                node = node.rchild
            else:
                return node.key
        return closest_value



b = BST(5)
b.insert(10)
b.insert(20)
b.insert(30)
b.insert(40)
b.inorder()
print()
b.postorder()
b.deletion(10)
print()
b.inorder()
b.min_node()
b.max_node()
print("Max height:",b.height())
print(b.closest(33))




class BST:

    def __init__(self, node):
        self.node = node
        self.lchild = None
        self.rchild = None

    def insert(self, data):
        if self.node is None:
            self.node = data
            return

        if self.node == data:
            return 

        if self.node > data:
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
        if self.node == data:
            print("Node is found")
            return
        
        if self.node > data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not present in tree")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not present in tree")

    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.node, end=" ")
        if self.rchild:
            self.rchild.inorder()

    def preorder(self):

        print(self.node, end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def postorder(self):

        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.node, end=" ")

    def delete(self, data, curr):

        if self.node is None:
            print("Tree is empty")
            return
        if self.node > data:
            if self.lchild:
                self.lchild.delete(data)
            else:
                print("node not present")
        elif self.node < data:
            if self.rchild:
                self.rchild.delete(data)
            else:
                print("node not present")
        else:
            if self.lchild is None and self.rchild is None:
                return None

            if self.lchild is None:
                return self.rchild
            
            if self.rchild is None:
                return self.lchild
            
            nodee = self.rchild
            while nodee.lchild:
                nodee = nodee.lchild
            self.node = nodee.node
            self.rchild = self.rchild.delete(nodee.node)
        return self


class BST:

    def __init__(self, node):
        self.node = node
        self.lchild = None
        self.rchild = None
    
    def insert(self, data):
        if self.node is None:
            self.node = data
            return 

        if self.node > data:
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

        if self.node == data:
            print("Node found")
            return
        if self.node > data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not present")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not present")

    def delete(self, data):

        if self.node is None:
            print("Node is not preesnt")
            return 

        if self.node > data:
            if self.lchild:
                self.lchild = self.lchild.delete(data)
            else:
                print("Not present")
        elif self.node < data:
            if self.rchild:
                self.rchild = self.rchild.delete(data)
            else:
                print("not present")
        elif:

            if self.lchild is None and self.rchild is None:
                return 
            
            if self.lchild is None:
                return self.rchild
            
            if self.rchild is None:
                return self.rchild:

            temp = self.rchild
            while temp.lchild:
                temp = temp.lchild
            self.node = temp.node
            self.rchild = self.rchild.delete(temp.node)
        return self

    def inorder(self):

        if self.lchild:
            self.lchild.inorder()
        print(self.node, end=" ")
        if self.rchild:
            self.rchild.inorder()

    def postorder(self):

        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.node, end=" ")

    def preorder(self):

        print(self.node, end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchildpreorder()

    def min_node(self):
        current = self
        while current.lchild:
            current = current.lchild
        print(current.node)

    def max_node(self):
        current = self
        while current.rchild:
            node = current.rchild
        print(current.node)

    def height(self):
        left = -1
        right = -1

        if self is None:
            return -1

        if self.lchild:
            left = self.lchild.height()
        if self.rchild:
            right = self.rchild.height()
        
        return 1+max(left, right)

    def height(self):
        left = -1
        right = -1

        if self.node is None:
            return -1

        if self.lchild:
            left = self.lchild.height()
        if self.rchild:
            left = self.rchild.height()
        
        return 1 + max(left, right)


    def kth_element(self, k):
        
        self.count = 0
        self.answer = None

        def inorder(node):

            if not node and self.answer is None:
                return None

            inorder(node.lchild)

            self.count += 1
            if self.answer == k:
                self.answer = node.node
                return 

            inorder(node.rchild)
        inorder(self)
        return self.answer

    def kth_elemet(self):

        self.count = 0
        self.answer = None

        def inorder(node):

            if not node and self.answer is None:
                return

            inorder(node.lchild)

            self.count += 1
            if self.answer == k:
                self.answer = node.node
                return
            
            inorder(node.rchild)
        
        inorder(self)
        return self.answer


    def closest(self, target):

        temp = self
        closest_value = self.node

        while node:
            if abs(target - temp.node) < abs(target - closest_value):
                closest_value = temp.node
            
            if target > temp.node:
                temp = temp.lchild
            elif target < temp.node:
                temp = tem.rchild
            else:
                return temp.node
        return closest_value


    def closest(self, target):

        temp =self
        closest_value = self.node

        while temp:
            if abs(target - temp.node) < abs(target - closest_value):
                closest_value = temp.node

            if target > temp.node:
                temp = temp.lchild
            elif target < temp.node:
                temp = temp.rchild
            else:
                return temp.node
        return closest_value

        




def count(node):
    if node is None:
        return 0

    return 1+count(node.lchild) + count(node.rchild)






def heap_sort(arr):

    size = len(arr)

    for i in range(size//2 -1, -1, -1):
        heapify_down(arr, size, i)
    
    for i in range(size-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
    
        heapify_down(arr, i, 0)