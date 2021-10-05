K = int(input())

b_list = list(map(int, input().split()))
# 중위순회로 적은 빌딩 번호
# b_list = 2**k - 1개

tree = [0]*(2**K)

idx = 0
while idx < K:
    temp = b_list[idx]
