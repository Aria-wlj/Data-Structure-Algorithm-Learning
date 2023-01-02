# from https://www.tutorialspoint.com/python_data_structure/python_tree_traversal_algorithms.htm

class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    # Insert Node
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # Print Tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()


"""
Recursive, Inorder
"""
def inTra(root):
    output = []
    node = root
    if node:
        output = inTra(node.left)
        output.append(node)
        output = output + inTra(node.right)
    return output


'''
Recursive, postorder
'''
def postTra(root):
    output = []
    node = root
    if node:
        output = postTra(node.left)
        output = output + postTra(node.right)
        output.append(node)
    return output


if __name__ == '__main__':
    root = Node(27)
    root.insert(14)
    root.insert(35)
    root.insert(10)
    root.insert(19)
    root.insert(31)
    root.insert(42)


    for i in inTra(root):
        print(i.data)
    print('-----------------------')
    for i in postTra(root):
        print(i.data)
