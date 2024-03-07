import difflib
import string
import sys


def file_read(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f'文件不存在：{path}')
        return FileNotFoundError


def translate(text):
    text = text.translate(str.maketrans('', '', string.punctuation)).lower().replace(' ', '')
    return text


def get_copy_percentage(ori_text, copy_text):
    matcher = difflib.SequenceMatcher(None, ori_text, copy_text)
    matching_blocks = matcher.get_matching_blocks()
    matching_amount = sum(block.size for block in matching_blocks)
    copy_percentage = matching_amount / max(len(ori_text), len(copy_text))
    return copy_percentage


def main():
    if len(sys.argv) != 4:
        print("用法：python main.py 原文文件路径 抄袭文件路径 输出文件路径")
        sys.exit(1)

    ori_path, copy_path, output_path = sys.argv[1:]

    ori_text = file_read(ori_path)
    copy_text = file_read(copy_path)

    ori_text = translate(ori_text)
    copy_text = translate(copy_text)

    copy_percentage = get_copy_percentage(ori_text, copy_text)

    with open(output_path, 'w', encoding="utf_8") as output_file:
        output_file.write(f"{copy_percentage:.2%}")


if __name__ == "__main__":
    main()
