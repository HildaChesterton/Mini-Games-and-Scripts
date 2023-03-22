import requests
from bs4 import BeautifulSoup
import csv

# 定义爬虫函数
def spider(url):
    # 发送 HTTP 请求并获取响应
    response = requests.get(url)

    # 解析 HTML 页面
    soup = BeautifulSoup(response.content, 'html.parser')

    # 提取需要的信息
    title = soup.find('h1', class_='title').text.strip()
    author = soup.find('span', class_='author-name').text.strip()
    content = soup.find('div', class_='content').text.strip()

    # 将提取的信息写入 CSV 文件
    with open('data.csv', mode='a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([title, author, content])

# 主函数
if __name__ == '__main__':
    # 待爬取的 URL 列表
    urls = ['https://www.example.com/page1', 'https://www.example.com/page2', 'https://www.example.com/page3']

    # 遍历 URL 列表并调用爬虫函数
    for url in urls:
        spider(url)
