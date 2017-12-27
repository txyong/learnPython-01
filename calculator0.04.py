    
import sys,csv
shuijin = [
    (80000,0.45,13505),
    (55000,0.35,5505),
    (35000,0.3,2755),
    (9000,0.25,1005),
    (4500,0.2,555),
    (1500,0.1,105),
    (0,0.03,0)
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
        print(self.peizhi('-c'))
        return self.peizhi('-d')
    
    #def shuchu_path(self):
        #return self.peizhi('-o')
        
huoqucfg = Huoqucfg()

class Config(object):
    def __init__(self):
        self.conf = self.read_conf()
        
    def read_conf(self):
        cnfg_path = huoqucfg.cfg_path
        config = {}
        with open(cnfg_path) as file:
            for line in file.readlines():
                key,values = line.split('=')
                key = key.strip()
                values = values.strip()
                #config(key) = float(values)
                
        return config
        
    def jishulow(self):
        jishu = self.config[key]
        return jishu('JiShuL')
        
    def jishuHi(self):
        jishu = self.config[key]
        return jishu(JiShuH)
        
    def bilvsum(self):
        bili = self.config[key]
        return sum([self.bili('YangLao'),
            self.bili('YiLiao'),
            self.bili('ShiYe'),
            self.bili('GongShang'),
            self.bili('ShenYu'),
            self.bili('GongJiJin')])
       
    
    
    
config = Config()    


class userdata(object):
    def __init__(self):
        self.user = self.read_user()
        
    def read_user(self):
        userdatapath = huoqucfg.user_path
        userdata = []
        with open(userdatapath) as file:
            for line in file.readlines():
                id,gongzi = line.split(',')
                #gongzi = int(gongzi)
                print(id)
                #userdata.append((id,gongzi))
        print(userdatapath)        
        return userdata
        
    
