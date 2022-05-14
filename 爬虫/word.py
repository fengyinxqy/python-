# -*- coding: utf-8 -*-
# @Time    : 2022/3/28 20:25
# @Author  : 肖
# @FileName: word.py
# @Software: PyCharm
# @Blog    ：https:xiaoqiyan.top

from wordcloud import WordCloud
import imageio
import matplotlib.pyplot as plt
import jieba


def read_deal_text():
    with open("comments2.txt", "r", encoding="UTF-8") as f:  # 打开词源文件
        text = f.read()
    cut_text = jieba.cut(text, cut_all=False)  # 分词
    stopwords = set()  # 定义一个停用词集合
    content = [line.strip() for line in open('stopwords.txt', 'r', encoding='UTF-8').readlines()]  # 把停用词按行读到content当中
    stopwords.update(content)  # 加到停用词集合中
    result = '/'.join(cut_text)
    mask = imageio.imread("KFC.png")  # 图片文件路径
    word = WordCloud(background_color="white",
                     stopwords=stopwords,
                     width=800,
                     height=800,
                     font_path=r'C:\Windows\Fonts\FZYTK.TTF',
                     max_words=4000,
                     mask=mask,
                     ).generate(result)  # 画图了
    print("词云图片已保存")

    plt.imshow(word)
    plt.axis("off")
    plt.show()
    word.to_file('weibowordcloud1.png')  # 写为png文件


if __name__ == "__main__":
    read_deal_text()
