#!/usr/bin/env python3
import sys
if len(sys.argv) <= 1:
    print("Parameter Error")

try:
    for arg in sys.argv[1:]:   #循环获取参数列
        a = arg.split(':')     #参数去掉：赋给a
        b = int(a[0])          #数值化列表第一个值为ID
        c = int(a[1])          #数值化列表第二个值为薪金
#        print(b,c)
        y = 0.08+0.02+0.005+0.06              #各险金比例
        x = c - 3500 - c * y      #判断税金的等级
        if x < 1:
            d = 0                     #d为税金
            e = c - c*y - d
        elif x <= 1500:
            d = x * 0.03
            e = c - c*y - d
        elif x >1500 and x <= 4500:
            d = x * 0.1 - 105
            e = c - c*y - d
        elif x > 4500 and x <= 9000:
            d = x * 0.2 - 555
            e = c - c*y - d
        elif x > 9000 and x <= 35000:
            d = x * 0.25 - 1005
            e = c - c*y - d
        elif x > 35000 and x <= 55000:
            d = x * 0.3 - 2755
            e = c - c*y - d
        elif x > 55000 and x <= 80000:
            d = x * 0.35 - 5505
            e = c - c*y - d
        elif x > 80000:
            d = x * 0.45 - 13505
            e = c - c*y - d
        print(a[0],end=':')
        print(format(e,".2f"))
except ValueError:
    print("Parameter Error")