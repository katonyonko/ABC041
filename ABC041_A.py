import io
import sys

_INPUT = """\
6
atcoder
3
beginner
1
contest
7
z
1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  s=input()
  i=int(input())
  print(s[i-1])