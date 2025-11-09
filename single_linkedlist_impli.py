
# Define class node
class node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating node instance
n1 = node(10)
n2 = node(20)
n3 = node(30)
n4 = node(40)

# Connecting nodes to form a linked list
n1.next = n2
n2.next = n3
n3.next = n4

# Printing the linked list
current = n1

while(current.next != None):
    print(current.data, end = " -> ")
    current = current.next
print('None')