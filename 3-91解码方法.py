class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0]*(n + 1) #dp[i]表示s从下标长度为i的字符串的方法总数
        dp[0] = 1
        dp[1] = 1 if s[0]!="0" else 0

        for i in range(2, n + 1):
    #当前位是否是0，如果是0，当前位不能进行一位数解码，并且只有当前一位是1或者2的时候才能够进行合法的两位数解码
            if s[i - 1] == '0':
                if 0 < int(s[i - 2]) <= 2:
                    dp[i] = dp[i - 2]
                else:
                    dp[i] = 0
    #如果当前位不是0，那么当前位的一位数解码肯定是合法的，
    #现在我们要讨论两位数解码是否也合法，于是我们查看当前位是否和前一位组成合法的两位数，
            else:
                if 10 < int(s[i - 2] + s[i - 1]) <= 26:
                    dp[i] = dp[i - 2] + dp[i - 1]
                else:
                    dp[i] = dp[i - 1]
        return dp[-1]
