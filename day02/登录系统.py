print("================登录系统============")

count=0
while True:
    count = count + 1
    name1=input("请输入用户名")
    id1=input("请输入密码")
    name="jason"
    id="admin"
    if name1==name and id1==id:
        print("登录成功")
        break
    elif name1!=name or id1!=id:
        print("登录失败")
    if count >= 3:
            print("超过三次"
                  "锁定系统")
            break










