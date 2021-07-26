from __future__ import print_function
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Traveraser:
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        print (root.val, end=' ')
        self.inorder(root.right)

    def preorder(self, root):
        if not root:
            return
        print (root.val, end=' ')
        self.preorder(root.left)
        self.preorder(root.right)
    
    def postorder(self, root):
        if not root:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print (root.val, end=' ')

    def inorder_stack(self, root):
        if not root:
            return
        stack = []
        cur = root
        # if cur is null and stack is empty, algorithm return
        while (cur or stack):
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                print (cur.val, end=' ')
                cur = cur.right
        return

    def preorder_stack(self, root):
        if not root:
            return  
        stack = []
        cur = root
        while (cur or stack):
            if cur:
                print (cur.val, end = ' ')
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                cur = cur.right

    def postorder_stack(self, root):
        if not root:
            return
        stack = []
        cur = root
        while (cur or stack):
            return

if __name__ == '__main__':
    root = TreeNode('A')
    root.left = TreeNode('B')
    root.right = TreeNode('C')
    root.left.left = TreeNode('D')
    root.left.right = TreeNode('E', None, TreeNode('F'))

    traverser = Traveraser()
    # traverser.inorder(root)
    # print ('using stack')
    # traverser.inorder_stack(root)

    # traverser.preorder(root)
    # print ('')
    # traverser.preorder_stack(root)

    traverser.postorder(root)
    # print ('')
    # traverser.postorder_stack(root)