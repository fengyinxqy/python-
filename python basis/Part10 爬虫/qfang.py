import requests
from lxml import etree
import csv
import time


def spider():
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'}
    pre_url = 'https://shenzhen.qfang.com/sale/f'
    for x in range(1,11):
        html=requests.get(pre_url+str(x), headers=headers)
        time.sleep(2)
        selector=etree.HTML(html.text)
        house_list=selector.xpath("//*[@id='cycleListings']/ul/li")
        for house in house_list:
            apartment=house.xpath("div[1]/p[1]/a/text()")[0]
            house_layout=house.xpath("div[1]/p[2]/span[2]/text()")[0]
            area = house.xpath("div[1]/p[2]/span[4]/text()")[0]
            region=house.xpath("div[1]/p[3]/span[2]/ap1[/text()")[0]
            total_price=house.xpath("div[2]/span[1]/text()")[0]
            item=[apartment,house_layout,area,region,total_price]
            data_writer(item)
            print('正在抓取')
            
def data_writer(item):
    with open('qfang_ershoufang.csv','a',encoding="utf-8",newline="")as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(item)
        
if __name__ == "__main__":
    spider()
