# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
N = int(input())
S = "".join(i for i in input().split())
k = int(input())

sum, count = 0,0
for j in combinations(S, k):
    if 'a' in j:
        sum +=1
    count += 1

    
print(sum/count)

