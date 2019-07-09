def mergeSort(alist):
	n = len(alist)
	if len(alist) <= 1:
		return alist
	interval = n // 2
	# left_list = alist[:interval]
	# right_list = alist[interval:]
	left_list = mergeSort(alist[:interval])
	right_list = mergeSort(alist[interval:])

	left_point = 0
	right_point = 0
	result = []

	while left_point < len(left_list) and right_point < len(right_list):
		if left_list[left_point] <= right_list[right_point]:
			result.append(left_list[left_point])
			left_point += 1
		else:
			result.append(right_list[right_point])
			right_point += 1
	result += left_list[left_point:]
	result += right_list[right_point:]
	return result


if __name__ == '__main__':
	li = [54,26,93,17,77,31,44,55,20]
	print(li)
	result = mergeSort(li)
	print(result)