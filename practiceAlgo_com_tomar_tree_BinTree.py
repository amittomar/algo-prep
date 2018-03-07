from Queue import Queue
import sys


# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.right=None
#         self.left=None

class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # setData
    def setData(self, data):
        self.data = data

    # get data of node
    def getData(self):
        return self.data

    # get the left node
    def getLeftChild(self):
        return self.left

    # get the right node
    def getRightNOde(self):
        return self.right

    def insertleft(self, newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp = self.left
            self.left = temp

    def insertRight(self, newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.right = self.right
            self.right = temp

    # insert using level order traversal
    def insertInBinaryTreeUsingLevelOrder(root, data):
        newNode = BinaryTree(data)
        if root is None:
            root = newNode
            return root
        q = Queue()
        q.put_nowait(root)
        node = None
        while not q.empty():
            node = q.get_nowait()
            if data == node.getDate():
                return root
            if node.left is not None:
                q.put_nowait(node.left)
            else:
                node.left = newNode
                return root

            if node.right is not None:
                q.put_nowait(node.right)
            else:
                node.right = newNode
                return root

    def printLevelOrderTraversal(self, root):
        if root is not None:
            q = Queue()
            q.put_nowait(root)
            node = None

            while not q.empty():
                node = q.get_nowait()
                print node.getData()

                if node.left is not None:
                    q.put_nowait(node.left)

                if node.right is not None:
                    q.put_nowait(node.right)

    if __name__ == "__main__":
        tree = BinaryTree(1)
        # tree.insertInBinaryTreeUsingLevelOrder(1)
        tree.insertInBinaryTreeUsingLevelOrder(tree, 2)
        tree.insertInBinaryTreeUsingLevelOrder(tree, 3)
        tree.insertInBinaryTreeUsingLevelOrder(tree, 4)
        tree.insertInBinaryTreeUsingLevelOrder(tree, 5)
        tree.insertInBinaryTreeUsingLevelOrder(tree, 6)
        tree.insertInBinaryTreeUsingLevelOrder(tree, 7)
        tree.insertInBinaryTreeUsingLevelOrder(tree, 8)
        tree.insertInBinaryTreeUsingLevelOrder(tree, 9)
        tree.insertInBinaryTreeUsingLevelOrder(tree, 10)
        tree.insertInBinaryTreeUsingLevelOrder(tree, 11)
        tree.printLevelOrderTraversal(tree)
