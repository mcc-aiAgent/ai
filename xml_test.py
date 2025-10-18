from lxml import html
from bs4 import BeautifulSoup

er = html.etree
xml_doc = """
<?xml version="1.0" encoding="ISO-8859-1"?>
<bookstore>
    <book>
        <title lang="eng">Harry Potter</title>
        <price>29.99</price>
    </book>
    <book>
        <title lang="eng">Learning XML</title>
        <price>39.95</price>
    </book>
</bookstore>

"""

soup = BeautifulSoup(xml_doc, features="lxml")
# print(soup.prettify)
# print(f"========={soup.find_all("book")}")
tag = soup.find("title")
print(tag.name)
print(tag["lang"])
print(tag.string)  # 获取title对应的文本值
print(tag.getText())

# print(soup.getText()) #获取所有文本
