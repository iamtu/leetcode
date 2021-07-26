class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ret = [[root.val]]
        q = [root, '\n']
        row = []
        c = 0
        while q:
            c += 1
            cur = q.pop(0)
            if cur == '\n':
                if not q:
                    break
                q.append('\n')
                ret.append(row)
                row = []
                continue
            row.append(cur.val)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

        return ret

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    s = Solution()
    print(s.levelOrder(root))