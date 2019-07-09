def selectionSort(alist):
	for j in range(0, len(alist)-1): #j  0 ~ (n-2)
		origin_min_index = j
		for i in range(j+1, len(alist)):
			if alist[i] < alist[origin_min_index]:
				current_min_index = i
				alist[origin_min_index], alist[current_min_index] = alist[current_min_index], alist[origin_min_index]


if __name__ == '__main__':
	li = [54,26,93,17,77,31,44,55,20]
	print(li)
	selectionSort(li)
	print(li)