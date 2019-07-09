def shellSort(alist):
	n = len(alist)
	gap = n // 2

	#gap要大于1，控制下面插入算法次数的控制
	while gap > 0:
		#里面相当于做了第一层划分和比较
		for j in range(gap, n):
			i = j
			#举个例子----i=5 gap=4
			while i > 0:
				if alist[i] < alist[i-gap]:
					alist[i-gap], alist[i] = alist[i], alist[i-gap]
					i -= gap
				else:
					break

		gap = gap // 2




if __name__ == '__main__':
	li = [54,26,93,17,77,31,44,55,20]
	print(li)
	shellSort(li)
	print(li)