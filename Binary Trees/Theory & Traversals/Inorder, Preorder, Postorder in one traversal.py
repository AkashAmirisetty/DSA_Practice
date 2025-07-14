# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def tree_traversal(self, root):
        #your code goes here
        pre=[]
        ino=[]
        pos=[]
        if not root:
            return [pre, ino, pos]
        st=[(root,1)]

        while st:
            node,state=st.pop()
            if state==1:
                pre.append((node.data))
                st.append((node,2))
                if node.left:
                    st.append((node.left,1))

            elif state==2:
                ino.append((node.data))
                st.append((node,3))
                if node.right:
                    st.append((node.right,1))
            else:
                pos.append((node.data))
        return [ino,pre,pos]
