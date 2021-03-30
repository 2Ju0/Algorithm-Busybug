# △BOJ 13164
# 행복 유치원

n, k = map(int, input().split())
arr = list(map(int, input().split()))
diff = [0]*n
for i in range(len(arr) - 1):
    diff.append(arr[i + 1] - arr[i])  # 키 차이
diff.sort(reverse=True)  # 내림차순
print(sum(diff[k - 1:]))  # [k-1]부터 끝까지 sum
