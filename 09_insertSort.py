def insertSort(alist): #这种方法最有时间复杂度为O(n)，最坏时间复杂度为O(n^2)

	#外层循环：从右边无序序列中取出多少个元素执行这样的过程
	for j in range(1, len(alist)):
		i = j
		while i > 0:  #内层循环：执行从右边的无序序列中取出第一个元素，即i位置的元素，然后将其插入到前面的正确位置中
			if alist[i] < alist[i-1]:
				alist[i-1], alist[i] = alist[i], alist[i-1]
				i -= 1  #每循环一次都要将i减1
			else:
				break

		#内层的while循环也可以使用 range(i, 0, -1)，如下

'''
def insert_sort(alist):
	
    # 从第二个位置，即下标为1的元素开始向前插入
    for i in range(1, len(alist)):
        # 从第i个元素开始向前比较，如果小于前一个元素，交换位置
        for j in range(i, 0, -1):
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]
'''
if __name__ == '__main__':
	li = [54,26,93,17,77,31,44,55,20]
	print(li)
	insertSort(li)
	print(li)