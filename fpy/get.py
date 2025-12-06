import requests as rq

base_url = "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png"
response = rq.get(base_url)
response.encoding = "utf-8"
with open("baidu.png", "wb") as file:
    file.write(response.content)
# print(response.text)

# rq.post()
