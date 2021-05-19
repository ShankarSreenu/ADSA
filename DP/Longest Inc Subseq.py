#Bottom Up Dp
# ex 0 5 6 1 2 7
#    1 1 1 1 1 1
#    1 2 1 1 1 1
#    1 2 3 1 1 1
#    1 2 3 3 1 1
#    1 2 3 3 4 1
#    1 2 3 3 4 4
class Solution:
    def lengthOfLIS(self, arr) -> int:
        n=len(arr)
        ans=[1]*n #initilising array with 1
        for i in range(0,n):
            best=0
            for j in range(0,i):
                if arr[i]>arr[j]:
                    best=max(best,ans[j])
            ans[i]=best+1
        return max(ans)
