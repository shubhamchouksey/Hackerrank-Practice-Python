# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for i in range(T):
    na = int(input())
    A = set(map(int, input().split()))
    nb = int(input())
    B = set(map(int, input().split()))
    if A.issubset(B):
        print(True)
    else:
        print(False)

