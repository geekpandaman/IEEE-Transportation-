import re
import requests
import random
from IEEEsql import *

def get_kwords(id_num):
    r = requests.get('https://ieeexplore.ieee.org/document/%s' % (id_num))
    #m = re.findall('"IEEE Keywords","kwd":\[(-[,"\w\s]+)\]',r.text)
    m = re.findall('"IEEE Keywords","kwd":\[([^\]]*)',r.text)
    #m = re.search('"IEEE Keywords"',r.text)
    #m = re.findall('"IEEE Keywords"',r.text)
    try:
            return m[0]
    except IndexError:
            print('fail to get_kwords')
            return 'no IEEE kwd!'


def get_paperurl(manu_url):
        r = requests.get(manu_url)
        m = re.findall('art-abs-title-(\d+)">([,-:\w\s\d]+)',r.text)
        pub_years = re.findall('Publication Year: ([0-9]{4})',r.text)
        cit_nums = re.findall('Papers \((\d+)\)',r.text)
        while len(cit_nums) < len(m):
                cit_nums.append('0')
        for i in range(0,len(m)):
                kwd=get_kwords(m[i][0])
                info = {}
                info['id_name'] = m[i][0]
                info['title'] = m[i][1]
                info['pub_year'] = pub_years[i]
                info['cit_num'] = cit_nums[i]
                info['kwd'] = kwd
                paper_db(info)


#sort by citations
manu_url="https://ieeexplore.ieee.org/xpl/tocresult.jsp?isnumber=33692&punumber=6979"


get_paperurl(manu_url)
