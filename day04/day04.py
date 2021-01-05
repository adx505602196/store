shop=[
    ["iphone",10000],
    ["mac loptop",12000],
    ["辣条",12],
    ["娃哈哈",10],
    ["洗衣液",30],
    ["少女的唾液",58],

]
#展示商品
for item,v in enumerate(shop):
    print(item,v)

#校验工资
    while True:
        salary = input("请初始化您的工资：")
        if salary.isdigit():  # isdigit（） 来判断字符串是不是由数字组成
            salary = int(salary)
            break
        else:
            print("请输入合适的工资。")
    print("您的工资为", salary)

mycart=[]
while True:
    print("============欢迎来到购物商场============")
    for item, v in enumerate(shop):
        print(item, v)

    chose=input("请输入您的商品号：")
    if chose.isdigit():
        chose=int (chose)
        if chose>len(shop):
            print("\033[41;20;1m输入商品不存在\033[0m")
        else:
            if salary < shop[chose][1]:
                print("\033[41;20;1m工资余额不足\033[0m")
            else:
                mycart.append(shop[chose])
                salary=salary-shop[chose][1]
    elif chose=="q" or chose=="Q":
        break
    else:
        print("\033[41;20;1m您的输入不合法，请重新输入\033[0m")
print("=======欢迎下次光临==========")
print("您购买的商品为",mycart,"您的工资余额为",salary,"￥")