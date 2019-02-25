def TriangleArea(a,b,c):
    C = 0.5*(a+b+c)
    area = (C*(C-a)*(C-b)*(C-c))**0.5
    return area

def main():
    a = eval(input("a="))
    b = eval(input("b="))
    c = eval(input("c="))
    print(TriangleArea(a,b,c))

main()
