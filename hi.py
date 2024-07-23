class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def preOrder(self,root):
        if(root==None):
            return
        print(root.data,end=" ")
        root.preOrder(root.left)
        root.preOrder(root.right)
    def postOrder(self,root):
        if(root==None):
            return
        root.postOrder(root.left)
        root.postOrder(root.right)
        print(root.data, end=" ")
    def inOrder(self,root):
        if(root==None):
            return
        root.inOrder(root.left)
        print(root.data,end=" ")
        root.inOrder(root.right)
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
root.preOrder(root)
print()
root.postOrder(root)
print()
root.inOrder(root)
print()