#4,5,9 key 8
#1,1 key =2

#0,3
#5<8
#(1,3)
#9>8
#(1,2)
#5<8

#0,2 m=1
#5<8
#(2,3)
#9>8
#(2,2)
#9>8
#(3,2)

#(0,2)
#1<2:
(1,2)
#1<2:
(2,2)
#1<2
#index out of bound error
#(0,0)
#1<2
#(0,-1)

class BinarySearch:
    def __init__(self,key,arr):
        self.key=key
        self.arr=arr
        self.L=0
        self.R=len(arr)-1
        
    def search(self,L,R):
        if L<=R:
            m=(L+R)//2
            if self.arr[n]==self.key:
                return True
            elif self.arr[n]>self.key:
                return self.search(L,m-1)
            elif self.arr[n]<self.key:
                return self.search(m+1,R)
        return False
    
    def search_loop(self):
        key=self.key
        L=self.L
        R=self.R
        arr=self.arr
        while L<=R:
            m=(L+R)//2
            
            if arr[m]==key:
                return True
            
            elif arr[m]>key:
                R=m-1
            
            elif arr[m]<key:
                L=m+1
                
        return False
