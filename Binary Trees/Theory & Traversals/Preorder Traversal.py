# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self,root,arr):
        if root is None:
            return 
        arr.append(root.val)
        self.helper(root.left,arr)
        self.helper(root.right,arr)
        
        
    def preorder(self, root):
        #your code goes here
        arr=[]
        self.helper(root,arr)
        return arr