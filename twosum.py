s = list(range(1,20))
t = 10
ans = []

# Brut force approach
'''
for i in range(1,len(s)):
    for j in range(i+1,len(s)):
        if s[i] + s[j] == t:
            ans.append([s[i], s[j]])

print(ans)
'''

# Two pointer method
ss = sorted(s)
l = 0
r = len(ss) - 1

while(l < r):
    w = ss[l] + ss[r]
    print(w)
    if w == t:
        ans.append([ss[l], ss[r]])
        l+=1
        r-=1
    elif w > t:
        r-=1
    elif w < t:
        l+=1

print(ans)