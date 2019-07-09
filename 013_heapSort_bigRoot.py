
#大根堆
#时间复杂度和空间复杂度 
#1. https://blog.csdn.net/loveliuzz/article/details/77618530
#2. https://blog.csdn.net/qq_34228570/article/details/80024306
#生成堆的时间复杂度计算：http://pre.nowcoder.com/questionTerminal/8b5f6be9fd29428ab7c2ea10cd256107?toCommentId=540975
def heapify(arr, n, i): 
    if i >= n:
        return
    largest = i  
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]  # 交换
  
        heapify(arr, n, largest) 

def build_heap(arr, n):
    last_node = n-1
    parent = (last_node-1) // 2
    for i in range(parent, -1, -1):
        heapify(arr, n, i)
  
def heapSort(arr, n): 
    build_heap(arr, n)
    # 一个个交换元素
    for i in range(n-1, -1, -1): 
        arr[i], arr[0] = arr[0], arr[i]   # 交换
        heapify(arr, i, 0) 

if __name__ == '__main__':
    arr = [2, 5, 3, 1, 10, 4]
    heapSort(arr, len(arr))
    print(arr)