class heap:
    def __init__(self):
        self.arr=['$']


    def insert(self,val):
        self.arr.append(val)
        n=len(self.arr)
        child=n-1
        while self.arr[child]!='$':
            par=child//2
            if self.arr[par]!='$' and self.arr[child]>self.arr[par]:
                temp=self.arr[child]
                self.arr[child]=self.arr[par]
                self.arr[par]=temp
            child = par


    def heappop(self):
        if self.arr!=['$']:
            last=self.arr[-1]
            self.arr[1]=last
            self.arr.pop()


    def heapdown(self):
        if len(self.arr)==1:
            return
        n=len(self.arr)
        par=1
        while par*2<n or par*2+1<n:
            if par*2<n and par*2+1>=n:
                if self.arr[par]>=self.arr[par*2]:
                    return

                else:
                    temp=self.arr[par*2]
                    self.arr[par*2]=self.arr[par]
                    self.arr[par]=temp
                    par=par*2

            elif par*2<n and par*2+1<n:
                if self.arr[par]<self.arr[par*2] and self.arr[par*2]>=self.arr[par*2+1]:
                    temp=self.arr[par*2]
                    self.arr[par*2]=self.arr[par]
                    self.arr[par]=temp
                    par=par*2
                elif  self.arr[par]<=self.arr[par*2+1]:
                    temp=self.arr[par*2+1]
                    self.arr[par*2+1]=self.arr[par]
                    self.arr[par]=temp
                    par=par*2+1
                elif self.arr[par]>=self.arr[par*2] and self.arr[par]>=self.arr[par*2+1]:
                    return
arr=[5,2,4,1,3,6,0]

h=heap()
for val in arr:
    h.insert(val)

h.heappop()
h.heapdown()
h.heappop()
h.heapdown()
h.heappop()
h.heapdown()
# ['$', 6, 3, 5, 1, 2, 4, 0]
# ['$', 0, 3, 5, 1, 2, 4] 
# ['$',5,3,0,1,2,4]
