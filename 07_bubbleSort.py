#冒泡排序
#冒泡排序有两种实现方式，通过i和j的取值变化而不同

#第一种
def bubbleSort01(alist):
	for j in range(0, len(alist)-1):
		count = 0
		for i in range(0, len(alist)-1-j):
			if alist[i] > alist[i+1]:
				alist[i+1], alist[i] = alist[i], alist[i+1]
				count += 1
		if count == 0:
			break

def bubbleSort02(alist):
	for j in range(len(alist)-1, 0, -1):
		count = 0
		for i in range(0, j):
			if alist[i] > alist[i+1]:
				alist[i+1], alist[i] = alist[i], alist[i+1]
				count += 1
		if count == 0:
			break



if __name__ == '__main__':
	li = [54,26,93,17,77,31,44,55,20]
	print(li)
	bubbleSort01(li)
	print(li)

	print("-----------------------")
	
	li2 = [54,26,93,17,77,31,44,55,20]
	print(li2)
	bubbleSort02(li2)
	print(li2)
