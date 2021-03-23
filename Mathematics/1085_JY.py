# BOJ 1085
# 직사각형에서 탈출
x, y, w, h = map(int, input().split())
arr = [x,y]
arr.append(h-y)
arr.append(w-x)
print(min(arr))