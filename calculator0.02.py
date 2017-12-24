#!/usr/bin/env python3
import sys
try:
    a = int(float(sys.argv[1]))
    if len(sys.argv) == 2:     #判断参数数量
        x = a - 3500          
        if x <= -3500:          #判断参数是否小于0
            print("Parameter Error")
        else:
            if x > -3500 and x < 1:
                b = 0
            elif x <= 1500:
                b = x * 0.03
            elif x >1500 and x <= 4500:
                b = x * 0.1 - 105
            elif x > 4500 and x <= 9000:
                b = x * 0.2 - 555
            elif x > 9000 and x <= 35000:
                b = x * 0.25 - 1005
            elif x > 35000 and x <= 55000:
                b = x * 0.3 - 2755
            elif x > 55000 and x <= 80000:
                b = x * 0.35 - 5505
            elif x > 80000:
                b = x * 0.45 - 13505
            print(format(b,".2f"))
    else:
        print("Parameter Error 01")
except IndexError:
    print("Parameter Error")
except ValueError:
    print("Parameter Error")
except NameError:
    print("Parameter Error")


	
	
实验楼的方式1

import sys


def main():
    if len(sys.argv) != 2:        #如果传入的参数数量（len()是统计数量）不等于2，此处用于检查是否传入了正确的参数数量
        print('Parameter Error')
        exit()
    try:
        income = int(sys.argv[1]) #判断是否为整数,并转换成整数,传给income
    except ValueError:
        print('Parameter Error')
        exit()                    #遇到异常就退出,一般的小异常会用打印日志,如果一有异常就退出,会导致程序关闭.
    value = income - 3500
    if value <= 0:               #小于0,就是工资小于3500
        result = 0               #强制置为0
    elif 0 < value <= 1500:
        result = value * 0.03 - 0
    elif 1500 < value <= 4500:
        result = value * 0.1 - 105
    elif 4500 < value <= 9000:
        result = value * 0.2 - 555
    elif 9000 < value <= 35000:
        result = value * 0.25 - 1005
    elif 35000 < value <= 55000:
        result = value * 0.3 - 2755
    elif 55000 < value <= 80000:
        result = value * 0.35 - 5505
    else:
        result = income * 0.45 - 13505
    print('{:.2f}'.format(result))     #format格式化输出


if __name__ == '__main__':
    main()



实验楼的方法2   代码要遵循PEP8 Python 编码规范

def calc_income_tax(income):
    taxable_part = income - 3500
    if taxable_part <= 0:             #先判断小于0
        return '0.00'                 #直接返回0
    income_tax_quick_lookup_table = [   #包含元组的列表
        (80000, 0.45, 13505),
        (55000, 0.35, 5505),
        (35000, 0.30, 2755),
        (9000, 0.25, 1005),
        (4500, 0.2, 555),
        (1500, 0.1, 105),
        (0, 0.03, 0)
    ]
    for item in income_tax_quick_lookup_table:  #一个一个元素的获取,第一次获取的是(80000, 0.45, 13505)，名称也要遵循pep8
        if taxable_part > item[0]:               #将第一个获取的(80000, 0.45, 13505)第0个值取出进行判断
            result = taxable_part * item[1] - item[2]
            return '{:.2f}'.format(result)       #这个return是条件执行了就退出,不继续循环了


def main():
    import sys
    if len(sys.argv) != 2:
        print('Parameter Error')
        exit()
    try:
        income = int(sys.argv[1])
    except ValueError:
        print('Parameter Error')
        exit()
    print(calc_income_tax(income))


if __name__ == '__main__':
    main()                         #开始调用函数,前面的函数是先定义,还没开始调用执行,是从这个开始调用.


