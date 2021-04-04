# BOJ 2456
# 나는 학급회장이다

n = int(input())
arrFirst = [0]*n
arrTwo = [0]*n
arrThird = [0]*n
for i in range(n):
    arrFirst[i], arrTwo[i], arrThird[i] = map(int, input().split())
m = max(sum(arrFirst), sum(arrTwo), sum(arrThird))
count = 0
if sum(arrFirst) == m:
    count += 1
if sum(arrTwo) == m:
    count += 1
if sum(arrThird) == m:
    count += 1
if count == 1:
    if sum(arrFirst) == m:
        print(1, m)
    elif sum(arrTwo) == m:
        print(2, m)
    else:
        print(3, m)
elif count != 1:
    res = 0
    countThree = max(arrFirst.count(3), arrTwo.count(3), arrThird.count(3))
    countTwo = max(arrFirst.count(2), arrTwo.count(2), arrThird.count(2))
    if arrFirst.count(3) == countThree:
        res += 1
    if arrTwo.count(3) == countThree:
        res += 1
    if arrThird.count(3) == countThree:
        res += 1
    if res == 1:
        if arrFirst.count(3) == countThree:
            print(1, m)
        elif arrTwo.count(3) == countThree:
            print(2, m)
        else:
            print(3, m)
    elif res != 1:
        temp = 0
        if arrFirst.count(3) == countThree and arrFirst.count(2) == countTwo:
            temp += 1
        if arrTwo.count(3) == countThree and arrTwo.count(2) == countTwo:
            temp += 1
        if arrThird.count(3) == countThree and arrThird.count(2) == countTwo:
            temp += 1
        if temp == 1:
            if arrFirst.count(2) == countTwo:
                print(1, m)
            elif arrTwo.count(2) == countTwo:
                print(2, m)
            else:
                print(3, m)
        elif temp != 1:
            print(0, m)
# ============================================
# 🎇다른 풀이법
point = [[0]*4 for _ in range(4)]

count = int(input())

for i in range(count):
    temp = list(map(int,input().split()))
    point[1][temp[0]] +=1
    point[2][temp[1]] +=1
    point[3][temp[2]] +=1

#print(point)

tempMax = -1
maxCount =0 # 최댓값인 것 갯수
check = 0 # 동점자 체크
numb = -1 # 최댓값가진 후보 번호

for i in range(1,4):
    sumTemp = point[i][1] + point[i][2]*2 + point[i][3]*3

    if sumTemp > tempMax:
        tempMax = sumTemp
        maxCount += 1
        numb = i
    elif sumTemp == tempMax:
        if point[numb][3] < point[i][3]:
            numb = i
            check =0
        elif point[numb][3] == point[i][3] and point[numb][2] < point[i][2]:
            numb=i
            check=0
        elif point[numb][3] == point[i][3] and point[numb][2] == point[i][2]:
            check = 1

if check==1:
    numb=0

print(numb,tempMax)