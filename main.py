# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    for i in range(2500):
        print i
        url = 'http://www.yangpu8k.com.cn/home/index/score_inquiry?number=' + "%04d" % i
        response = requests.get(url)
        time = None
        try:
            soup = BeautifulSoup(response.text, 'html.parser')
            time = soup.find(string='成绩:').next_element.next_sibling.contents[0].strip()
        except Exception as e:
            print str(e)
        with open('result.txt', 'a') as f:
            f.write('%d,%s\n' % (i, time))
            print i, time
            


