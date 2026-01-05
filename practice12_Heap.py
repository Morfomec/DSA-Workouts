class MinHeap:

    def __init__(self):
        self.heap = []

    def insert(self ,data):
        self.heap.append(data)
        self._move_up(len(self.heap) -1)

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
            lchild = (index* 2) +1
            rchild = (index* 2) +2
            smallest = index

            if lchild < size and self.heap[lchild] < self.heap[smallest]:
                smallest = lchild
            
            if rchild < size and self.heap[rchild] < self.heap[smallest]:
                smallest = rchild

            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]

            index = smallest

    def display(self):
        print(self.heap)

m = MinHeap()
ls = [2, 3, 4, 5, 112, 6, 7, 7, 7, 7, 1]
m.build(ls)
# print(m.heap)
# print(m.heap)
m.display()






import heapq



def kth_smallest(nums, k):

    heap = []

    for num in nums:
        heapq.heappush(heap, -num)

        if len(heap) > k:
            heapq.heappop(heap)
    return -heap[0]


def k_largest(nums, k):

    heap = []

    for num in nums:
        heapq.heappush(heap, num)

        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]

k = 8
print(kth_smallest(ls, k))
q = 2
print("Largest", k_largest(ls, q))


def freq(nums, k):

    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    min_heap = []

    for num, count in freq.items():
        heapq.heappush(min_heap,(count, num))

        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return [num for count, num in min_heap]



def top_k(nums, k):

    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) +1

    min_heap = []

    for num, count in freq.items():
        heapq.heappush(min_heap, (count, num))

        if len(min_heap) > k:
            heapq.heappop(min_heap)
    
    return [(num, count) for count, num in min_heap]

k = 5
print(f"Top {k} are",top_k(ls, k))



def heapify(arr):
    size= len(arr)

    def _move_down(index):
        while True:
            lchild = (index *2) + 1
            rchild = (index *2) + 2
            smallest = index

            if lchild < size and arr[lchild] < arr[smallest]:
                smallest = lchild
            if rchild < size and arr[rchild] < arr[smallest]:
                smallest = rchild

            if smallest == index:
                break

            arr[index], arr[smallest] = arr[smallest], arr[index]
            index = smallest

    for i in range(size//2-1, -1, -1):
        _move_down(i)


arr = [2, 3, 4, 5, 6, 7, 1]
heapify(arr)
print(arr)
        


def heap_sort(arr):
    size = len(arr)

    for i in range(size//2-1, -1, -1):
        move_down(arr, size, i)

    for i in range(size-1, 0, -1):
        move_down(arr, i, 0)

def move_down(arr, size, index):

    while True:
        lchild = (index*2)+1
        rchild = (index*2)+2
        largest = index

        if lchild < size and arr[lchild] < arr[largest]:
            largest = lchild

        if rchild < size and arr[rchild] < arr[largest]:
            largest = rchild

        if largest == index:
            break
        
        arr[index], arr[largest] = arr[largest], arr[index]
        index = largest
    
lq = [ 12, 31, 53, 65, 95, 13]
heap_sort(lq)
print("lq:", lq)


def heap_sort(arr):

    size = len(arr)

    for i in range(size//2-1, -1, -1):
        move_down(arr, arr, i)

    for i in range(size-1, 0, -1):
        move_down(arr, i, 0)

def heap_sort(arr):

    size = len(arr)

    for i in range(size//2-1, -1, -1):
        move_down(arr, size, i)

    for i in range(size-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        move_down(arr, i, 0)

    return arr


class MaxHeap:

    def __init__(self):
        self.heap = []

    def insert(self, data):
        self.heap.append(data)
        self._move_up(len(self.heap)-1)

    def remove(self):

        if not self.heap:
            return None

        max_val = self.heap[0]
        last = self.heap.pop()

        if self.heap:
            self.heap[0] = last
            self._move_down(0)

        return max_val

    def _move_up(self, index):

        while index > 0:
            parent = (index-1)//2
            if self.heap[index] > self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def build(self, arr):
        self.heap = arr[:]

        for i in range(len(self.heap)//2-1, -1, -1):
            self._move_down(i)


import heapq

def kth_smallest(nums, k):

    max_heap = []

    for num in nums:
        heapq.heappush(max_heap, -num)

        if len(max_heap) > k:
            heapq.heappop(max_heap)
    retrun -max_heap[0]

def freq(nums, k):

    freq= {}

    for num in nums:
        freq[num] = freq.get(num, 0) +1

    min_heap = []

    for num, count in freq.items():
        heapq.heappush(min_heap, (count, num))

        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return [num for count, num in min_heap]

# ---------------------------------------------------------




class MinHeap:

    def __init__(self):
        self.heap = []
    
    def insert(self, values):
        self.heap.append(values)
        self._move_up(len(self.heap)-1)

    def remove(self):
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
        for i in range(len(self.heap)//2 -1, -1, -1):
            self._move_down(i)

    def _move_up(self, index):

        while index > 0:
            parent = (index-1) //2
            if self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def _move_down(self, index):
        size = len(self.heap)

        while True:
            lchild = (index * 2)+1
            rchild = (2 * index)+2
            smallest = index

            if lchild < size and self.heap[lchild] < self.heap[smallest]:
                smallest = lchild
            if rchild < size and self.heap[rchild] < self.heap[smallest]:
                smallest = rchild

            if smallest == index:
                break
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest

m = MinHeap()
m.insert(3)
m.insert(12)
m.insert(1)
m.insert(5)
print(m.heap)
m.remove()
print(m.heap)


    