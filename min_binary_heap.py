class MinHeap:

    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._move_up(len(self.heap)-1)

    def remove(self, value):
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
        for i in range(len(self.heap) // 2-1, -1, -1):
            self._move_down(i)

    def _move_up(self, index):

        while index > 0:
            parent = (index -1)//2
            if self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else: 
                break
        

    def _move_down(self, index):

        size = len(self.heap)

        while True:
            lchild = (index *2) +1
            rchild = (index *2) +2
            smallest = index
            if lchild < size and self.heap[lchild] < self.heap[smallest]:
                smallest = lchild

            if rchild < size and self.heap[rchild] < self.heap[smallest]:
                smallest = rchild

            if smallest == index:
                break
            
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest


class MinHeapp:

    def __init__(self):
        self.heap = []
    
    def insert(self, value):
        self.heap.append(value)
        self._move_up(len(self.heap)-1)

    def remove(self, value):

        if not self.heap:
            return

        min_val = self.heap[0]
        last = self.heap.pop()

        if self.heap:
            self.heap[0] = last
            self._move_down(0)

    def build(self, arr):
        self.heap = arr[:]
        for i in range(len(self.heap)//2-1, -1, -1):
            self._move_down(i)
    
    def _move_up(self, index):

        while index > 0:
            parent = (index -1) //2
            if self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

        

    def _move_down(self, index):

        size = len(self.heap)

        while True:

            lchild = (index *2) + 1
            rchild = (index *2) + 2
            smallest = index

            if lchild < size and self.heap[lchild] < self.heap[smallest]:
                smallest = lchild
            if rchild < size and self.heap[rchild] < self.heap[smallest]:
                smallest = rchild

            if smallest == index:
                break 
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest
m = MinHeapp()
li = [2, 4, 5, 1, 6, 8]
m.build(li)
print("Builded",m.heap)
m.remove(5)
print("Builded",m.heap)


class MinHeap:
    def __init__(self):
        self.data = []

    def insert(self, value):
        self.data.append(value)
        self._move_up(len(self.data)-1)

    def remove(self):

        if not self.data:
            return None

        min_value = self.data[0]
        last = self.data.pop()

        if self.data:
            self.data[0] = last
            self._move_down(0)

        return min_value

    def _move_up(self, index):

        while index > 0:
            parent = (index - 1) // 2

            if self.data[index] < self.data[parent]:
                self.data[index], self.data[parent] = self.data[parent], self.data[index]
                index = parent
            else:
                break

    def _move_down(self, index):
        size = len(self.data)

        while True:
            lchild = (2* index) +1
            rchild = (2* index) +2
            smallest = index

            if lchild < size and self.data[lchild] < self.data[smallest]:
                smallest = lchild

            if rchild < size and self.data[rchild] < self.data[smallest]:
                smallest = rchild
            
            if smallest == index:
                break

            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            index = smallest

    def build(self, arr):
        self.data = arr[:]
        for i in range(len(self.data)//2-1, -1, -1):
            self._move_down(i)


m = MinHeap()
m.build([1, 2, 3, 12 , 22,  5])
print("Min_Heap:", m.data)
m.insert(19)
m.remove()
m.remove()
print("Min_Heap:", m.data)

# class MinHeap:
#     def __init__(self):
#         self.data = []

#     # -------- BUILD HEAP --------
#     def build(self, arr):
#         self.data = arr[:]
#         for i in range(len(self.data)//2 - 1, -1, -1):
#             self._move_down(i)

#     # -------- INSERT --------
#     def insert(self, value):
#         self.data.append(value)
#         self._move_up(len(self.data) - 1)

#     # -------- REMOVE (MIN ELEMENT) --------
#     def remove(self):
#         if not self.data:
#             return None

#         min_value = self.data[0]
#         last = self.data.pop()

#         if self.data:
#             self.data[0] = last
#             self._move_down(0)

#         return min_value

#     # -------- HELPER: MOVE UP --------
#     def _move_up(self, index):
#         while index > 0:
#             parent = (index - 1) // 2

#             if self.data[index] < self.data[parent]:
#                 self.data[index], self.data[parent] = self.data[parent], self.data[index]
#                 index = parent
#             else:
#                 break

#     # -------- HELPER: MOVE DOWN --------
#     def _move_down(self, index):
#         size = len(self.data)

#         while True:
#             left = 2 * index + 1
#             right = 2 * index + 2
#             smallest = index

#             if left < size and self.data[left] < self.data[smallest]:
#                 smallest = left

#             if right < size and self.data[right] < self.data[smallest]:
#                 smallest = right

#             if smallest == index:
#                 break

#             self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
#             index = smallest


class Min_heap:

    def __init__(self):
        self.data = []


    def _move_up(self, index):
        while index > 0:
            parent = (index -1) // 2
            if self.data[index] < self.data[parent]:
                self.data[index], self.data[parent] = self.data[parent], self.data[index]
                index = parent
            else:
                break

    def _move_down(self, index):
        size = len(self.data)

        while True:
            lchild = (2 * index) +1 
            rchild = (2 * index) +2

            smallest = index
            if lchild < size and self.data[lchild] < self.data[smallest]:
                smallest = lchild

            if rchild < size and self.data[rchild] < self.data[smallest]:
                smallest = rchild

            if smallest == index:
                break
            
            self.data[smallest], self.data[index] = self.data[index], self.data[smallest]
            index = smallest

    def insert(self, value):

        self.data.append(value)
        self._move_up(len(self.data)-1)

    def remove(self, value):

        if self.data is None:
            return None

        min_value = self.data[0]
        last = self.data.pop()

        if self.data:
            self.data[0] = last
            self._move_down(0)
        return min_value

    def build(self, arr):

        self.data = arr[:]
        for i in range(len(self.data)//2-1, -1, -1):
            self._move_down(i)


class Min_heap:

    def __init__(self):
        self.data = []

    def insert(self, value):
        self.data.append(value)
        self._move_up(len(self.data) - 1)

    def remove(self):
        if not self.data:
            return None

        min_val = self.data[0]
        last = self.data.pop()

        if self.data:
            self.data[0] = last
            self._move_down(0)

    def build(self, arr):
        self.data = arr[:]
        for i in range(len(self.data)//2-1, -1, -1):
            self._move_down(i)

    def _move_up(self, index):

        while index > 0:
            parent = (index -1) // 2

            if self.data[index] < self.data[parent]:
                self.data[index], self.data[parent] = self.data[parent], self.data[index]
                index = parent
            else:
                break

    def _move_down(self, index):
        size = len(self.data)

        while True:
            lchild = (index *2  ) +1
            rchild = (index *2) +2
            smallest = index

            if lchild < size and self.data[lchild] < self.data[smallest]:
                smallest = lchild

            if rchild < size and self.data[rchild] < self.data[smallest]:
                smallest = rchild
            
            if smallest == index:
                break
            
            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            index = smallest
