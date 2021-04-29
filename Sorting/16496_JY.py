# BOJ 16496
# 큰 수 만들기

import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    lst = sys.stdin.readline().rstrip().split(" ")
    m_length = max([len(n) for n in lst])
    lst.sort(key=lambda x: x * (m_length // len(x) + 1), reverse=True)
    print(int(''.join(lst)))
