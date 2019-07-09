#实现栈，他是一个后进先出的存储结构

class Stack(object):
	"""docstring for Stack"""
	def __init__(self):
		self.__list = []

	def push(self, item):   #尾部添加
		self.__list.append(item)

	def pop(self):
		'''弹出栈顶元素'''   #尾部出栈
		return self.__list.pop()

	def peek(self, item):
		'''取出栈顶元素'''
		if self.__list is None:
			return None
		else:
			return self.__list[-1]

	def is_empty(self):
		return self.__list == []

	def size(self):
		return len(self.__list)


if __name__ == '__main__':
	s = Stack()
	s.push(1)
	s.push(2)
	s.push(3)
	s.push(4)
	print(s.is_empty())
	print(s.size())
	print(s.pop())
	print(s.pop())
	print(s.pop())
	print(s.pop())