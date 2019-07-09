class Node(object):
	"""docstring for Node"""
	def __init__(self, item):
		self.elem = item
		self.lchild = None
		self.rchild = None


class Tree(object):
	"""docstring for Tree"""
	def __init__(self):
		self.root = None
	def treeAdd(self, item):
		node = Node(item)
		#这边是特殊情况---根节点为空的情况
		if self.root is None:
			self.root = node
			return
		queue = []
		queue.append(self.root)

		while queue:
			cur_node = queue.pop(0)
			if cur_node.lchild is None:
				cur_node.lchild = node
				return
			else:
				queue.append(cur_node.lchild)

			if cur_node.rchild is None:
				cur_node.rchild = node
				return
			else:
				queue.append(cur_node.rchild)


	def breadthTravel(self):
		if self.root is None:
			return
		queue = [self.root]
		while queue:
			cur_node = queue.pop(0)
			print(cur_node.elem, end=" ")
			if cur_node.lchild is not None:
				queue.append(cur_node.lchild)
			if cur_node.rchild is not None:
				queue.append(cur_node.rchild)

	def preorder(self, node):
		'''先序遍历'''
		if node is None:
			return
		print(node.elem, end=" ")

		self.preorder(node.lchild)
		self.preorder(node.rchild)



	def inorder(self, node):
		'''中序遍历'''
		if node is None:
			return
		self.inorder(node.lchild)
		print(node.elem, end=" ")
		self.inorder(node.rchild)

	def postorder(self, node):
		'''后序遍历'''
		if node is None:
			return
		self.postorder(node.lchild)
		self.postorder(node.rchild)
		print(node.elem, end=" ")
if __name__ == '__main__':
	tree = Tree()
	tree.treeAdd(0)
	tree.treeAdd(1)
	tree.treeAdd(2)
	tree.treeAdd(3)
	tree.treeAdd(4)
	tree.treeAdd(5)
	tree.treeAdd(6)
	tree.treeAdd(7)
	tree.treeAdd(8)
	tree.treeAdd(9)


	tree.breadthTravel()
	print(" ")
	tree.preorder(tree.root)
	print(" ")
	tree.inorder(tree.root)
	print(" ")
	tree.postorder(tree.root)
	print(" ")