print("-----------------个人信息---------------")
info='''
姓名：{name}
身份证号：{id}
年龄：{age}
性别：{gender}
身高：{height}
体重：{weight}
'''
name="张三"
id="130824199901110506"
age="21"
gender="男"
height="1.8m"
weight="70kg"

print(info.format(name=name,id=id,age=age,gender=gender,height=height,weight=weight))