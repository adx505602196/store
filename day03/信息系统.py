# 姓名  年龄  性别  编号   任职公司   薪资   部门编号
names = [
    ["何登勇","56","男","106","IBM", 500 ,"50"],
    ["曹东雪","19","女","230","微软", 501 ,"60"],
    ["刘营营", "19", "女", "210", "Oracle", 600, "60"],
    ["李汉聪", "45", "男", "230", "Tencent", 700 , "10"],
    ["张家玮","45","男","220","阿里巴巴",500,"30"],
]
#1统计每个人的平均工资
sum=0
for i in range(0,len(names)):
    sum=sum+names[i][5]
print("平均新增为：",sum/len(names))

#2平均年龄为
sum1=0
for j in range(0,len(names)):
    sum1=sum1+int(names[j][1])
print("平均年龄为：",sum1//len(names))

#3添加数据


#统计公司男女人数

man=0
woman=0
for k in range (0,len(names)):
    if names[k][2]=="男":
        man+=1
    else:
        woman+=1
print("男生的人数为",man,"女生的人数为",woman,)

#统计每个部门人数
m50=0
m60=0
m10=0
m30=0
for q in range(0,len(names)):
    if names[q][6]=="50":
        m50=m50+1
    if names[q][6]=="60":
        m60=m60+1
    if names[q][6]=="10":
        m10=m10+1
else:
        m30=m30+1
print("部门编号为50的有",m50,"人","部门编号为60的有",m60,"人""部门编号为10的有",m10,"人""部门编号为30的有",m30,"人",)





