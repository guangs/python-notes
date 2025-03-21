import re


# re.match(pattern, string, flags=0)
# pattern: 匹配的正则表达式 
# string: 要匹配的字符串
# flags: 标志位，用于控制正则表达式的匹配方式，如：
    # re.I(re.IGNORECASE): 忽略大小写
    # re.M(re.MULTILINE): 多行模式，改变'^'和'$'的行为
    # re.S(re.DOTALL): 点任意匹配模式，改变'.'的行为
    # re.X(re.VERBOSE): 详细模式，忽略空白字符和#号的注释
    # re.U(re.UNICODE): Unicode模式
    # re.L(re.LOCALE): 本地化模式
    # re.A(re.ASCII): ASCII模式
# 返回值: 匹配成功返回一个匹配对象，否则返回None

pattern = r'\d+'  # 匹配一个或多个数字
string = '123abc456'

match = re.match(pattern, string)
if match:
    print(match.group())  # 输出: 123




# re.search(pattern, string, flags=0)
pattern = r'\d+'  # 匹配一个或多个数字
string = 'abc123def'

search = re.search(pattern, string)
if search:
    print(search.group())  # 输出: 123



# re.findall(pattern, string, flags=0)
pattern = r'\d+'  # 匹配一个或多个数字
string = 'abc123def456ghi789'

matches = re.findall(pattern, string)
print(matches)  # 输出: ['123', '456', '789']


# re.sub(pattern, repl, string, count=0, flags=0)
pattern = r'\d+'  # 匹配一个或多个数字
string = 'abc123def456ghi789'

result = re.sub(pattern, '#', string)
print(result)  # 输出: abc#def#ghi#



# re.split(pattern, string, maxsplit=0, flags=0)

pattern = r'\d+'  # 匹配一个或多个数字
string = 'abc123def456ghi789'

result = re.split(pattern, string)
print(result)  # 输出: ['abc', 'def', 'ghi', '']


# re.compile(pattern, flags=0)
# 译正则表达式模式，以便重复使用, 提高效率
pattern = re.compile(r'\d+')  # 编译正则表达式
string = 'abc123def456ghi789'

matches = pattern.findall(string)
print(matches)  # 输出: ['123', '456', '789']