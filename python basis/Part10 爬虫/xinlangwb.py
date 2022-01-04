from selenium import webdriver
import csv
import time


def csv_writer(item):
    with open("weibo.csv",'a',encoding="utf-8",newline="")as csvfile:
        writer=csv.writer(csvfile)
        try:
            writer.writerow(item)
        except:
            print("写入失败")
            
def login():
    driver.get('https://weibo.com')
    time.sleep(5)