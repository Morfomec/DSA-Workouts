# def heapify_down(arr, size, index):

#     while True:

#         lchild = (index * 2) + 1
#         rchild = (index * 2) + 2
#         largest = index

#         if lchild < size and arr[lchild] > arr[largest]:
#             largest = lchild
        
#         if rchild < size and arr[rchild] > arr[largest]:
#             largest = rchild

#         if largest == index:
#             break
        
#         arr[index], arr[largest] = arr[largest], arr[index]
#         index = largest


# def heap_sort(arr):
#     size = len(arr)

#     for i in range(size // 2-1, -1, -1):
#         heapify_down(arr, size, i)


#     for i in range(size-1, 0, -1):
#         arr[i], arr[0] = arr[0], arr[i]
#         heapify_down(arr, i , 0)

#     return arr

# li = [11, 2, 9, 1, 7, 10, 4]
# print("After sorting:",heap_sort(li))



def heap_sort(arr):
    size = len(arr)

    for i in range(size//2-1, -1, -1):
        heapify_down(arr, size, i)

    for i in range(size-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify_down(arr, i, 0)

    return arr

def heapify_down(arr, size, index):
    
    while True:
        lchild = (2 * index) + 1
        rchild = (2 * index) + 2
        largest = index

        if lchild < size and arr[lchild] > arr[largest]:
            largest = lchild

        if rchild < size and arr[rchild] > arr[largest]:
            largest = rchild

        if largest == index:
            break
        
        arr[index], arr[largest] = arr[largest], arr[index]
        index = largest


lo = [33, 11, 33, 66, 77, 88, 44]
print("Heap sort:", heap_sort(lo))



def heap_sort(arr):

    size = len(arr)

    for i in range(size//2-1, -1, -1):
        heapify_down(arr, size, i)

    for i in range(size-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify_down(arr, i, 0)

    return arr

def heapify_down(arr, size, index):

    while True:

        lchild = (index *2) +1
        rchild = (index *2) +2
        largest = index

        if lchild < size and arr[lchild] > arr[largest]:
            largest = lchild

        if rchild < size and arr[rchild] > arr[largest]:
            largest = rchild

        if largest == index:
            break
        
        arr[index], arr[largest] = arr[largest], arr[index]
        index = largest


la = [33, 11, 121, 321, 123]
m=(sorted(heap_sort(la), reverse=True))
print(m)

import heapq

task = []
heapq.heappush(task, (1, "high priority"))
heapq.heappush(task, (3, "low priority"))
heapq.heappush(task, (2, "medium priority"))

while task:
    print(heapq.heappop(task))


task 