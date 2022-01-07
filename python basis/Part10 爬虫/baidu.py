import requests
from lxml import etree
response=("https://www.baidu.com/")
response.encode("utf-8").decode("utf-8")
selector=etree.HTML(response.text.encode("utf-8"))