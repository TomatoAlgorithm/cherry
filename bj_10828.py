import sys
N = int(sys.stdin.readline())
stack = []
 
for n in range(N):
    str = sys.stdin.readline().split()
    command = str[0]
    
    if command == "push":
        stack.append(str[1])
    
    elif command == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
 
    elif command == "size":
        print(len(stack))
    
    elif command == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
     
    elif command == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])