import time
import requests

print(time.strftime("开始时间：%Y-%m-%d %H:%m:%S"))
try:
    html_str = requests.get("http://www.google.com", timeout=2).text

except requests.exceptions.RequestException as error:
    print(error)

print(time.strftime("结束时间：%Y-%m-%d %H:%m:%S"))
