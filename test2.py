import sys
import csv
from collections import namedtuple
class Args(object):                     #这个类处理命令行参数 

    def __init__(self):
        self.args = sys.argv[1:]
        

    def _value_after_option(self, option):  #是内部函数是私有的不希望外部调用，一般前面加个下划线，因为下面3个获取配置的函数是一样的，所以此处用一个内部函数做在一起
        
        index = self.args.index(option)
             #这个option传入的参数是-c的话，获取该参数的当前位置,通过args.index()获取
        return self.args[index + 1]


    @property                 #设置成属性的方法，是个装饰器，使用会方便，类里的方法要调用，不调用不会执行
    def config_path(self):          #核心的接口，获得配置文件的路径
        
        return self._value_after_option('-c')

    @property                #如果不用@property的装饰器方法，调用该类就要用args.config_path()这种形式，装饰器就args.config_path来直接调用
    def userdata_path(self):        #获得用户数据的路径
        return self._value_after_option('-d')

    @property
    def export_path(self):          #获得数据输出的路径
        return self._value_after_option('-o')



args = Args()
print(args.userdata_path)

class UserData(object):       #读取用户数据的类，这个接口是需要获取一个列表，但用了迭代器使之成为一个可迭代的对象，这个列表是一个可迭代的对象

    def __init__(self):
        self.userdata = self.read_users_data()  #将数据读取到内部的一个元组表userdata中
    @property
    def read_users_data(self):
        userdata_path = args.userdata_path
        userdata = []
        with open(userdata_path) as f:
            for line in f.readlines():
                employee_id, income_string = line.strip().split(',')
                
                income = int(income_string)
                
                userdata.append((employee_id, income))
        
        return userdata

    def __iter__(self): 
                    #使用iter这个迭代器后使该类变成一个可迭代的对象
        return iter(self.userdata)


class IncomeTaxCalculator(object):      #计算的类

    def __init__(self, userdata):
        self.userdata = userdata   #前面使用了__iter__这个函数，所以这里就可以使用userdata这个列表

    @staticmethod
    def calc_social_insurance_money(income):     #这里是个静态函数与本类联系不紧密，和本类只有一点联系，只需要传入一个income不需要cls或self，完全可以用单独的类来处理
        if income < config.social_insurance_baseline_low:
            return config.social_insurance_baseline_low * \
                config.social_insurance_total_rate
        if income > config.social_insurance_baseline_high:
            return config.social_insurance_baseline_high * \
                config.social_insurance_total_rate
        return income * config.social_insurance_total_rate

    @classmethod                                    #用classmethod装饰器装饰的类函数，不用实例化也能调用的函数，可直接使用IncomeTaxCalculator.calc_income_tax_and_remain()来调用
    def calc_income_tax_and_remain(cls, income):    #普通的函数或类函数必须要用cls或self之类的名称，这里的cls所代表的是当前的这个类 IncomeTaxCalculator()，income是user_data类中获取到的工资
        social_insurance_money = cls.calc_social_insurance_money(income)
        real_income = income - social_insurance_money
        taxable_part = real_income - INCOME_TAX_START_POINT
        if taxable_part <= 0:
            return '0.00', '{:.2f}'.format(real_income)
        for item in INCOME_TAX_QUICK_LOOKUP_TABLE:
            if taxable_part > item.start_point:
                tax = taxable_part * item.tax_rate - item.quick_subtractor
                return '{:.2f}'.format(tax), '{:.2f}'.format(real_income - tax)

    def calc_for_all_userdata(self):              #普通的函数，self是当前类的实例，相当于类的实例化
        result = []
        for employee_id, income in self.userdata:
            data = [employee_id, income]
            social_insurance_money = '{:.2f}'.format(self.calc_social_insurance_money(income))
            tax, remain = self.calc_income_tax_and_remain(income)
            data += [social_insurance_money, tax, remain]
            result.append(data)
        return result

    def export(self, default='csv'):      #这个用于接口的函数将结果输出到文件
        result = self.calc_for_all_userdata()
        with open(args.export_path, 'w', newline='') as f:
            writer = csv.writer(f)    #使用csv这个模块将result这个列表的数据写入文件
            writer.writerows(result)

if __name__ == '__main__':
    userdata = UserData() 
    print(userdata)