    
import sys,csv
from collections import namedtuple

susuan = namedtuple(
    'susuan',
    ['qizhengdian','shuilv','susuankouchu']
)

SUSUAN_BIAO = [
    susuan(80000,0.45,13505),
    susuan(55000,0.35,5505),
    susuan(35000,0.3,2755),
    susuan(9000,0.25,1005),
    susuan(4500,0.2,555),
    susuan(1500,0.1,105),
    susuan(0,0.03,0)
]
    
class Huoqucfg(object):
    def __init__(self):
        self.huoqu = sys.argv[1:]
    
    def peizhi(self,option):
        index = self.huoqu.index(option)
        return self.huoqu[index+1]
        
    @property
    def cfg_path(self):
        return self.peizhi('-c')
    @property
    def user_path(self):
        return self.peizhi('-d')
    @property
    def shuchu_path(self):
        return self.peizhi('-o')
        
huoqucfg = Huoqucfg()


class Config(object):
    def __init__(self):
        self.config = self.read_conf()
       
    def read_conf(self):
        cnfg_path = huoqucfg.cfg_path
        config = {}
        with open(cnfg_path) as file:
            for line in file.readlines():
                key,values = line.split('=')
                key = key.strip()
                values = values.strip()
                config[key] = float(values)
                       
        return config
    
    def get_config(self, key):
            
        return self.config[key]

    @property    
    def jishulow(self):
        return self.get_config('JiShuL')
    @property    
    def jishuHi(self):
    
        return self.get_config('JiShuH')
    @property    
    def bilvsum(self):
        return sum([self.get_config('YangLao'),
            self.get_config('YiLiao'),
            self.get_config('ShiYe'),
            self.get_config('GongShang'),
            self.get_config('ShengYu'),
            self.get_config('GongJiJin')])
    
    
config = Config()    


class Userdata(object):
    def __init__(self):
        self.userdata = self.read_user()
    
    def read_user(self):
        userdatapath = huoqucfg.user_path
        userdata = []
        with open(userdatapath) as file:
            for line in file.readlines():
                id,gongzi = line.strip().split(',')
                gongzi = int(gongzi)
               
                userdata.append((id,gongzi))
        return userdata
    def __iter__(self):
        return iter(self.userdata)


class Gongzijisuan(object):
    def __init__(self,userdata):
        self.userdata = userdata

    @staticmethod
    def gongzibili(gongzi):
        if gongzi < config.jishulow:
            return config.jishulow * config.bilvsum
        if gongzi > config.jishuHi:
            return config.jishuHi * config.bilvsum
        return gongzi * config.bilvsum

    @classmethod
    def gongzi_shuilv_jisuan(cls,gongzi):
        gongzi_baoxian = cls.gongzibili(gongzi)
        gongzi_shuiqian = gongzi - gongzi_baoxian
        gongzi_qizheng = gongzi_shuiqian - 3500
        if gongzi_qizheng <= 0:
            return "0.00",format(gongzi_shuiqian,".2f")
        for item in SUSUAN_BIAO:
            if gongzi_qizheng > item.qizhengdian:
                shuijin = gongzi_qizheng * item.shuilv - item.susuankouchu
                return '{:.2f}'.format(shuijin),'{:.2f}'.format(gongzi_shuiqian - shuijin)
    
    def userdata_gongzi_jizhong(self):
        shuihou_all = []
        for id,gongzi in self.userdata:
            gongzi_jine = [id,gongzi]
            gongzi_baoxian = '{:.2f}'.format(self.gongzibili(gongzi))
            shuijin,shuihou = self.gongzi_shuilv_jisuan(gongzi)
            gongzi_jine += [gongzi_baoxian,shuijin,shuihou]
            shuihou_all.append(gongzi_jine)
        return shuihou_all



    def shuchu(self,default='csv'):
        user_all = self.userdata_gongzi_jizhong()
        with open(huoqucfg.shuchu_path,'w',newline='') as file:
            writer = csv.writer(file)
            writer.writerows(user_all)


if __name__ == '__main__':
    userdata = Userdata()
    gongzijisuan = Gongzijisuan(Userdata())
    gongzijisuan.shuchu()
    
    