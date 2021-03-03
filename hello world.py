class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def recur(l,r,s):
            if l==n and r==n: #终止条件
                ans.append(s)
                return
            #每一层的变化：
            if l<n: recur(l+1,r,s+"(") #只要左括号数量不超过n，左括号就可以任意加
            if r<l: recur(l,r+1,s+")") #只有当右括号数量小于左括号数量时，才可以加右括号
        recur(0,0,"")  #递归调用
        return ans
