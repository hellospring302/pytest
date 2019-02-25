def getdict(phone):
    A=[i for i in range(0,10)]
    B=['zero','one','two','three','four','five','six','seven','eight','nine']
    mydict=dict(zip(A,B))
    for i in phone:
        print(mydict[int(i)],end=" ")
def main():
    phone=input("Please enter a series phone number:")
    getdict(phone)
main()
