import sys
input = sys.stdin.readline

n, m = map(int,input().split())

n_list = set(map(int,input().split()))
m_list = set(map(int,input().split()))
print(len(n_list ^ m_list))