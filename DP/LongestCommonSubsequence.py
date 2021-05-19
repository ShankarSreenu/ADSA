#basic recursion
p="abcss"
q="as"

def rec_lcs(p,q,i,j):
    if i==len(p) or j==len(q):
        return 0
    
    elif p[i]==q[j]:
        return 1+rec_lcs(p,q,i+1,j+1)
    else:
        return max(rec_lcs(p,q,i,j+1),rec_lcs(p,q,i+1,j))

#recursion+memorisations bottom up
memo=[[0]*len(p) for i in range(0,len(q))]
def memo_lcs():
    return 0


#top down dp
dp=[[0]*(len(p)+1) for i in range(0,len(q)+1)]
def dp_lcs(p,q):
    top=-1
    for i in range(1,len(q)+1):
        for j in range(1,len(p)+1):
            if p[j-1]==q[i-1]:
                dp[i][j]=dp[i-1][j-1]+1
            if p[j-1]!=q[i-1]:
               dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    
    return dp[top][top]
 



#memo+top down dp
ans=dp_lcs(p,q)
print(ans)