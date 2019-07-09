#单向循环列表

class Node(object):
	"""docstring for Node"""
	def __init__(self, item):
		self.elem = item
		self.next = None

class danlaibiao(object):
	"""docstring for singleCycleLinkList"""
	def __init__(self, node=None):
		self.__header = node
		if node:
			node.next = node

	def is_empty(self):
		'''判断单向循环列表是否为空'''
		return self.__header == None 

	def length(self):
		'''单向循环列表的长度'''
		if self.is_empty():
			return
		count  = 1
		cur = self.__header
		while cur.next != self.__header:
			cur = cur.next
			count += 1 
		return count

	def travel(self):
		'''单向循环列表遍历'''
		if self.__header == None:
			return
		cur = self.__header
		while cur.next != self.__header:
			print(cur.elem, end=" ")
			cur = cur.next
		print(cur.elem)

	def add(self, item):
		node = Node(item)
		if self.__header == None:
			self.append(item)
		cur = self.__header
		while cur.next != self.__header:
			cur = cur.next
		#循环结束，cur指向尾节点
		node.next = self.__header
		self.__header = node
		cur.next = node



	def append(self, item):
		'''单向循环列表的尾插法'''
		node = Node(item)
		if self.is_empty():
			self.__header = node
			node.next = node
		else:
			cur = self.__header
			while cur.next != self.__header:
				cur = cur.next
			cur.next = node
			node.next = self.__header

	def insert(self, pos, item):
		node = Node(item)
		if pos <= 0:
			self.add(item)
		elif pos > (self.length()-1):
			self.append(item)
		else:
			pre = self.__header
			count = 0
			while count < (pos-1):
				pre = pre.next
				count += 1
			node.next = pre.next
			pre.next = node

	def search(self, item):
		if self.__header == None:
			return False
		cur = self.__header
		while cur.next != self.__header:
			if cur.elem == item:
				return True
			else:
				cur = cur.next
		if cur.elem == item:
			return True
		else:
			return False

	def remove(self, item):
		if self.is_empty():
			return
		pre = None
		cur = self.__header
		while cur.next != self.__header:
			if cur.elem == item:
				if cur == self.__header: 
					#多个节点，然后在头部删除。还需要找到尾部节点，定位到原本的第二个节点
					#先求尾节点
					reer = self.__header
					while reer.next != self.__header:
						reer = reer.next
					self.__header = cur.next
					reer.next = cur.next	
				else:
					#中间节点
					pre.next = cur.next
				return
			else:
				pre = cur
				cur = cur.next

		#退出循环，即到尾部---多个节点，在尾部删除，同时这边也要考虑列表只有一个节点的情况（因为一个节点也是尾节点）
		if cur.elem == item:
			if cur == self.__header:
				self.__header = None
			else:
				pre.next = self.__header

# def ceshi():   #返回的是None，不是False
# 	return


if __name__ == '__main__':
	sll = danlaibiao()
	print(sll.is_empty())
	print(sll.length())

	sll.append(1)
	print(sll.is_empty())
	print(sll.length())

	sll.append(2)
	sll.append(3)
	sll.append(4)
	sll.append(5)
	sll.append(6)

	sll.add(7)
	print(sll.is_empty())
	print(sll.length())
	sll.travel()

	sll.insert(0, 100)
	sll.insert(-1, 200)
	sll.insert(10, 300)
	sll.travel()
	print(sll.search(3))




