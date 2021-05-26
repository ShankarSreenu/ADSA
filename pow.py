#O(Log(n)) space and time

def power(x,n):
    if n==0:
       return 1
    val=power(x,n//2)
    if n%2==0:
       return val*val
    else:
       return val*val*x
