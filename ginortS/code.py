# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
text = input()
lowercase = sorted(re.findall(r'[a-z]',text))
uppercase = sorted(re.findall(r'[A-Z]', text))
even_digits = sorted(re.findall(r'[0,2,4,6,8]', text))
odd_digits = sorted(re.findall(r'[1,3,5,7,9]', text))

final_res = lowercase + uppercase + odd_digits + even_digits
print(''.join(i for i in final_res))

# print(*sorted(input(), key=lambda c: (-ord(c) >> 5,c in '02468',c)),sep='')

