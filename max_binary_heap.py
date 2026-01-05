class MaxHeap:

    def __init__(self):
        self.data = []

    def insert(self, value):
        self.data.append(value)
        self._move_up(len(self.data)-1)

    def remove(self):

        if not self.data:
            return None

        max_val = self.data[0]
        last = self.data.pop()

        if self.data:
            self.data[0] = last
            self._move_down(0)

        return max_val

    def build(self, arr):
        self.data = arr[:]
        for i in range(len(self.data) //2-1, -1, -1):
            self._move_down(i)


    def _move_up(self, index):
        
        while index > 0:
            parent = (index -1) // 2

            if self.data[index] > self.data[parent]:
                self.data[index], self.data[parent] = self.data[parent], self.data[index]
                index = parent
            else:
                break

    def _move_down(self, index):

        size = len(self.data)
        while True:
            lchild = (2*index) +1
            rchild = (2*index) +2
            largest = index

            if lchild > size  and self.data[lchild] > self.data[largest]:
                largest = lchild

            if rchild > size and self.data[rchild] > self.data[largest]:
                largest = rchild

            if largest == index:
                break

            self.data[index], self.data[largest] = self.data[largest], self.data[index]
            index = largest

h = MaxHeap()
# h.build([5, 3, 8, 4, 1])
h.build([4, 10, 3, 5, 1])
print(h.data)      # [8, 4, 5, 3, 1]

h.insert(0)
print(h.data)      # [10, 4, 8, 3, 1, 5]

print(h.remove())  # 10
print(h.data)   



class MaxHeap:
    
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._move_up(len(self.heap)-1)

    def remove(self, value):
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
        for i in range(len(self.heap) // 2-1, -1, -1):
            self._move_down(i)

    def _move_up(self, index):

        while index > 0:

            parent = (index -1) // 2
            if self.heap[index] > self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def _move_down(self, index):

        size = len(self.heap)

        while True:
            lchild = (index*2) + 1
            rchild = (index*2) + 2
            largest = index

            if lchild < size and self.heap[lchild] > self.heap[largest]:
                largest = lchild
            if rchild < size and self.heap[rchild] > self.heap[largest]:
                largest = rchild
            if largest == index:
                break

            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest

m = MaxHeap()
li = [1, 2, 3, 4, 5]
m.build(li)
print("New",m.heap)
print(m.remove(2))
print("New",m.heap)

    