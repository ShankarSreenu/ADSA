class Solution:
    def longestPalindrome(self, string: str) -> str:
        N=len(string)
        even_res=""
        odd_res=""
        max1=1
        max2=1
        if N==1:
            return string
        if N==2:
            if string[0]==string[1]:
                return string
            else:
                return string[0]
        for k in range(0,N-1):
            i,j=k,k
            odd_count=1
            even_count=0
            ans1=""
            ans2=string[k]

            p,q=0,2*k
            s,t=0,2*k+1
            l,h=k,k+1
            
            if k>=N//2:
                p=2*k-N+1
                q=N-1
            if k>=N//2:
                s=2*k-N+1
                t=N-1

            while l>=s and h<=t:
                if string[l]==string[h]:
                    ans1=string[l]+ans1+string[h]
                    l=l-1
                    h=h+1
                    even_count=even_count+2
                else:
                    break

            while i-1>=p and j+1<=q:
                if string[i-1]==string[j+1]:
                    ans2=string[i-1]+ans2+string[j+1]
                    i=i-1
                    j=j+1
                    odd_count=odd_count+2
                else:
                    break
            if len(ans1)>=max1:
                max1=len(ans1)
                even_res=ans1

            if len(ans2)>=max2:
                max2=len(ans2)
                odd_res=ans2
        
        if max1==1 and max2==1:
            return odd_res
        if max1>max2:
            return even_res
        else:
            return odd_res
    
