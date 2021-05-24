#segment tree: Used Hackearth as referance.
#bottom up approach recursion
#https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/tutorial/
#Time Complexity:O(log(n))
#space complexity:O(n)
#Update:O(log(n))
#update time is O(1) brute works fine using suffix tree
#O(l-R) in worst case O(n)
#for n updates complexity is O(n^2)


#give array input
arr=[1,2,2,4]
n=len(arr)
val= (n+1)//2 if n%2==0 else (n)//2+1

#initialising tree
tree=[0 for i in range(0,pow(2,val+1))]

#O(N)
#root sum of array
# leaf nodes are array elements
#  children of node i is 2*i and 2*i+1
def build(arr,i,start,end):
  
    #implies if you tough leaf nodes populate tree with the value
    if start==end:
        tree[i]=arr[start]
        
    else:
         #caluculate the middle index of array
         mid=(start+end)//2
         #divide and call left sub tree
         build(arr,2*i,start,mid)
         #divide and call left sub tree
         build(arr,2*i+1,mid+1,end)
         #back track and assign sum to parent node from child node
         tree[i]=tree[2*i]+tree[2*i+1]

#O(log(n))
#Range represented by a node is completely inside the given range
#Range represented by a node is completely outside the given range
#Range represented by a node is partially inside and partially outside the given range
def query(i,start,end,l,r):
    #if no overlap
    if r<start or l>end:
        return 0
    #if complete overlap
    if l<=start and end<=r:
        return tree[i]
    #if partial overlap
    mid=(start+end)//2
    left_subtree=query(2*i,start,mid,l,r)
    right_subtree=query(2*i+1,mid+1,end,l,r)

    return left_subtree + right_subtree

#idx index
#val value to update
#how to know index as its changed
#how to backtrack after changing
#To update an element, look at the interval in which the element is present and recurse accordingly on the left or the right child.
#O(log(n))
def update(i,start,end,idx,val):
    if start==end:
        arr[idx]= arr[idx]+val
        tree[i] = tree[i]+val
    else:
        mid=(start+end)//2
        if start<=idx and idx<=mid:
            update(2*i,start,mid,idx,val)
        else:
            update(2*i+1,mid+1,end,idx,val)
        
        tree[i]=tree[2*i]+tree[2*i+1]



#build ,update ,query
build(arr,1,0,len(arr)-1)
update(0,0,len(arr)-1,2,1)
query(arr,1,0,len(arr)-1,0,5)


        

 
