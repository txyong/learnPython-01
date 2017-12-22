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
    if len(sys.argv) != 2:        #如果不等于2
        print('Parameter Error')
        exit()
    try:
        income = int(sys.argv[1]) #判断是否为整数,并数值化
    except ValueError:
        print('Parameter Error')
        exit()
    value = income - 3500
    if value <= 0:
        result = 0
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
    print('{:.2f}'.format(result))


if __name__ == '__main__':
main()



实验楼的方法2

def calc_income_tax(income):
    taxable_part = income - 3500
    if taxable_part <= 0:
        return '0.00'
    income_tax_quick_lookup_table = [
        (80000, 0.45, 13505),
        (55000, 0.35, 5505),
        (35000, 0.30, 2755),
        (9000, 0.25, 1005),
        (4500, 0.2, 555),
        (1500, 0.1, 105),
        (0, 0.03, 0)
    ]
    for item in income_tax_quick_lookup_table:
        if taxable_part > item[0]:
            result = taxable_part * item[1] - item[2]
            return '{:.2f}'.format(result)


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
main()


