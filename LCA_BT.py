# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        elif root == p:
            return root
        elif root == q:
            return root
        l = self.lowestCommonAncestor(root.left , p , q)
        r = self.lowestCommonAncestor(root.right , p , q)
        
        if l and r :
            return root
        else:
            if l:
                return l
            else:
                return r
        
        
# elegant code for the same logic

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None or root==p or root == q:
            return root
        l = self.lowestCommonAncestor(root.left , p , q)
        r = self.lowestCommonAncestor(root.right , p , q)
        
        if l and r :
            return root
        return l if l else r
        
        
# more elegant soln 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root in (None , p , q):
            return root
        l = self.lowestCommonAncestor(root.left , p , q)
        r = self.lowestCommonAncestor(root.right , p , q)
        
        if l and r :
            return root
        return l if l else r
        
        
        