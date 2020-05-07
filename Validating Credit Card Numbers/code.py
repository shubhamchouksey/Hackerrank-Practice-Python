# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
card_no_range = int(input())
for i in range(card_no_range):
    card_no = input()
    toggle1 = re.match(r'(^[4,5,6](\d){3}[-]?\d{4}[-]?\d{4}[-]?\d{4})',  card_no)
    # print(toggle)
    if toggle1:
        s = re.sub(r'\D', r'', card_no)
        toggle3 = len(s) == 16
        toggle2 = re.search(r'((\d)\2{3,})', s)
        if toggle1 and (not toggle2) and toggle3:  
            print('Valid')
        else:
            print('Invalid')
    else:
        print('Invalid')
    
    # print(s)
    # s = re.sub(r'\D', r'', card_no)
    # print(len(s))
    # toggle2 = re.search(r'((\d)\2{3,})', s)
    # print(toggle2)
# (^[4,5,6](\d){3}[-]?\d{4}[-]?\d{4}[-]?\d{4})


# 

