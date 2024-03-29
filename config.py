from dotenv import load_dotenv
import os

load_dotenv()

env_path = '.env'
# 检查.env文件是否存在
if not os.path.exists(env_path):
    # 如果不存在，则创建一个新的.env文件
    with open(env_path, 'w') as f:
        f.write("BASE_URL=https://api.poenai.com\n")
        f.write("API_KEY=please input your apikey\n")
        f.write("MODEL=gpt-4-1106-preview\n")
    print("未检测到.env文件，已自动创建并填入默认配置,请填写你的apikey或填入中转url及key")
    exit()


class Config:
    BASE_URL = os.getenv("BASE_URL")
    API_KEY = os.getenv("API_KEY")
    MODEL = os.getenv("MODEL")