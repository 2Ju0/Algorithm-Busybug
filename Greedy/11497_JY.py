# BOJ 11497
# 통나무 건너뛰기

t = int(input())

for i in range(t):
    n = int(input())
    trees = list(map(int, input().split()))
    trees.sort()

    max_level = 0
    for i in range(2, n):
        max_level = max(max_level, abs(trees[i] - trees[i - 2]))

    print(max_level)
