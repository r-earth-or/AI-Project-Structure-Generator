import os


def create_structure(base_path, data):
    if type(data) == list:
        for item in data:
            create_structure(base_path, item)
        return
    name = data.get('name')
    type_ = data.get('type')
    path = os.path.join(base_path, name)
    if type_ == 'folder':
        # 如果目录不存在，则创建它
        os.makedirs(path, exist_ok=True)
        # 递归创建子目录和文件
        if 'children' in data:
            create_structure(path, data['children'])
    elif type_ == 'file':
        # 创建一个空文件
        with open(path, 'w') as file:
            pass  # 文件已创建，这里不写入任何内容
