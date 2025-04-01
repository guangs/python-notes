# 读取整个文件
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# 按行读取文件
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # 去除换行符

# 读取固定字节数
with open("example.txt", "r") as file:
    content = file.read(10)  # 读取前 10 个字符
    print(content)

# 覆盖写入
with open("example.txt", "w") as file:
    file.write("This is a new line.\n")

# 追加写入
with open("example.txt", "a") as file:
    file.write("This is an appended line.\n")

# 获取当前指针位置
with open("example.txt", "r") as file:
    print(file.tell())  # 输出当前指针位置

# 移动指针位置
with open("example.txt", "r") as file:
    file.seek(5)  # 将指针移动到第 5 个字节
    print(file.read())  # 从第 5 个字节开始读取

# 读取二进制文件
with open("image.jpg", "rb") as file:
    content = file.read()
    print(content[:10])  # 打印前 10 个字节

# 写入二进制文件
with open("copy.jpg", "wb") as file:
    with open("image.jpg", "rb") as source:
        file.write(source.read())

# 文件是否存在
import os

if os.path.exists("example.txt"):
    print("File exists.")
else:
    print("File does not exist.")

# 删除文件

import os

if os.path.exists("example.txt"):
    os.remove("example.txt")
    print("File deleted.")
else:
    print("File does not exist.")


# 文件操作的异常处理
try:
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found.")
except IOError:
    print("An error occurred while accessing the file.")



# 注意，追加模式下，即使通过seek来移动文件指针，写入操作仍然会从文件末尾开始，这是追加模式的设计

# 使用追加模式写入文件
with open("test.txt", "a") as file:
    file.seek(10)  # 尝试将指针移动到第 10 个字节
    file.write(" [INSERTED] ")  # 写入操作仍然会从文件末尾开始


# 使用 "r+" 模式实现替换文件中的 "hello" 为 "hello world"
file_path = "test.txt"

try:
    # 打开文件以读写模式
    with open(file_path, "r+") as file:
        # 读取文件内容
        content = file.read()

        # 替换 "hello" 为 "hello world"
        updated_content = content.replace("hello", "hello world")

        # 将文件指针移动到开头
        file.seek(0)

        # 写入更新后的内容
        file.write(updated_content)

        # 截断文件，防止新内容比原内容短时保留旧内容的残余部分
        file.truncate()

    print("File updated successfully.")
except FileNotFoundError:
    print("File not found.")
except IOError as e:
    print(f"An error occurred while accessing the file: {e}")