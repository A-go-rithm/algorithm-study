def slicing(n):
    if n:
        slicing(tree[n][0])
        slicing(tree[n][1])
        tree[n] = False
    else:
        return 0


N = int(input())
# 노드개수
info = list(map(int, input().split()))
info = [[i, info[i]] for i in range(N)]

# 0 to N-1번 노드의 부모번호
tree = [[0,0] for _ in range(N)]
target = int(input())


for i in range(N):
    c = info[i][0] # 주어진 노드번호
    p = info[i][1] # 주어진 노드의 부모정보

    if p not in [0, -1]:

        if tree[p][0]:
            tree[p][1] = c
        else:
            tree[p][0] = c

slicing(target)

if target == 0:
    print(0)
else:
    print(tree.count([0, 0])-1)