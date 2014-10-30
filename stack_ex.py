
# A stack (in the context of algorithms and computer science) 

n = 10

stack = []  # last-in, first-out 

for i in list(range(n)):
    stack.append(i)
print(stack)

stack.extend(("break", "break"))

for i in list(range(n+1,2*n+1)):
    stack.append(i)
print(stack)

for i in list(range(int(n/2))):
    stack.pop()                         #last-in, first-out 
    print(stack)
 
 
 
 
