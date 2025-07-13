# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    # def helper(self,root,arr):
        # if root is None:
        #     return
        # self.helper(root.left,arr)
        # self.helper(root.right,arr)
        # arr.append(root.data)
    def postorder(self, root):
        #your code goes here
        # arr=[]
        # self.helper(root,arr)
        # return arr

        # Iterative approach
        ans=[]
        stack=[]
        if root:
            stack.append(root)
        while stack:
            node=stack.pop()
            ans.append(node.data)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        ans.reverse()
        return ans



