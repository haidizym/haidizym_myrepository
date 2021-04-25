class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:  #因为括号成对出现，如果括号数不为偶数肯定为假
            return False
        
        pairs = {       #用一个字典实现左右括号的对应与匹配，其中右括号为键，左括号为值
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = list()  #工作栈，先出现的括号后匹配
        for ch in s:  #遍历字符串每一个括号
            if ch in pairs: #只有当右括号出现在字符串的时候才去栈里匹配，否则把出现的左括号加到栈末尾
                if not stack or stack[-1] != pairs[ch]:  #只有栈不为空，且栈的倒数第一个与正数第一个相匹配，才能继续下去，否则返回假
                    return False
                stack.pop() #匹配成功一对，就从栈中弹出
            else:
                stack.append(ch)  #
        
        return not stack  #只有最终栈为空，才为真
