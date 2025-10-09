# Python测试配置

# 添加测试
add_test(NAME linear_system_test
         COMMAND python3 ${CMAKE_SOURCE_DIR}/tests/test_linear_system.py)

# 可以添加更多测试...