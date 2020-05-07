# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

S, k = input().split()
k = int(k)
res = sorted(list(permutations(S,k)), key= lambda x: x)
for i in res:
    print(''.join(st for st in i))

