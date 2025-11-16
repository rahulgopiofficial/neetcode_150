# Define a dynamic array/list for stack
stk = []

# Add in stack
stk.append(5)
stk.append(6)
stk.append(7)
stk.append(8)
stk.append(9)
print(stk)

# Remove from stack
if stk:
    stk.pop()
else:
    print('Stack is empty')

# Peek
print(stk[-1])

# Check if stack is empty
if stk:
    print(True)
else:
    print(False)