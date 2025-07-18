# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root):
        #your code goes here
        ans=[]
        if not root:
            return ans
        q=deque([root])
        while q:
            level=[]
            for i in range(len(q)):
                node=q.popleft()
                level.append(node.data)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(level)
        return ans