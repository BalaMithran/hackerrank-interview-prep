# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    maxi = 0
    def diameterhelper(self , root , maxi):
        if not root: return 0 
        lh = self.diameterhelper(root.left , maxi)
        rh = self.diameterhelper(root.right , maxi)
        self.maxi = max(self.maxi , lh+rh)
        return 1+max(lh , rh)
    def diameterOfBinaryTree(self, root):
        self.diameterhelper(root , self.maxi)
        return self.maxi
        """
        :type root: TreeNode
        :rtype: int
        """
        