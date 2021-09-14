import sys
sys.stdin = open('input.txt')

'''
1) 양 끝 공유기
2) 중간값 to + - 1 값 탐색하며 공유기가없는 집 찾으면 공유기 설치
  (+-1 탐색중 두군데 모두 있으면 이전 공유기와 더 먼 쪽에 설치)
3) 두개의 구간이 생김 -> 2번 반복
3) 공유기 다 설치하면 for문 돌리면서 최대거리 찾기
'''

# 집의 개수, 공유기 수
N, wifi = map(int, input().split())

# 집의 위치
home = [int(input()) for _ in range(N)]

# 집 오름차순으로 정렬
for i in range(N-1, -1, -1):
    for j in range(1,i):
        if home[j] > home[j+1]:
            home[j], home[j+1] = home[j+1], home[j]

# 공유기 설치된 집 인덱스 리스트
arr = [False for _ in range(home[-1])]

start = home[0]
end = home[-1]

if (start+end)%2: # 처음 + 끝홀수의 경우
    mid = (start+end-1)//2
    # mid1 = mid mid2 = mid+1



else: # 처음 + 끝 짝수의 경우
    mid = (start+end)//2

    for i in range(len(home[:mid])):
        if arr[mid+i] == False and (mid+i) in home:
            arr[mid+i] == True
            break
        elif arr[mid-i] == False and (mid+i) in home:
            arr[mid-i] == True
            break


