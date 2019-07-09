#实现栈，他是一个后进先出的存储结构

class deQueue(object):
	"""docstring for Stack"""
	def __init__(self):
		self.__list = []

	def add_front(self, item):#头部添加
		self.__list.insert(0, item)

	def add_rear(self, item):#尾部添加
		self.__list.append(item)

	def pop_front(self):      #头部出队列
		'''弹出栈顶元素'''
		return self.__list.pop(0)

	def pop_rear(self):      #尾部出队列
		'''弹出栈顶元素'''
		return self.__list.pop()

	def is_empty(self):
		return self.__list == []

	def size(self):
		return len(self.__list)


if __name__ == '__main__':
	s = deQueue()
	s.add_front(1)
	s.add_front(2)
	s.add_rear(3)
	s.add_rear(4)
	print(s.is_empty())
	print(s.size())
	print(s.pop_front())
	print(s.pop_front())
	print(s.pop_rear())
	print(s.pop_rear())