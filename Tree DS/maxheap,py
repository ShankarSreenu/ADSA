#k largets
class maxheap:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        h=[-1]
        def swap(i,j):
            temp=h[i]
            h[i]=h[j]
            h[j]=temp

        def heappush(val):
            h.append(val)
            idx=len(h)-1
            par=idx//2

            while idx>1 and h[idx]>h[par]:
                swap(idx,par)
                idx=par
                par=idx//2

        def heapify(idx):
            left=2*idx
            right=2*idx+1
            max_idx=idx
            last=len(h)
            if left<last and h[left]>h[idx]:
                max_idx=left
            
            if right<last and h[right]>h[max_idx]:
                max_idx=right

            if idx!=max_idx:
                swap(idx,max_idx)
                heapify(max_idx)

        def pop():
            last=len(h)-1
            swap(1,last)
            h.pop()
            heapify(1)

        

        for val in A:
            heappush(val)
        print(h)
        ans=[]
        for i in range(0,B):
            if len(h)>1:
                val=h[1]
                pop()
                ans.append(val)
        
        return ans
        



A=[ 943, 828, 437, 392, 605, 903, 154, 293, 383, 422, 717, 719, 896, 448, 727, 772 ]
B=3
sol=maxheap()
ans=sol.solve(A,B)
print(ans)
