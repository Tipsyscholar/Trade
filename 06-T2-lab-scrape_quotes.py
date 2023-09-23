#import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

context = ssl._create_unverified_context() #表示忽略未经核实的SSL证书认证

all_quotes = []

url = f'https://quotes.toscrape.com/page/1/' # 目标网址
# 用浏览器打开网址，查看源代码
page = urlopen(url,context = context) # 请求网页信息
# 将网页信息组合为BeautifulSoup结构，利用HTML解析器
soup = BeautifulSoup(page, 'html.parser') 
# 搜寻quote标记
quotes = soup.find_all('div', class_='quote')
# 逐行测试代码，理解各行的意义
for quote in quotes:
    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    tags = quote.find('div', class_='tags').find_all('a')

    tags_list = []
    for tag in tags:
        tags_list.append(tag.text)
    single_quote = [text, author, tags_list]
    all_quotes.append(single_quote)
    print(all_quotes)

"""
任务：
1. 完整理解基础代码的功能和结果（即对每一行基础代码添加注释）；
2. 添加代码，爬取相同网站的10个页面内容，并将爬取内容存储在同一个CSV格式文件；  
3. 模拟会员登录过程。
（提示：调用selenium库，
  目标网页： http://quotes.toscrape.com/login
  参考信息：https://www.thepythoncode.com/article/automate-login-to-websites-using-selenium-in-python
  任意username和password都可登录成功，例如：username = "username" password = "password" ）
4. 爬取虚拟书店的书籍信息，并存储为CSV格式，图片单独命名存储。
包含图片、价格、评价，书名等书籍所有内容。
网址： http://books.toscrape.com
参考内容：https://towardsdatascience.com/image-scraping-with-python-a96feda8af2d
5. 爬豆瓣影评信息
网址：https://movie.douban.com/
爬取：年度排行榜电影的影评
要求：至少一类电影的影评、至少10也影评
比如：评分最高的外国语电影
"""