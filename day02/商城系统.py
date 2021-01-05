
print("------------------------------------------海澜之家-------------------------------------------------")
print("衣服名称        尺码      颜色      数量      单价      总价")
info='''
{name},           {size},      {colour},       {number},       {unitPrice}     {otalprice}
'''

name="裤子"
size="xl"
colour="红色"
number="10"
unitPrice="100"
otalprice="1000"
print(info.format(name=name,size=size,colour=colour,number=number,unitPrice=unitPrice,otalprice=otalprice))

name1="衬衫"
size1="xl"
colour1="黑色"
number1="100"
unitPrice1="100"
otalprice1="10000"
print(info.format(name=name1,size=size1,colour=colour1,number=number1,unitPrice=unitPrice1,otalprice=otalprice1))

name2="外套"
size2="l"
colour2="黑色"
number2="100"
unitPrice2="200"
otalprice2="20000"
print(info.format(name=name2,size=size2,colour=colour2,number=number2,unitPrice=unitPrice2,otalprice=otalprice2))

