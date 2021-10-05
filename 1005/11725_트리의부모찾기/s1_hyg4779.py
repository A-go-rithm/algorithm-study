import sys
sys.stdin = open('input.txt')
N = int(input())
# 노드개수

tree = []
edge = []
for _ in range(N-1):
    a, b = map(int,input().split())
    edge = edge + [a, b]

