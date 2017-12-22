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
from collections import namedtuple


IncomeTaxQuickLookupItem = namedtuple(
    'IncomeTaxQuickLookupItem',
    ['start_point', 'tax_rate', 'quick_subtractor']
)

INCOME_TAX_START_POINT = 3500

INCOME_TAX_QUICK_LOOKUP_TABLE = [
    IncomeTaxQuickLookupItem(80000, 0.45, 13505),
    IncomeTaxQuickLookupItem(55000, 0.35, 5505),
    IncomeTaxQuickLookupItem(35000, 0.30, 2755),
    IncomeTaxQuickLookupItem(9000, 0.25, 1005),
    IncomeTaxQuickLookupItem(4500, 0.2, 555),
    IncomeTaxQuickLookupItem(1500, 0.1, 105),
    IncomeTaxQuickLookupItem(0, 0.03, 0)
]

SOCIAL_INSURANCE_MONEY_RATE = {
    'endowment_insurance': 0.08,
    'medical_insurance': 0.02,
    'unemployment_insurance': 0.005,
    'employment_injury_insurance': 0,
    'maternity_insurance': 0,
    'public_accumulation_funds': 0.06
}


def calc_income_tax_and_remain(income):
    social_insurance_money = income * sum(SOCIAL_INSURANCE_MONEY_RATE.values())
    real_income = income - social_insurance_money
    taxable_part = real_income - INCOME_TAX_START_POINT
    if taxable_part <= 0:
        return '0.00', '{:.2f}'.format(real_income)
    for item in INCOME_TAX_QUICK_LOOKUP_TABLE:
        if taxable_part > item.start_point:
            tax = taxable_part * item.tax_rate - item.quick_subtractor
            return '{:.2f}'.format(tax), '{:.2f}'.format(real_income - tax)


def main():
    for item in sys.argv[1:]:
        employee_id, income_string = item.split(':')
        try:
            income = int(income_string)
        except ValueError:
            print('Parameter Error')
        _, remain = calc_income_tax_and_remain(income)
        print('{}:{}'.format(employee_id, remain))


if __name__ == '__main__':
main()
	
	
