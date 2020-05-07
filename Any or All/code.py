# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())
lst = raw_input().split()

print(all([int(i)>0 for i in lst]) and any([j == j[::-1] for j in lst]))

