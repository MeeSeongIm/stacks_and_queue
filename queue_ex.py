
# Deque: a doubly linked list. List: an array. 
# The main advantage of a deque: insertions and deletions at the beginning. 
# The main advantage of a list: fast random reads.  

from collections import deque  
n = 10

queue = deque([])
 
for i in list(range(n)):
    queue.append(i)    
print(queue)

queue.extend(("break", "break"))

for i in list(range(n+1,2*n+1)):
    queue.append(i)
print(queue)

for i in list(range(int(n/2))):
    queue.popleft()                      #first-in, first-out 
    print(queue)





