'''for  i   in   range (0,5):
    for j in  range(0,i+1):
        print("*",end="")     #end=""不换行
    print()

for i  in  range (1,12):
    for j  in  range (1,i+1):
        print( j,"x",i,"=",(j*i),"\t",end="")
    print()
'''
a=[1,2,4,5,66,77]
#1、求所有数的和
sum=0
for i in  range (0,len(a)):
    sum=sum+a[i]
print("总和为",sum)

#求偶数的和

sum1=0
for i in range (0,len(a)):
    if a[i]%2==0:
        sum1=sum1+a[i]
print("偶数和为",sum1)

#最大数

i=0
for k in range (0,len(a)):
    if a[k] > i:
        i=a[k]
print("最大值为",i)

#选择排序
for i  in range (0,len(a)):
    for j in range (i+1,len(a)):
        if a[j]<a[i]:
            c=a[j]
            a[j]=a[i]
            a[i]=c
print(a)

