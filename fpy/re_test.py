import re

regex_obj = re.compile(r"[\u4e00-\u9fa5]+")
print(type[regex_obj])

str1 = regex_obj.findall("你好啊:dog")
print(str1)
