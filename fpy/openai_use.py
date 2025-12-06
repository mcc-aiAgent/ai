import os
from dotenv import load_dotenv, dotenv_values
from pathlib import Path

# 1. 检查当前工作目录和.env文件位置
print("当前工作目录:", os.getcwd())
env_path = Path(".env")
print(".env文件是否存在:", env_path.exists())
print(".env文件的绝对路径:", env_path.absolute())

# 2. 尝试直接读取.env文件的内容，看是否能正确解析
try:
    config = dotenv_values()  # 此方法直接返回一个字典，不修改系统环境变量
    print("通过 dotenv_values() 解析出的内容:", config)
except Exception as e:
    print("解析.env文件时出错:", e)

# 3. 加载环境变量并再次检查
load_dotenv()  # 这会修改 os.environ
api_key_from_env = os.getenv("API_KEY2")
print("通过 os.getenv('API_KEY') 获取的值:", api_key_from_env)

# 4. 检查系统环境变量中是否已存在同名变量（默认不覆盖）
system_api_key = os.environ.get("API_KEY2")
print("系统环境变量中的 API_KEY:", system_api_key)
