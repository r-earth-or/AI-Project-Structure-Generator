import json

from create_structure import create_structure
from request_openai import request_openai


def main():
    project_path = input("请输入项目目录，默认为本文件所处目录")
    if project_path == "":
        project_path = "."
    project_require = input("请输入")
    try:
        response = request_openai(project_require)
        response_dict = json.loads(response)
        print("JSON解析成功，正在创建")
        create_structure(project_path, response_dict)
        print("创建成功")
    except json.JSONDecodeError:
        print("解析失败")
        print(response)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
