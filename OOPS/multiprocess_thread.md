### Quick overview
<img src="https://user-images.githubusercontent.com/65806647/196727177-ee7b28fc-789f-4111-b10c-0199c6886379.png" width="600" height="350" />

- CPU (central processing unit) is a piece of hardware in a computer that executes binary code.
- OS (operating system) is software that schedules when programs can use the CPU.
- Process is a program that is being executed.
- Thread is part of a process.
- Blocking happens when a thread is stuck, waiting for a something to finish so it can complete its function.
When single-threaded apps get blocked, this causes a poor user experience and slower overall execution time.
- Multi-threaded apps can execute more than one function at what appears to be the same time.
While one thread is blocked, other threads can continue their execution.


<img src='https://user-images.githubusercontent.com/65806647/196622566-70e1d5d1-feb8-4041-9559-ba830c7d258c.png' width="250" height="250"/>

#### Difference between threads and process:
- The major difference between the two is that in multithreading threads are being executed in one process sharing common address.
space whereas in multi processing different processes have different address space.
- Each Threads have thier own tasks and instruction sets.
- Processes:Are differrent programms running on computer.
- Threads are light weight processes.
- In a process address are stored within a process.
- Every process has its own address space,thus program variable are not shared between two process.
- Address space is where a space stores variables etc.
- threads share common memory using process memory
- process share common memory with shared memory
```python
  import time
  import threading
  def square(arr):
      for i in range(0,len(arr)):
          print("sq",arr[i]**2)
  def cube(arr):
      for i in range(0,len(arr)):
          print("cub",arr[i]**3)
          
  arr=[11,12,9]
  t=time.time()
  t1=threading.Thread(target=square,args=(arr,))
  t2=threading.Thread(target=cube,args=(arr,))
  t1.start()
  t2.start()
  t1.join()#done with individual thread
  t2.join()
  print(time.time()-t)
```

### Sharing Data between two process in Python.
```python
  import multiprocessing
  def fun(arr,res,var):
      var.value=3.14
      i=0
      for val in arr:
          res[i]=(val**3)
          i+=1

  arr=[4,5,6]
  res=multiprocessing.Array('i',3)
  var=multiprocessing.Value('d',0.0)
  p1 = multiprocessing.Process(target=fun,args=(arr,res,var))
  p1.start()
  p1.join()
  print(res[:],var.value)
```

### Multiprocessing Locking

why is locking needed?
- when two or more process work on same shared memory there can be chance of conflicts.
- Locking blocks other process untill one process is completed.
```python
  import multiprocessing
  import time
  def deposit(money,lock):
      for i in range(0,100):
          time.sleep(0.0010)
          lock.acquire()
          money.value=money.value+1
          lock.release()

  def withdraw(money,lock):
      for i in range(0,100):
          time.sleep(0.0010)
          lock.acquire()
          money.value=money.value-1
          lock.release()

  money=multiprocessing.Value('i',200)
  lock = multiprocessing.Lock()
  p1=multiprocessing.Process(target=deposit,args=(money,lock))
  p2=multiprocessing.Process(target=withdraw,args=(money,lock))
  p1.start()
  p2.start()
  p1.join()
  p2.join()
  print(money.value)
```
### Multiprocess pooling
```python
  from multiprocessing import Pool
  def fun(arr):
      print(arr)
      return arr*arr

  arr=[4,5,6]
  p=Pool()
  res=p.map(fun,arr)
  print(res)
```
![image](https://user-images.githubusercontent.com/65806647/196676867-b4d2f313-cc30-48ba-9322-6b0d45853901.png)
- Dividing the work between the cores and reducing them back into single out put.


