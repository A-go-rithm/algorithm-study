import sys
sys.stdin = open('input.txt')

T = int(input())

while T>0:

    N = int(input()) # 유제품 갯수
    yogurt_list = [int(input()) for _ in range(N)]

    # idx 0부터 오름차순으로 정렬
    for i in range(N):
        for j in range(i-1,-1,-1):
            if yogurt_list[j] < yogurt_list[j+1]:
                yogurt_list[j], yogurt_list[j+1] = yogurt_list[j+1], yogurt_list[j]

    result = 0
    
    # 3으로 나눠서 두번째 값은 포함시키지 않고 다 더함
    for i in range(N):
        if i%3 != 2:
            result += yogurt_list[i]
    print(result)
    T -= 1