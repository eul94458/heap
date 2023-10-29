# heap

Usage:
```
A = MaxHeap()
N = 15

for n in range(N):
    A.append(n)
    print(A.data)
    print(A)

B = A.copy()
for n in range(N):
    temp = B.popleft()
    print(f"popleft({temp})")
    print(B)
```
Output:
```
deque([0])
MaxHeap vvvvvvvvvvvv
0
^^^^^^^^^^^^^^^^^^^^
deque([1, 0])
MaxHeap vvvvvvvvvvvv
 1  
0   
^^^^^^^^^^^^^^^^^^^^
deque([2, 0, 1])
MaxHeap vvvvvvvvvvvv
 2  
0 1 
^^^^^^^^^^^^^^^^^^^^
deque([3, 2, 1, 0])
MaxHeap vvvvvvvvvvvv
   3    
 2   1  
0       
^^^^^^^^^^^^^^^^^^^^
deque([4, 3, 1, 0, 2])
MaxHeap vvvvvvvvvvvv
   4    
 3   1  
0 2     
^^^^^^^^^^^^^^^^^^^^
deque([5, 3, 4, 0, 2, 1])
MaxHeap vvvvvvvvvvvv
   5    
 3   4  
0 2 1   
^^^^^^^^^^^^^^^^^^^^
deque([6, 3, 5, 0, 2, 1, 4])
MaxHeap vvvvvvvvvvvv
   6    
 3   5  
0 2 1 4 
^^^^^^^^^^^^^^^^^^^^
deque([7, 6, 5, 3, 2, 1, 4, 0])
MaxHeap vvvvvvvvvvvv
       7        
   6       5    
 3   2   1   4  
0               
^^^^^^^^^^^^^^^^^^^^
deque([8, 7, 5, 6, 2, 1, 4, 0, 3])
MaxHeap vvvvvvvvvvvv
       8        
   7       5    
 6   2   1   4  
0 3             
^^^^^^^^^^^^^^^^^^^^
deque([9, 8, 5, 6, 7, 1, 4, 0, 3, 2])
MaxHeap vvvvvvvvvvvv
       9        
   8       5    
 6   7   1   4  
0 3 2           
^^^^^^^^^^^^^^^^^^^^
deque([10, 9, 5, 6, 8, 1, 4, 0, 3, 2, 7])
MaxHeap vvvvvvvvvvvv    
           10           
     9           5      
  6     8     1     4   
 0  3  2  7             
^^^^^^^^^^^^^^^^^^^^    
deque([11, 9, 10, 6, 8, 5, 4, 0, 3, 2, 7, 1])
MaxHeap vvvvvvvvvvvv    
           11           
     9           10     
  6     8     5     4   
 0  3  2  7  1          
^^^^^^^^^^^^^^^^^^^^    
deque([12, 9, 11, 6, 8, 10, 4, 0, 3, 2, 7, 1, 5])
MaxHeap vvvvvvvvvvvv    
           12           
     9           11     
  6     8     10    4   
 0  3  2  7  1  5       
^^^^^^^^^^^^^^^^^^^^    
deque([13, 9, 12, 6, 8, 10, 11, 0, 3, 2, 7, 1, 5, 4])
MaxHeap vvvvvvvvvvvv    
           13           
     9           12     
  6     8     10    11  
 0  3  2  7  1  5  4    
^^^^^^^^^^^^^^^^^^^^    
deque([14, 9, 13, 6, 8, 10, 12, 0, 3, 2, 7, 1, 5, 4, 11])
MaxHeap vvvvvvvvvvvv    
           14           
     9           13     
  6     8     10    12  
 0  3  2  7  1  5  4 11 
^^^^^^^^^^^^^^^^^^^^    
popleft(14)
MaxHeap vvvvvvvvvvvv    
           13           
     9           12     
  6     8     10    11  
 0  3  2  7  1  5  4    
^^^^^^^^^^^^^^^^^^^^    
popleft(13)
MaxHeap vvvvvvvvvvvv    
           12           
     9           11     
  6     8     10    4   
 0  3  2  7  1  5       
^^^^^^^^^^^^^^^^^^^^    
popleft(12)
MaxHeap vvvvvvvvvvvv    
           11           
     9           10     
  6     8     5     4   
 0  3  2  7  1          
^^^^^^^^^^^^^^^^^^^^    
popleft(11)
MaxHeap vvvvvvvvvvvv    
           10           
     9           5      
  6     8     1     4   
 0  3  2  7             
^^^^^^^^^^^^^^^^^^^^    
popleft(10)
MaxHeap vvvvvvvvvvvv
       9        
   8       5    
 6   7   1   4  
0 3 2           
^^^^^^^^^^^^^^^^^^^^
popleft(9)
MaxHeap vvvvvvvvvvvv
       8        
   7       5    
 6   2   1   4  
0 3             
^^^^^^^^^^^^^^^^^^^^
popleft(8)
MaxHeap vvvvvvvvvvvv
       7        
   6       5    
 3   2   1   4  
0               
^^^^^^^^^^^^^^^^^^^^
popleft(7)
MaxHeap vvvvvvvvvvvv
   6    
 3   5  
0 2 1 4 
^^^^^^^^^^^^^^^^^^^^
popleft(6)
MaxHeap vvvvvvvvvvvv
   5    
 3   4  
0 2 1   
^^^^^^^^^^^^^^^^^^^^
popleft(5)
MaxHeap vvvvvvvvvvvv
   4    
 3   1  
0 2     
^^^^^^^^^^^^^^^^^^^^
popleft(4)
MaxHeap vvvvvvvvvvvv
   3    
 2   1  
0       
^^^^^^^^^^^^^^^^^^^^
popleft(3)
MaxHeap vvvvvvvvvvvv
 2  
0 1 
^^^^^^^^^^^^^^^^^^^^
popleft(2)
MaxHeap vvvvvvvvvvvv
 1  
0   
^^^^^^^^^^^^^^^^^^^^
popleft(1)
MaxHeap vvvvvvvvvvvv
0
^^^^^^^^^^^^^^^^^^^^
popleft(0)
MaxHeap vvvvvvvvvvvv
^^^^^^^^^^^^^^^^^^^^
^^^^^^^^^^^^^^^^^^^^
```
