from urllib.request import urlopen 
html=urlopen("https://www.douban.com/")
response = html.read()
print(response)