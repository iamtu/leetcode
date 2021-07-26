from __future__ import print_function
class Node:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

def insert(root, item):
    '''
    insert a node with item to the BST with root
    '''
    if not root:
        root = Node(item)
        return root
    if item > root.val:
        root.right = insert(root.right, item)
        root.right.parent = root
    elif item < root.val:
        root.left = insert(root.left, item)
        root.left.parent = root
    else:
        print ('[INFO]', item, 'is in the tree. ignore it.')
    return root

def delete(root, item):
    '''
    delete a node with item from a BST
    return root of the BST
    '''
    if not root:
        return None
    if item < root.val:
        root.left = delete(root.left, item)
    elif item > root.val:
        root.right = delete(root.right, item)
    else: # found item to delete root.val == item:
        if root.left and root.right:
            node = find_min(root.right)
            root.val = node.val
            root.right = delete(root.right, root.val)
        else:
            # do not have left or right
            if root.left is None: #if no root.left, go to root.right
                root = root.right
            elif root.right is None: #if no root.right, go to root.left
                root = root.left
    return root


def inorder(root):
    '''
    traversal the tree inorder
    '''
    if not root:
        return
    inorder(root.left)
    print (root.val, end=' ')
    inorder(root.right)

def find(root, item):
    '''
    if a Node with item in the BST root
    return None if not found, esle return found Node
    '''
    if not root or root.val == item:
        return root
    if item > root.val:
        return find(root.right, item)
    else:
        return find(root.left, item)

def find_min(root):
    '''
    find the min node of a BST root
    it's the left most node from the root
    '''
    if not root:
        return None
    cur = root
    while cur.left:
        cur = cur.left
    return cur
def find_max(root):
    '''
    find the max node of a BST root
    it's the right most node from the root
    '''
    if not root:
        return None
    cur = root
    while cur.right:
        cur = cur.right
    return cur

def successor(root, val):
    '''
    find sucessor of the node with val in the BST root
    return None if not found, else return sucessor Node
    '''
    #first found the node with val
    node = find(root, val)
    if not node:
        return None
    if node.right:
        return find_min(node.right)
    else:
        p = node.parent
        while p and node == p.right:
            node = p
            p = p.parent
        return p

def predcessor(root, val):
    '''
    find the predcessor of a node with val in the BST root
    return None if not found, else return predcessor Node
    '''
    node = find(root, val)
    if not node:
        return
    if node.left:
        return find_max(root.left, val)
    else:
        p = node.parent
        while p and node == p.left:
            node = p
            p = p.parent
        return p

def print_tree(root, val="val", left="left", right="right"):
    ''' 
        https://stackoverflow.com/a/65865825/7197528
    '''
    def display(root, val=val, left=left, right=right):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if getattr(root, right) is None and getattr(root, left) is None:
            line = '%s' % getattr(root, val)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if getattr(root, right) is None:
            lines, n, p, x = display(getattr(root, left))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if getattr(root, left) is None:
            lines, n, p, x = display(getattr(root, right))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = display(getattr(root, left))
        right, m, q, y = display(getattr(root, right))
        s = '%s' % getattr(root, val)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    lines, *_ = display(root, val, left, right)
    for i in range(len(lines)):
        print(i, lines[i])

if __name__ == '__main__':
    root = None
    for x in [50, 30, 55, 25, 35, 10, 20, 23, 55, 53, 31, 37, 60, 62]:
        root = insert(root, x)
    print_tree(root)

    root = delete(root, 30)
    print_tree(root)


    # node = find(root, 30)
    # if node:
    #     print ("Found a node. val ", node.val)
    #     if node.parent:
    #         print ("with parent val: ", node.parent.val)
    # else:
    #     print ("NOT FOUND")
    

    # min_node = find_min(root)
    # print (min_node.val)
    # max_node = find_max(root)
    # print (max_node.val)

    # item = 31
    # suc = successor(root, item)
    # if suc:
    #     print ("found succ of item ", item , 'is', suc.val)
    # else:
    #     print (item, "is maximum, no successor")
    
    # item = 62
    # suc = successor(root, item)
    # if suc:
    #     print ("found succ of item ", item , 'is', suc.val)
    # else:
    #     print (item, "is maximum, no successor")
    
    # item = 62
    # pred = predcessor(root, item)
    # if pred:
    #     print ("found pred of item ", item , 'is', pred.val)
    # else:
    #     print (item, "is mininum, no predcessor")

    # item = 10
    # pred = predcessor(root, item)
    # if pred:
    #     print ("found pred of item ", item , 'is', pred.val)
    # else:
    #     print (item, "is mininum, no predcessor")

    # root = Node(10)
    # root.left = Node(7)
    # root.right = Node(9)
    # root.left.left = Node(4)
    # root.left.right = Node(5)
