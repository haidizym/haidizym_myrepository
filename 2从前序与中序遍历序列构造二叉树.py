# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder)!=len(inorder): return None
        n=len(preorder)
        #中序遍历构建哈希表，以便每次快速找到先序遍历第一个元素在中序遍历中的位置
        hashtable={c:i for i,c in enumerate(inorder)} 
        def helper(preL,preR,inL,inR):#递归函数需要传入先序遍历和中序遍历的左右边界参数
            if preL>preR:return None #递归终止条件
            pindex=hashtable[preorder[preL]]
            root=TreeNode(preorder[preL])#每次把先序遍历第一个节点作为根节点存储成树
            root.left=helper(preL+1,pindex-inL+preL,inL,pindex-1) #递归调用更新参数
            root.right=helper(pindex-inL+preL+1,preR,pindex+1,inR)
            return root
        return helper(0,n-1,0,n-1)
