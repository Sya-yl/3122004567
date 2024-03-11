import difflib
import string
import sys


def file_read(path):  # 读取文件内容
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f'文件不存在：{path}')
        return FileNotFoundError


def translate(text):  # 去除文本中的标点符号，并改成全部小写
    text = text.translate(str.maketrans('', '', string.punctuation)).lower().replace(' ', '')
    return text


def get_copy_percentage(ori_text, copy_text):
    # 创建匹配对象
    matcher = difflib.SequenceMatcher(None, ori_text, copy_text)
    # 获取匹配内容
    matching_blocks = matcher.get_matching_blocks()
    # 计算匹配内容的长度
    matching_amount = sum(block.size for block in matching_blocks)
    # 计算查重率
    copy_percentage = matching_amount / max(len(ori_text), len(copy_text))
    return copy_percentage


def main():
    # 输入文件
    if len(sys.argv) != 4:
        print("用法：python main.py 原文文件路径 抄袭文件路径 输出文件路径")
        sys.exit(1)
    # 保存输入的对应文件路径
    ori_path, copy_path, output_path = sys.argv[1:]
    # 文本读取
    ori_text = file_read(ori_path)
    copy_text = file_read(copy_path)
    # 文本预处理
    ori_text = translate(ori_text)
    copy_text = translate(copy_text)
    # 计算查重率
    copy_percentage = get_copy_percentage(ori_text, copy_text)
    # 写入输出文件
    with open(output_path, 'w', encoding="utf_8") as output_file:
        output_file.write(f"{copy_percentage:.2%}")


if __name__ == "__main__":
    main()
