# Library to define
from collections import deque

# Initialise the queue
q = deque()

# Add element in queue
q.append(10)
q.append(20)
q.append(30)

print(q)

# Remove element from queue pop can also be use but then it will act like stack
q.popleft()

print(q)

# Peek 1st element
print(q[0])

# Peek last element
print(q[-1])