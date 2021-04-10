# BOJ 2810
# 컵홀더

n = int(input())
movie = input()
cup = movie.count('S')+(movie.count('L') // 2)
print(min(cup + 1, n))
