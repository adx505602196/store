shop = [
    ["烤肉拌饭",200],
    ["巫山烤鱼",400],
    ["日本寿司",600],
    ["鱼香肉丝",600],
    ["糖醋里脊",300],
    ["宫保鸡丁",200],
    ["鱼头泡饼",200],
    ["泡椒凤爪",200]
]

def u ():
    for v ,i in enumerate(shop):
        print(v,i)

while True:
    salary = input("请初始化您的工资：")
    if salary.isdigit():
        salary=int(salary)
        break
    else:
        print("您的输入有误")
mycart=[]
sum=0

while True:
    print("===========欢迎来到干饭人天堂============")
    u()
    chose = input("请选择你想吃的美食的编号：")
    if chose.isdigit():
        chose=int(chose)
        if chose > len(shop):
            print("无此美食")
        else:
            if salary < shop[chose][1]:
                print("本店不支持霸王餐哦！")
            else:
                mycart.append(shop[chose])
                salary = salary-shop[chose][1]
    elif chose=='q' or chose=='Q':
        break
    else:
        print("请重新输入哦！")
    sum=0+shop[chose][1]
    j=0
    if sum<=200 and sum>0:
        j=j+200
        print('恭喜您获得积分',j,)
    elif sum>200 and sum<=400:
        j=j+400
        print("恭喜您获得积分",j,)
    elif sum>400:
        j=j+600
        print("恭喜您您获得积分",j,)
    else:
        break


print("------------欢迎下次光临！------------------")
print("购买成功以下是您的商品信息：")
for item in mycart:
    print(item)
print("您的余额为：",salary)
print("您的积分为:",j,)









