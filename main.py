with open('file.txt', 'r') as file:
    lines = file.readlines()
    n = int(lines[0])
    m = list(map(int, lines[1].split(' ')))
    a = list(map(lambda x: int(x) - 1, lines[2].split(' ')))
    b = list(map(lambda x: int(x) - 1, lines[3].split(' ')))
    p = [0 for _ in range(n)]
    for i in range(n):
        p[b[i]] = a[i]
    C = []
    vis = [False for _ in range(n)]
    for i in range(n):
        if not vis[i]:
            c = [i]
            vis[i] = True
            x = p[i]
            while vis[x] is not True:
                vis[x] = True
                c.append(x)
                x = p[x]
            C.append(c)
    mass_sum = [sum([m[s] for s in c]) for c in C]
    min_c = [min([m[s] for s in c]) for c in C]
    min_all = min(m)
    res = 0
    for ci, c in enumerate(C):
        met1 = mass_sum[ci] + (len(c) - 2) * min_c[ci]
        met2 = mass_sum[ci] + min_c[ci] + (len(c) + 1) * min_all
        res += min(met1, met2)
    print(res)



