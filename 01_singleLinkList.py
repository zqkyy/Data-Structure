
#初始化节点的类
class Node(object):
	"""docstring for Node"""
	def __init__(self, elem):
		self.elem = elem
		self.next = None

class singleLinkList(object):
	"""docstring for singleLinkList"""
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
		node.next = self.__head
		self.__head = node

	def append(self, item):
		'''链表尾部添加元素'''
		node = Node(item)
		if self.__head == None:
			self.__head = node
		else:
			cur = self.__head
			while cur.next != None:
				cur = cur.next
			cur.next = node

	def insert(self, pos, item):
		"""
		指定位置添加元素
		:param pos 从0开始 
		"""  
		#加入元素的中要求的位置 要替换原先在链表中的位置   1，2，3 ---加入(4,2)---1,2,4,3
		node = Node(item)
		if pos <= 0:
			self.add(item)
		elif pos > (self.length()-1): #这里不能包含等号
			self.append(item)
		else:
			pre = self.__head
			count = 0
			while count < pos:
				count += 1
				pre = pre.next
			#退出循环后，pre指向pos-1位置
			node.next = pre.next 
			pre.next = node


	def remove(self, item):
		'''删除节点'''
		pre = None
		cur = self.__head
		while cur != None:
			if cur.elem == item:
				#先判断此节点是否是头节点
				if cur == self.__head:
					self.__head = cur.next  #处理好头节点之后，尾节点情况是也能包括在内
				else:
					pre.next = cur.next
				break
			else:
				pre = cur
				cur = cur.next

	def search(self, item):
		'''查找节点是否存在'''
		cur = self.__head
		while cur != None:
			if cur.elem == item:
				return True
			else:
				cur = cur.next
		return False	

if __name__ == '__main__':
	sll = singleLinkList()
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
	sll.insert(10, 10)
	print(sll.is_empty())
	print(sll.length())
	sll.travel()
	sll.insert(-1, 200)
	sll.travel()

	sll.remove(200)
	sll.travel()

	sll.remove(3)
	sll.travel()


