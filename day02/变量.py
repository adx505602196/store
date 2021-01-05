username="妙蛙种子"
age="200岁"
high="20cm"
weight="50kg"

username1="杰尼龟"
age1="188岁"
high1="38cm"
weight1="66kg"



info='''
------个人展示-----
姓名：{username},
年龄：{age},
身高：{high},
体重：{weight},
'''
print(info.format(username=username,age=age,high=high,weight=weight,))
print(info.format(username=username1,age=age1,high=high1,weight=weight1))