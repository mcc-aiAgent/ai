import requests
from bs4 import BeautifulSoup
import json
from jsonpath import jsonpath
import time
import csv


def scrape_douban_movies():
    # 1. 设置请求头，模拟浏览器访问，避免被拒绝
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    base_url = " https://movie.douban.com/top250"

    # 2. 存储所有电影信息的列表
    all_movies = []

    # 3. 遍历前2页（示例，可调整）
    for start in range(0, 50, 25):  # 每页25条，前2页
        url = f"{base_url}?start={start}"
        print(f"正在抓取: {url}")

        try:
            # 4. 发送HTTP GET请求
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # 如果状态码不是200，抛出异常

            # 5. 使用BeautifulSoup解析HTML，指定lxml解析器[11](@ref)
            soup = BeautifulSoup(response.text, "lxml")

            # 6. 定位到所有电影项（通过CSS选择器）[11](@ref)
            movie_items = soup.select(".item")

            for item in movie_items:
                # 7. 使用BeautifulSoup提取具体信息
                # 电影标题（注意清除多余空格）
                title_elem = item.select_one(".title")
                title = title_elem.get_text(strip=True) if title_elem else "N/A"

                # 评分
                rating_elem = item.select_one(".rating_num")
                rating = rating_elem.get_text(strip=True) if rating_elem else "N/A"

                # 电影详情页链接
                link_elem = item.select_one("a")
                link = (
                    link_elem["href"]
                    if link_elem and link_elem.has_attr("href")
                    else "N/A"
                )

                # 将信息存入字典
                movie_info = {"title": title, "rating": rating, "link": link}
                all_movies.append(movie_info)
                print(f"已抓取: {title} - {rating}")

            # 8. 设置延时，礼貌爬取，避免对服务器造成压力[11](@ref)
            time.sleep(2.5)

        except requests.RequestException as e:
            print(f"请求出错: {e}")
            continue
        except Exception as e:
            print(f"解析出错: {e}")
            continue

    return all_movies


def save_to_csv(movies_data, filename="douban_movies.csv"):
    """将数据保存到CSV文件"""
    if movies_data:
        with open(filename, "w", newline="", encoding="utf-8-sig") as f:
            # 使用DictWriter，表头为字典的key
            writer = csv.DictWriter(f, fieldnames=movies_data[0].keys())
            writer.writeheader()
            writer.writerows(movies_data)
        print(f"数据已保存到 {filename}")


# 主程序入口
if __name__ == "__main__":
    movies_list = scrape_douban_movies()
    if movies_list:
        save_to_csv(movies_list)
        print(f"共抓取 {len(movies_list)} 部电影信息。")
    else:
        print("未抓到数据。")
