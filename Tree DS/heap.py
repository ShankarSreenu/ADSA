
class heap:
    def __init__(self):
        self.arr=[-1]
        self.type=True

    def swap(self,idx,par):
        temp=self.arr[idx]
        self.arr[idx]=self.arr[par]
        self.arr[par]=temp


    def insert(self,val):
        self.arr.append(val)
        idx=len(self.arr)-1
        par=idx//2
        while idx>1 and self.arr[idx]<self.arr[par]:
            self.swap(idx,par)
            idx=par
            par=idx//2
    
    def getMin(self):
        if self.arr!=[]:
            return self.arr[0]
    
    def heapify(self,idx):
        left=2*idx
        right=2*idx+1
        min_idx=idx
        last=len(self.arr)
        if left<last and self.arr[idx]>self.arr[left]:
            min_idx=left
            
        if right<last and self.arr[min_idx]>self.arr[right]:
            min_idx=right

        if min_idx!=idx:
            self.swap(idx,min_idx)
            self.heapify(min_idx)

    def pop(self):
        last=len(self.arr)-1
        self.swap(1,last)
        self.arr.pop()
        self.heapify(1)

