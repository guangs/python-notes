# Python3在import的时候，默认是绝对引用
# Python2在import的时候，默认是相对引用
# Python3的模块加载机制
# 在 **Python 3** 中，模块加载机制主要依赖于模块的 **搜索路径** 和 **导入方式**。以下是 Python 3 模块加载机制的详细说明：

# ---

# ### **1. 模块加载的基本概念**
# - **模块**：一个模块是一个包含 Python 代码的文件，文件名以 `.py` 结尾。
# - **包**：一个包是一个包含 `__init__.py` 文件的目录，`__init__.py` 可以为空，用于标识该目录是一个包。

# Python 通过 `import` 语句加载模块或包，并执行模块中的代码（如果模块未被缓存）。

# ---

# ### **2. 模块加载的搜索路径**
# Python 在加载模块时，会按照以下顺序搜索模块：

# 1. **当前目录**：
#    - 如果模块在当前脚本所在的目录中，Python 会优先加载。
   
# 2. **`PYTHONPATH` 环境变量**：
#    - 如果设置了 `PYTHONPATH` 环境变量，Python 会在指定的路径中搜索模块。

# 3. **标准库路径**：
#    - Python 会在标准库路径中搜索模块（如 `lib` 目录）。

# 4. **第三方库路径**：
#    - Python 会在 `site-packages` 目录中搜索通过 `pip` 安装的第三方库。

# 5. **`sys.path`**：
#    - Python 会根据 `sys.path` 列表中的路径依次搜索模块。

# #### **查看模块搜索路径**
# 可以通过以下代码查看当前的模块搜索路径：
# ```python
# import sys
# print(sys.path)
# ```

# ---

# ### **3. 模块加载的方式**

# #### **(1) 绝对导入**
# - **描述**：
#   - 从项目的根目录开始，使用完整的路径导入模块。
#   - Python 3 默认使用绝对导入。
# - **示例**：
#   假设目录结构如下：
#   ```
#   project/
#   ├── main.py
#   └── package/
#       ├── __init__.py
#       └── module.py
#   ```

#   在 `main.py` 中：
#   ```python
#   from package import module
#   module.some_function()
#   ```

# #### **(2) 相对导入**
# - **描述**：
#   - 使用 `.` 或 `..` 表示相对路径导入模块。
#   - 只能在包内使用相对导入。
# - **示例**：
#   假设目录结构如下：
#   ```
#   project/
#   └── package/
#       ├── __init__.py
#       ├── module1.py
#       └── module2.py
#   ```

#   在 `module1.py` 中：
#   ```python
#   from . import module2
#   module2.some_function()
#   ```

# #### **(3) 动态导入**
# - **描述**：
#   - 使用 `importlib` 动态加载模块。
# - **示例**：
#   ```python
#   import importlib
#   module = importlib.import_module('package.module')
#   module.some_function()
#   ```

# ---

# ### **4. 模块的缓存机制**
# - Python 会将已加载的模块缓存到 `sys.modules` 中。
# - 如果再次导入相同的模块，Python 会直接从缓存中加载，而不会重新执行模块代码。

# #### **查看已加载的模块**
# ```python
# import sys
# print(sys.modules)
# ```

# ---

# ### **5. `__name__` 和 `__main__`**
# - 当模块被直接运行时，`__name__` 的值为 `"__main__"`。
# - 当模块被导入时，`__name__` 的值为模块的名称。

# #### **示例**：
# ```python
# # module.py
# if __name__ == "__main__":
#     print("This module is being run directly")
# else:
#     print("This module is being imported")
# ```

# 运行 `python module.py`：
# ```
# This module is being run directly
# ```

# 在其他模块中导入：
# ```python
# import module
# ```
# 输出：
# ```
# This module is being imported
# ```

# ---

# ### **6. 常见问题**

# #### **(1) 导入失败**
# - **原因**：
#   - 模块不在 `sys.path` 中。
#   - 文件名冲突（如模块名与标准库模块名相同）。
# - **解决方法**：
#   - 检查模块路径是否正确。
#   - 使用绝对导入避免冲突。

# #### **(2) 循环导入**
# - **原因**：
#   - 两个模块相互导入，导致无限循环。
# - **解决方法**：
#   - 重构代码，避免循环依赖。
#   - 将导入语句放在函数或方法内部。

# ---

# ### **7. 总结**
# - **Python 3 默认使用绝对导入**，相对导入需要显式使用 `.` 或 `..`。
# - 模块加载顺序由 `sys.path` 决定，可以通过修改 `sys.path` 或设置 `PYTHONPATH` 环境变量来调整搜索路径。
# - 模块加载后会缓存到 `sys.modules` 中，避免重复加载。
# - 使用 `__name__ == "__main__"` 判断模块是直接运行还是被导入。

# Python 3 的模块加载机制灵活且强大，合理使用模块和包可以提高代码的可维护性和复用性。