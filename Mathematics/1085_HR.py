# BOJ 1085
# 직사각형에서 탈출

x, y, w, h = map(int, input().split())
min = float('inf')
for _ in range(4):
    if w-x < min:
        min = w-x
    elif h-y < min:
        min = h-y
    elif x < min:
        min = x
    elif y < min:
        min = y
print(min)
