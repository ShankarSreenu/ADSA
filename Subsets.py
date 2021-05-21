class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
         n=len(nums)
         if len(nums)==0:
            return [[]]
         ans=[[]]
         for i in range(1,2**n):
            mask="{0:b}".format(i)
            mask=(n-len(mask))*"0"+mask
            temp=[]
            for j in range(0,len(nums)):
                if mask[j]=='1':
                    temp.append(nums[j])
            ans.append(temp)
         return ans
