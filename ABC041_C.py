import io
import sys

_INPUT = """\
6
3
140 180 160
2
1000000000 1
8
3 1 4 15 9 2 6 5
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  A=list(map(int,input().split()))
  d={a:i for i,a in enumerate(A)}
  A.sort(reverse=True)
  for i in range(N):
    print(d[A[i]]+1)