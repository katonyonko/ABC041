import io
import sys

_INPUT = """\
6
3 2
2 1
2 3
5 5
1 2
2 3
3 5
1 4
4 5
16 1
1 2
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  import sys
  sys.setrecursionlimit(1000000)
  N,M=map(int,input().split())
  G=[set() for _ in range(N)]
  for i in range(M):
    x,y=map(int,input().split())
    x-=1; y-=1
    G[y].add(x)
  memo=[-1]*(1<<N)
  def rec(m):
    if memo[m]>=0: return memo[m]
    res=0
    s=set([i for i in range(N) if (m>>i)&1==1])
    if len(s)==0: return 1
    for v in s:
      if len(G[v].intersection(s))==0:
        res+=rec(m-(1<<v))
    memo[m]=res
    return res
  print(rec((1<<N)-1))