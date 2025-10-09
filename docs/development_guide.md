# 开发指南

## 项目结构说明

```
numerical_analysis/
├── CMakeLists.txt          # 主CMake构建文件
├── README.md               # 项目说明
├── requirements.txt        # Python依赖项
├── include/                # C++头文件
│   └── numerical_analysis.h # 主要头文件
├── src/                    # C++源代码
│   ├── CMakeLists.txt      # 源码构建文件
│   └── linear_system.cpp   # 线性系统求解实现
├── tests/                  # Python测试和可视化
│   ├── CMakeLists.txt      # 测试构建文件
│   └── test_linear_system.py # 线性系统测试
├── docs/                   # 文档
│   └── development_guide.md # 开发指南
├── examples/               # 示例程序
└── build/                  # 编译输出目录
```

## 构建C++库

1. 进入项目根目录
2. 创建并进入构建目录：
   ```
   mkdir build
   cd build
   ```
3. 运行CMake配置：
   ```
   cmake ..
   ```
4. 编译项目：
   ```
   make
   ```

## 安装Python依赖

在项目根目录下运行：

```
pip install -r requirements.txt
```

## 运行测试

在构建目录中运行：

```
ctest
```

或者直接运行Python测试脚本：

```
python ../tests/test_linear_system.py
```

## 添加新算法

1. 在[include/numerical_analysis.h](file:///home/xiezhenhui/CodeProject/numerical_analysis/include/numerical_analysis.h)中添加函数声明或类定义
2. 在[src/](file:///home/xiezhenhui/CodeProject/numerical_analysis/src/)目录下创建相应的实现文件
3. 在[tests/](file:///home/xiezhenhui/CodeProject/numerical_analysis/tests/)目录下创建对应的Python测试文件
4. 更新文档

## 编码规范

### C++
- 使用C++17标准
- 所有代码放在`numerical_analysis`命名空间中
- 根据功能划分子命名空间（如`linear_system`, `interpolation`等）
- 头文件使用防护宏
- 函数和变量使用小写加下划线命名风格

### Python
- 遵循PEP8编码规范
- 使用类型提示
- 所有测试文件以`test_`开头
- 使用matplotlib进行数据可视化

## 算法实现注意事项

1. 注意数值稳定性
2. 处理边界条件和异常情况
3. 提供清晰的接口文档
4. 实现充分的测试覆盖