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
	
	
	
	
	
	实验楼方法
	
import sys
from collections import namedtuple  #namedtuple让元组的每一项都有一个名字，这样程序就不容易出错，程序更健壮


IncomeTaxQuickLookupItem = namedtuple(   #namedtuple使用先定义一个名字
    'IncomeTaxQuickLookupItem',         #定义的名字IncomeTaxQuickLookupItem
    ['start_point', 'tax_rate', 'quick_subtractor']   #元组中三个元素的名称
)

INCOME_TAX_START_POINT = 3500

INCOME_TAX_QUICK_LOOKUP_TABLE = [               #根据前一个方法的列表，使用namedtuple后列表就变成这样了
    IncomeTaxQuickLookupItem(80000, 0.45, 13505),
    IncomeTaxQuickLookupItem(55000, 0.35, 5505),
    IncomeTaxQuickLookupItem(35000, 0.30, 2755),
    IncomeTaxQuickLookupItem(9000, 0.25, 1005),
    IncomeTaxQuickLookupItem(4500, 0.2, 555),
    IncomeTaxQuickLookupItem(1500, 0.1, 105),
    IncomeTaxQuickLookupItem(0, 0.03, 0)
]

SOCIAL_INSURANCE_MONEY_RATE = {                 #将各项险金比例放入字典
    'endowment_insurance': 0.08,
    'medical_insurance': 0.02,
    'unemployment_insurance': 0.005,
    'employment_injury_insurance': 0,
    'maternity_insurance': 0,
    'public_accumulation_funds': 0.06
}


def calc_income_tax_and_remain(income):
    social_insurance_money = income * sum(SOCIAL_INSURANCE_MONEY_RATE.values())  #将所有值取出用sum求出总和
	                           sum计算总和  括号里是将字典里的所有值都取出                                            
    real_income = income - social_insurance_money
    taxable_part = real_income - INCOME_TAX_START_POINT
    if taxable_part <= 0:      #判断小于3500工资的情况，不用纳税
        return '0.00', '{:.2f}'.format(real_income)  # 直接返回0和扣除险金后的工资
    for item in INCOME_TAX_QUICK_LOOKUP_TABLE:         #用for去遍历个税的表给item
        if taxable_part > item.start_point:          #这里不再使用前例中item【0】的方式了，使用一个名称
            tax = taxable_part * item.tax_rate - item.quick_subtractor
            return '{:.2f}'.format(tax), '{:.2f}'.format(real_income - tax)
                       这个是返回个税字符串             这个是税后工资的字符串

def main():
    for item in sys.argv[1:]:       #获取除自己文件名后面的参数，相当于切片概念
        employee_id, income_string = item.split(':')  #split后的冒号是在字符串中以冒号为分割成两个字符串，第一个传给employee_id第二个传给income_string
        try:
            income = int(income_string)  #开始转成整数，这里还有错误输出的控制
        except ValueError:
            print('Parameter Error')    #错误输出
        _, remain = calc_income_tax_and_remain(income)  #前面的函数是获取到了两个字符串，下划线是将获取的第一个字符串丢弃
        print('{}:{}'.format(employee_id, remain))
		      这个是格式化输出方式，前面是告诉程序要按什么方式将结果打印出来。这里的第一个{}是员工号，冒号后面的一个{}是税后工资，format()是格式化函数，括号里面是需要输出的结果


if __name__ == '__main__':
main()
	
	
