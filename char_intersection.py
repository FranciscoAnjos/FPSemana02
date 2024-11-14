w1 = input()
w2 = input()
intersect = set(w1) & set(w2)
print("".join(sorted(intersect)))