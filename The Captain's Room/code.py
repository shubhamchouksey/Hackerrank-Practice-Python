from collections import Counter
# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())
lst = map(int, input().split())
dic = Counter(lst)
# print(dic)
for key, value in dic.items():
    if value == 1:
        print(key)

