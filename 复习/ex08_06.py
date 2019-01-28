##ex08_06.py
import random
def pp(n):
    while True:
        num = eval(input("取出几个豆子，只能1,2或3:"))
        if num < 1 or num > 3:
            print("错误，重来")
            continue
        return n - num
def cp(n):
    if n == 4:
        return 3
    if n == 3:
        return 2
    if n == 2:
        return 1
    else:
        i = random.randint(1,3)
        return i
def main():
    total=16
    while True:
        ppickrest=pp(total)
        cpick=cp(ppickrest)
        total=ppickrest-cpick
        if ppickrest==1:
            print("你赢了")
            break
        print("comp=%d,rest=%d"%(cpick,total))
        if total==1:
            print("你输了")
            break
main()
    
