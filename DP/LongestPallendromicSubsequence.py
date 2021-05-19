class Solution:
    def longestPalindromeSubseq(self, p: str) -> int:
        q=p[::-1]
        top=-1
        dp=[[0]*(len(p)+1) for i in range(0,len(q)+1)]
        for i in range(1,len(q)+1):
            for j in range(1,len(p)+1):
                if p[j-1]==q[i-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                if p[j-1]!=q[i-1]:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[top][top]
 
