import sys
sys.stdin = open('input.txt')

N = int(input())
p_list = [int(input()) for _ in range(N)]

max_tip = 0

def Gangho(nums, i):
    global max_tip

    if i == len(nums)-1:
        
        cnt = tip = 0
        # 손님 순위, 팁 초기화
        while cnt < len(nums):
            tip += nums[cnt]-(cnt+1-1)
            cnt += 1
            # 손님이 오면 주려던 팁 -(등수-1+1) (처음 순위가 0으로 되어있으니까 +1 보기좋게 +1-1해놓음)

        # 현재 받은 팁이 max보다 크면 값 바꿈+
        else:
            if max_tip < tip:
                max_tip = tip
    # 손님 순서를 바꾸면서 진행
    else:
        for j in range(1, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            Gangho(nums, i+1)
            nums[i], nums[j] = nums[j], nums[i]

Gangho(p_list, 0)

print(max_tip)
