#快速排序很重要，必须要掌握
def quickSort(alist, first, last):
	# 递归的退出条件 **********当first=last的时候，说明只是同一个数，即只剩下一个数
	if first >= last:
		return
	low = first
	high = last
	midValue = alist[first]

	while low < high:
		while low < high and alist[high] >= midValue:
			high -= 1
		alist[low] = alist[high]

		while low < high and alist[low] <= midValue:
			low += 1
		alist[high] = alist[low]

	alist[low] = midValue

	quickSort(alist, first, (low-1))
	quickSort(alist, (low + 1), last)



if __name__ == '__main__':
	li = [54,26,93,17,77,31,44,55,20]
	print(li)
	quickSort(li, 0, (len(li)-1) )
	print(li)