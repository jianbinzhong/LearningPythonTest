#_*_ coding:utf-8 _*_
_author_='BlackMb'

import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

import urllib2
import urllib
import json

class ZuiMei(object):
    def __init__(self):
        #通过chrome抓包获取headers
        self.url = 'http://www.zuimeitianqi.com/zuimei/queryWeather'
        self.headers={}
        self.headers['User-Agent']='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
        self.cities ={}
        #城市的ID
        self.cities['怀化']='01011505'
        self.cities['衡阳']='01011504'
        self.cities['长沙']='01011502'
        self.cities['益阳']='01011510'
        self.cities['成都']='01012703'
        self.data={}
        self.city='长沙'

    def query(self,city='长沙'):
        if city not in self.cities:
            print 'data null,暂不支持该城市'
            return None

        self.city=city
        data = urllib.urlencode({'cityCode':self.cities[self.city]}).encode('UTF-8')
        req = urllib2.Request(self.url,data,self.headers)
        response = urllib2.urlopen(req)

        html = response.read().decode('UTF-8','r')
        #print html
        self.json_parse(html)

    def json_parse(self,html):
        target = json.loads(html)
        high_temp=target['data'][0]['actual']['high']
        low_temp=target['data'][0]['actual']['low']
        chengdu_desc=target['data'][0]['actual']['desc']
        print 'the lowest tempture is: '+low_temp+'\nand the high tempture is: '+\
              high_temp+'\nand the quality of the air is: '+chengdu_desc

if __name__ == '__main__':
    zuimei = ZuiMei()
    zuimei.query("成都")
