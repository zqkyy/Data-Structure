#双向循环链表

class Node(object):
	"""docstring for Node"""
	def __init__(self, item):
		self.elem = item
		self.prev = None
		self.next = None
class doubleLinkList(object):
	"""docstring for doubleLinkList"""

	def __init__(self, node = None):
		self.__head = node


	def is_empty(self):
		''' 链表是否为空'''
		return self.__head == None

	def length(self):
		'''链表长度'''
		#加入cur游标，用来移动遍历节点
		if self.__head == None:
			return 0
		else:
			cur = self.__head
			count = 0
			while cur != None:
				count += 1
				cur = cur.next
			return count


	def travel(self):
		'''遍历整个链表'''
		cur = self.__head
		while cur != None:
			print(cur.elem, end=" ")
			cur = cur.next
		print("")


	def add(self, item):
		'''链表头部添加元素'''
		node = Node(item)
		if self.is_empty():
			self.__head = node
		node.next = self.__head
		self.__head.prev = node
		self.__head = node


	def append(self, item):
		'''链表尾部添加元素'''
		node = Node(item)
		if self.is_empty():
			self.__head = node
		else:
			cur = self.__head
			while cur.next != None:
				cur = cur.next
			cur.next = node
			node.prev = cur


	def insert(self, pos, item):
		"""
		指定位置添加元素
		:param pos 从0开始 
		"""  
		#加入元素的中要求的位置 要替换原先在链表中的位置   1，2，3 ---加入(4,2)---1,2,4,3
		node = Node(item)
		if pos <= 0:
			self.add(item)
		elif pos > (self.length()-1):
			self.append(item)
		else:
			pre = self.__head  #这边用pre可以，同时呢，因为这边是双向列表，所以使用cur也可以
			count = 0
			while count < (pos-1):
				pre = pre.next
				count += 1
			pre.next.prev = node
			node.next = pre.next
			pre.next = node
			node.prev = pre


	def search(self, item):
		'''查找节点是否存在'''
		cur = self.__head
		while cur != None:
			if cur.elem == item:
				return True
			else:
				cur = cur.next
		return False


	def remove(self, item):
		'''删除节点'''
		cur = self.__head

		while cur.next != None:
			if cur.elem == item:
				if cur == self.__head:
					self.__head = cur.next
					cur.next.prev = None
				else:
					cur.prev.next = cur.next
					cur.next.prev = cur.prev
				return
			else:
				cur = cur.next
		if cur.elem == item:
			cur.prev.next = None



if __name__ == '__main__':
	sll = doubleLinkList()
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
	sll.append(7)
	sll.add(8)
	sll.travel()
	sll.insert(10, 10)
	print(sll.is_empty())
	print(sll.length())
	sll.travel()

	sll.insert(0, 100)
	sll.insert(-1, 200)
	sll.insert(10, 300)
	sll.travel()
	# print(sll.search(3))

	sll.remove(200)
	sll.travel()
	sll.remove(10)
	sll.travel()
	sll.remove(3)
	sll.travel()


		