a=int(input("请输入A边长"))
b=int(input("请输入B边长"))
c=int(input("请输入C边长"))
if a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a:
    print("可以构成三角形")
    if a==c==b:
       print("构成等边三角形")
    elif   a==b or  a==c   or b==c:
        print("构成等腰三角形")
    else:
        print("构成普通三角形")
else:
    print("不构成三角形")
