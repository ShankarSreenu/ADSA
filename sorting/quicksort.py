def partition(arr,s,e):
    pivot=arr[e]
    i=s-1
    j=s
    while j<=e-1:
        if arr[j]<=pivot:
            i=i+1
            temp=arr[j]
            arr[j]=arr[i]
            arr[i]=temp
        j=j+1
    temp=arr[e]
    arr[e]=arr[i+1]
    arr[i+1]=temp
    return i+1
    

def quicksort(arr,i,j):
    if i>=j:
        return
    p=partition(arr,i,j)
    quicksort(arr,i,p-1)
    quicksort(arr,p+1,j)
