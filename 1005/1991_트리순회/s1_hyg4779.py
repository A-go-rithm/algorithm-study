alpha_dict = {'.': 100, 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
              'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17,
              'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}


def pre_order(n):

    if n < 100:
        print(tree[n][0], end='')
        pre_order(alpha_dict[tree[n][1]])
        pre_order(alpha_dict[tree[n][2]])


def in_order(n):

    if n < 100:
        in_order(alpha_dict[tree[n][1]])
        print(tree[n][0], end='')
        in_order(alpha_dict[tree[n][2]])


def last_order(n):

    if n:
        last_order(alpha_dict[tree[n][1]])
        last_order(alpha_dict[tree[n][2]])
        print(tree[n][0], end='')



N = int(input())
# 노드의 개수
tree = [list(input().split()) for _ in range(N)]
for i in range(N-2,-1,-1):
    for j in range(i+1, N):
        if alpha_dict[tree[i][0]] > alpha_dict[tree[j][0]]:
            tree[i], tree[j] = tree[j], tree[i]

tree = [0]+tree
pre_order(1)
print()
in_order(1)
print()
last_order(1)


