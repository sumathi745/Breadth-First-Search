#Define a binary tree class, create the tree, and print the nodes in order by level 

 # 	  7
 #   / \
 #  4    6
 # / \  / \
 #1  2  3   5


 # output: 
 # 7
 # 4 6
 # 1 2 3 4

class Node(object):
	def __init__(self, val, left=None, right=None):
		self.left = left
		self.right = right
		self.val = val


def print_nodes_by_level(root):
	queue = []
	queue.append(root)
	print(root.val)
	
	

	while queue != []:
		root = queue[0]
		length = len(queue)
		print("\n")

		for i in range(0, length):
			node = queue.pop(0)

			if node.left:
				queue.append(root.left)
				print(node.left.val, end=" ")
			if node.right:
				queue.append(root.right) 
				print(node.right.val, end=" ")

		print("\n")

		


if __name__ == "__main__":
	node4 = Node(4)
	node6 = Node(6)
	root = Node(7, node4, node6)
	node6.left = Node(3)
	node6.right = Node(5)
	node4.left = Node(1)
	node4.right = Node(2)



	print_nodes_by_level(root)
	


