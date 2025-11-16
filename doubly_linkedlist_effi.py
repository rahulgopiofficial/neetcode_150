class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# n1 = node(10)
# n2 = node(20)
# n3 = node(30)
# n4 = node(40)
# n5 = node(50)
# n6 = node(60)

# Or you can write in this way also

# n1, n2, n3, n4 = node(10), node(20), node(30), node(40)

# This is more efficient way
list = [10, 20, 30, 40, 50, 60]
nodes = [node(i) for i in list]

# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
# n5.next = n6

# n6.prev = n5
# n5.prev = n4
# n4.prev = n3
# n3.prev = n2
# n2.prev = n1

# Simple way to loop the values
for i in range(len(nodes) - 1):
    nodes[i].next, nodes[i+1].prev = nodes[i+1], nodes[i]

# head = n1
# tail = n6

head = nodes[0]
tail = nodes[-1]

while head:
    print(head.data, end = " -> ")
    head = head.next
print("None")

while tail:
    print(tail.data, end = " -> ")
    tail = tail.prev
print("None")