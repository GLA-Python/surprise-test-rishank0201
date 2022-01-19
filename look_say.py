lines=int(input())
num=1
print(num)
for i in range(1,lines):
    out=""
    while num>0:
        digit=num%10
        c=1
        num//=10
        while num>0 and num%10==digit:
            c+=1
            num//=10
        out=str(c)+str(digit)+out
    print(out)
    num=int(out)