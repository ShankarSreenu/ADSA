
#iam getting problem of how to create an array while back tracking
def merge(arr,s,e):
    mid=(s+e)//2
    i,j=s,mid+1
    temp=[]
    while i<=mid and j<=e:
        if arr[i]<arr[j]:
            temp.append(arr[i])
            i=i+1
        else:
            temp.append(arr[j])
            j=j+1
    while j<=e:
        temp.append(arr[j])
        j=j+1
    while i<=mid:
        temp.append(arr[i])
        i=i+1
    k=0
    for i in range(s,e+1):
        arr[i]=temp[k]
        k=k+1

def mergesort(arr,i,j):
    if i>=j:
        return
    mid=(i+j)//2
    mergesort(arr,i,mid)
    mergesort(arr,mid+1,j)
    merge(arr,i,j)

arr=list(map(int,input().split()))
mergesort(arr,0,len(arr)-1)
print(arr)

