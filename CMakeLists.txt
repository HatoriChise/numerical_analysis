cmake_minimum_required(VERSION 3.10)

project(NumericalAnalysis CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 设置编译器选项
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -O2")

# 包含头文件目录
include_directories(include)

# 添加子目录
add_subdirectory(src)

# 启用测试
enable_testing()
add_subdirectory(tests)