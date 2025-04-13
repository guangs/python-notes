# https://www.workat.tech/problem-solving/practice/binary-search-tree-iterator
# Medium
# ./resources/007-binary-search-tree-iterator.png



# This is the Node class definition

from typing import Optional, Generator
class Node:
	def __init__(self, data=0, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right
	
	def __repr__(self):
		return str(self.data)



class BSTIterator:

	def __init__(self, root: Node, *args, **kwargs):
		self.node = root
		self.stack = []
	
	def hasNext(self) -> bool:
		return self.stack or self.node

	def next(self) -> Optional[Node]:
		while self.node:
			self.stack.append(self.node)
			self.node = self.node.left
		if self.stack:
			self.node = self.stack.pop()
			node = self.node
			self.node = node.right
			return node
		else:
			return None

	
	def __str__(self):
		return str(self.node.data)



class PreOrderIterator:

	def __init__(self, root: Node, *args, **kwargs):
		self.node = root
		self.stack = []

	# preorder traversal
	def __iter__(self) -> Generator[Node]:
		while self.stack or self.node:
			if self.node:
				yield self.node
				self.stack.append(self.node)
				self.node = self.node.left
			else:
				self.node = self.stack.pop()
				self.node = self.node.right
	
	def __str__(self):
		return str(self.node.data)


class InOrderIterator:

	def __init__(self, root: Node, *args, **kwargs):
		self.node = root
		self.stack = []

	# inorder traversal
	def __iter__(self) -> Generator[Node]:
		while self.stack or self.node:
			if self.node:
				self.stack.append(self.node)
				self.node = self.node.left
			else:
				self.node = self.stack.pop()
				yield self.node
				self.node = self.node.right
	
	def __str__(self):
		return str(self.node.data)
	

class PostOrderIterator:

	def __init__(self, root: Node, *args, **kwargs):
		self.node = root
		self.stack = []
		self.visited = set()

	# postorder traversal
	def __iter__(self) -> Generator[Node]:
		while self.stack or self.node:
			if self.node:
				self.visited.add(self.node)
				self.stack.append(self.node)
				if self.node.right:
					self.stack.append(self.node.right)
				self.node = self.node.left
			else:
				self.node = self.stack.pop()
				if self.node in self.visited:
					yield self.node
					self.node = None
	
	def __str__(self):
		return str(self.node.data)


def preorder(node: Optional[Node]):
	if node:
		print(node.data)
		preorder(node.left)
		preorder(node.right)

def preorder_iterative(node: Optional[Node]):
	stack = []
	while stack or node:
		if node:
			print(node.data)
			stack.append(node)
			node = node.left
		else:
			node = stack.pop()
			node = node.right

def preorder_iterative2(node: Optional[Node]):
	stack = [node]
	while stack:
		node = stack.pop()
		print(node.data)
		if node.right:
			stack.append(node.right)
		if node.left:
			stack.append(node.left)

def inorder(node: Optional[Node]):
	if node:
		inorder(node.left)
		print(node.data)
		inorder(node.right)

def inorder_iterative(node: Optional[Node]):
	stack = []
	while stack or node:
		if node:
			stack.append(node)
			node = node.left
		else:
			node = stack.pop()
			print(node.data)
			node = node.right

def postorder(node: Optional[Node]):
	if node:
		postorder(node.left)
		postorder(node.right)
		print(node.data)

def postorder_iterative(node: Optional[Node]):
	stack = []
	visited_node = []
	while stack or node:
		if node:
			visited_node.append(node)
			stack.append(node)
			if node.right:
				stack.append(node.right)
			node = node.left
		else:
			node = stack.pop()
			# 2nd time visit, process node
			if node in visited_node:
				print(node.data)
				node = None

def postorder_iterative2(node: Node) -> None:
    stack = []
    last_visited = None
    while stack or node:
        if node:
            stack.append(node)
            node = node.left  # 继续处理左子树
        else:
            peek_node = stack[-1]  # 查看栈顶节点
            # 如果右子树存在且未被访问，则处理右子树
            if peek_node.right and last_visited != peek_node.right:
                node = peek_node.right
            else:
                # 访问当前节点
                print(peek_node.data)
                last_visited = stack.pop()

def levelorder(node: Optional[Node]):
	if node:
		queue = [node]
		while queue:
			node = queue.pop(0)
			print(node.data)
			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)

# BST
#  2 
# 1 4 
#   3 5
#      7

n2 = Node(2)
n2.data = 2
n1 = Node(1)
n1.data = 1
n3 = Node(3)
n3.data = 3
n4 = Node(4)
n4.data = 4
n5 = Node(5)
n5.data = 5
n7 = Node(7)
n7.data = 7

n2.left = n1
n2.right = n4
n1.left = None
n1.right = None
n4.left = n3
n4.right = n5
n3.left = None
n3.right = None
n5.left = None
n5.right = n7
n7.left = None
n7.right = None

root = n2

# n4.right = n7

# BSTIterator

# bst = BSTIterator(root)

# while bst.hasNext():
# 	n = bst.next()
# 	print(n)

postorder_iterative(root)

print('-' * 10)

bst2 = PostOrderIterator(root)
for n in bst2:
	print(n)