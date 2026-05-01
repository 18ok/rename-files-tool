import os
from pathlib import Path

def rename_txt_files():
    current_dir = Path.cwd()
    txt_files = [f for f in current_dir.iterdir() if f.is_file() and f.suffix.lower() == ".txt"]

    # 为了结果稳定，按文件名排序
    txt_files.sort(key=lambda x: x.name)

    for index, old_file in enumerate(txt_files, start=1):
        new_name = f"文件_{index}.txt"
        new_file = current_dir / new_name

        # 如果新名字和旧名字一样，跳过
        if old_file == new_file:
            continue

        # 避免目标文件已存在导致覆盖
        if new_file.exists():
            print(f"跳过：{new_name} 已存在")
            continue

        old_file.rename(new_file)
        print(f"{old_file.name} -> {new_name}")

if __name__ == "__main__":
    rename_txt_files()