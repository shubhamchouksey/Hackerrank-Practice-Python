# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
string = input()
k = input()
index = 0

if re.search(k, string):
    while index+len(k)+1 < len(string):
        m = re.search(k, string[index:]) #begins search with new index
        
        print("({0}, {1})".format(index+m.start(), index+m.end()-1)) 
        
        index += m.start() + 1 #assign new index by +1 
else:
    print((-1, -1))


