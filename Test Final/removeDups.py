def removeDups (i):
    i = set(i)
    u = i & i
    u = list(u)
    return sorted(u)

print(removeDups([1, 0, 1, 0]))
print(removeDups(["The","Big","Cat"]))
print(removeDups(["John","Taylor","John"]))