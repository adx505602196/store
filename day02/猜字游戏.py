import  random
num=int(random.random()*100)
i=0
while True:
    a=int(input("请输入你的数字："))
    i=i+1
    if a > num:
        print("大了")
    elif a< num:
        print("小了")
    else:
        print("恭喜猜中",num,"您本次共猜了",i,"次")
        break
