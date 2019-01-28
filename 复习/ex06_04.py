#ex06_04.py
s = input("输入字符串：")
s_new = ''
cnt_D = 0
cnt_6 = 0
for c in s:
    if c == 'D' or c == 'd':
        cnt_D += 1
    elif c == '6':
        cnt_6 += 1
    else:
        s_new += c
print("D的出现次数%s, 6的次数%d"%(cnt_D, cnt_6))
print("新字符串%s"%s_new)
