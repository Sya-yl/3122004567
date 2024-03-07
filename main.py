def file_read(path):
    try :
        with open(path, 'r', encoding='utf-8')
            return file.read()
    except FileNotFoundError:
        print(f'文件不存在：{path}')
        return FileNotFoundError


