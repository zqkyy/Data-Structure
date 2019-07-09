#实现栈，他是一个后进先出的存储结构

class Queue(object):
	"""docstring for Stack"""
	def __init__(self):
		self.__list = []

	def enqueue(self, item):#尾部添加
		self.__list.append(item)

	def dequeue(self):      #头部出队列
		'''弹出栈顶元素'''
		return self.__list.pop(0)

	def is_empty(self):
		return self.__list == []

	def size(self):
		return len(self.__list)


if __name__ == '__main__':
	s = Queue()
	s.enqueue(1)
	s.enqueue(2)
	s.enqueue(3)
	s.enqueue(4)
	print(s.is_empty())
	print(s.size())
	print(s.dequeue())
	print(s.dequeue())
	print(s.dequeue())
	print(s.dequeue())