class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = [] #用来放置答案序列的初始空列表
        def backtrack(S, left, right):  #加括号的递归函数
            if len(S) == 2 * n:  #当n对括号加足时，就结束，返回括号序列列表
                ans.append(''.join(S))
                return
            if left < n:   #只要左括号还没有加够就可以任意加左括号
                S.append('(')
                backtrack(S, left+1, right)  #每增加一个左括号，左括号数记录加1，
                S.pop()  
            if right < left:  #只要左括号数还小于右括号数，就可以加右括号
                S.append(')')
                backtrack(S, left, right+1)
                S.pop()

        backtrack([], 0, 0)
        return ans
