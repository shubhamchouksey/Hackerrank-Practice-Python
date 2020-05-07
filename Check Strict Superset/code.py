# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int,input().split()))
N = int(input())
res = True
for _ in range(N):
    if not A.issuperset(set(map(int,input().split()))):
        res = False
        break
    
print(res)

