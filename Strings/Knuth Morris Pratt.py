#not correct solution
def kmp(s,p):
    #construction of suffix and prifix table
    i,j=0,1
    table=[0]*len(p)
    while i<len(p) and j<len(p):
        if p[i]==p[j]:
            table[j]=i+1
            i=i+1
        j=j+1
    
    i,j=0,0
    ans=0
    while i<len(s) and j<len(p):
        if s[i]==p[j]:
            i=i+1
            j=j+1

        else:
            if table[j-1]==0:
                j=0
            else:
                j=table[j-1]
            if s[i]!=p[j]:
                i=i+1
        if j==len(p):
            ans=ans+1
            i=i-j+1
            j=0
        

    return ans

s=input()
p=input()
if len(p)>len(s):
    temp=s
    s=p
    p=temp
print(kmp(s,p))
