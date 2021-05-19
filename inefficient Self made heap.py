class heap_class:
    def __init__(self):
        self.node=[]
        self.top=-1
    def insert(self,val):
        if self.node==[]:
            self.node.append(val)
        else:
            self.node.append(val)
            n=len(self.node)
            child=self.top
            par=n//2
            while par>0:
                if self.node[par-1]>=val:
                    break
                else:
                    temp=self.node[par-1]
                    self.node[par-1]=self.node[child]
                    self.node[child]=temp
                    child=par-1
                    par=par//2
        return self.node

    def delete(self):
        n=len(self.node)
        if n==1:
            return []
        start=self.node.pop(0)
        val=self.node.pop(self.top)
        self.node.insert(0,val)
        n=len(self.node)
        child=0
        par=1
        if n==2:
            self.node.sort(reverse=True)
            return self.node
        while par+1<n:
            if val>= self.node[par] and  val>=self.node[par+1]:
                break

            elif self.node[par+1]>val and self.node[par+1]>=self.node[par]:
                temp=self.node[par+1]
                self.node[par+1]=self.node[child]
                self.node[child]=temp
                child=par+1
                par=child*2+1

            elif self.node[par]>val and self.node[par]>=self.node[par+1]:
                temp=self.node[par]
                self.node[par]=self.node[child]
                self.node[child]=temp
                child=par
                par=child*2+1
           
        return self.node


heap=heap_class()
heap.insert(4)
heap.insert(5)
heap.insert(8)
heap.insert(2)
heap.delete()
heap.delete()
