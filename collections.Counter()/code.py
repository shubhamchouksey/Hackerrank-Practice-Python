# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
X = int(input())
myList = list(map(int,input().strip().split()))[:X]

dict = Counter(myList)
N = int(input())

sum = 0
for i in range(N):
    shoe_size, price = input().split()
    shoe_size = int(shoe_size)
    price = int(price)
    
    if shoe_size in dict.keys() and dict[shoe_size]>0:
        sum += price
        dict[shoe_size] -= 1
    
print(sum)




