import os


def create_structure(base_path, data):
    for entry in data:
        name = entry['name']
        type_ = entry['type']
        path = os.path.join(base_path, name)

        if type_ == 'folder':
            # 如果目录不存在，则创建它
            os.makedirs(path, exist_ok=True)
            # 递归创建子目录和文件
            if 'children' in entry:
                create_structure(path, entry['children'])
        elif type_ == 'file':
            # 创建一个空文件
            with open(path, 'w') as file:
                pass  # 文件已创建，这里不写入任何内容
