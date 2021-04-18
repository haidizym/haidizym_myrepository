class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        stack = []
        # 当先遇到 `)` 需要先弹出元素，这里可以防止报错
        # 当遇到的 `()` 的字符时，-1 在计算长度的时候，发挥作用
        stack.append(-1)
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        return max_len
