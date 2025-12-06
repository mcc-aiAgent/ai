# http://bbs.itheima.com/forum-426-3.html
import requests


def load_page(url):
    # headers = {
    #     "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 QuarkPC/4.5.5.535"
    # }
    response = requests.get(url)

    return response.text


def save_file(html, filename):
    print("正在保存：" + filename)
    with open(filename, "w", encoding="utf-8") as file:
        file.write(html)


def heima(begen_page, end_page):
    for page in range(begen_page, end_page + 1):
        url = f"http://bbs.itheima.com/forum-426-{page}.html"
        file_name = "第" + str(page) + "页.html"
        html = load_page(url)
        save_file(html, file_name)


beigin_page = int(input("请输入开始的页码："))
end_page = int(input("请输入结束的页码："))
heima(beigin_page, end_page)
