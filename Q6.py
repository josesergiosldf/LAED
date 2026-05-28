u = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
v = [7, 2, 3, 1, 6, 5, 9, 10, 4, 8]

perm = True

for x in u:
    if u.count(x) != v.count(x):
        perm = False
        break

if perm:
    print("u e v são permutações um do outro.")
else:
    print("u e v não são permutações um do outro.")

# O(n^2)