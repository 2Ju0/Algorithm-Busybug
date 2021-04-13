# BOJ 2810
# 컵홀더

n = int(input())
seat = input()

count = seat.count('LL')
if (count <= 1):
    print(len(seat))
else:
    print(len(seat) - count + 1)
