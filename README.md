# 批量重命名文件工具

## 📝 项目简介
这是一个用Python写的批量重命名工具，可以把当前文件夹下所有的 `.txt` 文件重命名为 `文件_1.txt`、`文件_2.txt`...

## ✨ 功能特点
- ✅ 自动查找当前目录下所有 `.txt` 文件
- ✅ 按文件名排序，保证结果稳定
- ✅ 避免覆盖已存在的文件
- ✅ 清晰的重命名日志
- ✅ 使用现代 Python 语法（pathlib）

## 🚀 使用方法

### 1. 安装Python
确保你的电脑上安装了Python 3.6+

### 2. 下载代码
好的，请提供您需要翻译的文本。
git clone https://github.com/your-username/rename-files-tool.git
cd 重命名文件工具
3. 运行脚本
Run the Python script rename_files.py.
📸 运行效果
test1.txt -> File_1.txt
test2.txt -> File_2.txt

译文：test2.txt -> File_2.txt
test3.txt -> File_3.txt
💻 技术栈
Python 3.13
pathlib（文件路径处理）
📚 代码说明
核心逻辑
# 1. 获取当前目录下所有.txt文件
txt_files = [对于当前目录中每个名为 f 的文件，如果 f 是文件且其扩展名（小写）为 ".txt" ，则进行迭代。]

# 2. 按文件名排序
txt_files.sort(key=lambda x: x.name)

# 3. 重命名
对于索引和旧文件，按照枚举文本文件从 1 开始：
new_name = f" "File_{index}.txt"
旧文件重命名为新文件
安全机制
检查新旧文件名是否相同，避免无意义的重命名
检查目标文件是否已存在，避免覆盖
🎯 学到的东西
I have learned to write Python code using Cursor AI.
学会了用 pathlib 处理文件路径
学会了文件重命名的逻辑
学会了把代码放到GitHub
🔮 下一步计划
 支持更多文件类型（不只是 .txt）
 支持自定义命名规则（用户可以输入格式）
Add a GUI interface (using tkinter or PyQt)
 支持批量撤销重命名
👤 作者
18好

GitHub: @18ok
学习目标：3个月从零基础到跨境电商单品破万
📄 许可证
与条款

这是我的第一个GitHub项目，用Cursor + AI在1天内完成。如果对你有帮助，欢迎Star⭐！
