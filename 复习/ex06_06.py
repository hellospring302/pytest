##ex06_06.py
import random
random.seed()
passwd = ''
alpha = 0
digital = 0
other = 0
while alpha < 2 or digital < 3 or other < 2:
    passwd = ''
    alpha = 0
    digital = 0
    other = 0
    for n in range(16):
        c = random.randint(32,126)
        passwd += chr(c)
    for i in passwd:
        if 65 <= ord(i) <= 90:
            alpha += 1
        elif 48 <= ord(i) <= 57:
            digital += 1
        else:
            other += 1
print(passwd)
    
    
    
