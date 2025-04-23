from pathlib import Path

# 创建路径对象
p = Path("/Users/guang/github/python-notes")
print(p)  # 输出: /Users/guang/github/python-notes

p = Path("/Users/guang/github") / "python-notes" / "08-concurrency"
print(p)  # 输出: /Users/guang/github/python-notes/08-concurrency

p = Path("/Users/guang/github/python-notes/08-concurrency/07-coroutine-practice2.py")
print(p.name)    # 输出: 07-coroutine-practice2.py
print(p.stem)    # 输出: 07-coroutine-practice2
print(p.suffix)  # 输出: .py
print(p.parent)  # 输出: /Users/guang/github/python-notes/08-concurrency


p = Path("/Users/guang/github/python-notes/08-concurrency/07-coroutine-practice2.py")
print(p.exists())   # 输出: True 或 False
print(p.is_file())  # 输出: True
print(p.is_dir())   # 输出: False

p = Path("/Users/guang/github/new-folder/file.txt")
p.unlink()  # 删除文件

d = Path("/Users/guang/github/new-folder")
d.rmdir()  # 删除空目录


p = Path("/Users/guang/github/python-notes")
for item in p.iterdir():
    print(item)  # 输出目录下的所有文件和子目录