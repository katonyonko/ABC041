import io
import sys

_INPUT = """\
6
2 3 4
10000 1000 100
100000 1 100000
1000000000 1000000000 1000000000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  mod=10**9+7
  A,B,C=map(int,input().split())
  print(A*B*C%mod)