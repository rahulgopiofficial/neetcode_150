import random

# Create random value
s = [random.randint(1,20) for _ in range(20)]
t = 15
ans = []

# Sort the array
ss = sorted(s)

# Main logic
for i in range(len(ss)):

    # Created new list and removed the 1st index value
    nl = ss[:]
    nl.pop(i)

    # Two poi
    l = 0
    r = len(nl) - 1
    while(l<r):
        w = nl[l] + nl[r] + ss[i]

        if w == t:
            ans.append([nl[l], nl[r], ss[i]])
            l+=1
            r-=1
        elif w < t:
            l+=1
        elif w > t:
            r-=1

unique_list = set(tuple(sorted(sublist)) for sublist in ans)

print(unique_list)