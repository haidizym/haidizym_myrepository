class Solution:
    def isAnagram(self, s: str, t: str) -> bool:  #法2：哈希表，
        if len(s) != len(t): return False
        counts = [0] * 26
        for i in range(len(s)):
            counts[ord(s[i]) - ord("a")] += 1 # 如果S列表中如果存在a,则加1 
            counts[ord(t[i]) - ord("a")] -= 1 # t列表中存在a,则减1。
        for i in counts:
            if i != 0:
                return False
        return True
