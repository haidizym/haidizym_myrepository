class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(queens,xy_dif,xy_sum):
        #传三个参数，每一行的第几列是皇后，该皇后位置的行号与列号之差，之和，分别代表撇和捺的位置
            p=len(queens)
            if p==n:
                result.append(queens)
                return
            for q in range(n):
            #对于每一行的列号进行循环，如果该列号不在三个参数里，就更新三个参数，该位置可以放一个皇后
                if q not in queens and p-q not in xy_dif and p+q not in xy_sum:
                    dfs(queens+[q],xy_dif+[p-q],xy_sum+[p+q])
        result=[]
        dfs([],[],[])
        #result里放的依次是每一行的皇后所在列，对于答案里的每一个列号，前放点，后放点，本身放Q
        return [["."*i +"Q"+"."*(n-i-1) for i in sol] for sol in result]
