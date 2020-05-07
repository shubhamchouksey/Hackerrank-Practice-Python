# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
S = input()
print(*[(len(list(g)), int(k)) for k, g in groupby(S)], sep = ' ')

