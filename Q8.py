u = [9, 2, 7, 7, 2, 2, 1, 7, 7, 9]
v = [2, 15, 19, 12, 33, 9, 17, 41, 54, 8]
aparecem = []

for i in range(len(u)):
    for j in range(len(v)):
        if u[i] == v[j] and u[i] not in aparecem:
            aparecem.append(u[i])

print(aparecem)