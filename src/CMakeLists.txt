# 创建静态库
add_library(numerical_analysis STATIC)

# 自动添加所有cpp文件
file(GLOB_RECURSE SOURCES "*.cpp")
target_sources(numerical_analysis PRIVATE ${SOURCES})

# 安装规则
install(TARGETS numerical_analysis DESTINATION lib)
install(DIRECTORY ${CMAKE_SOURCE_DIR}/include/ DESTINATION include)

# 添加示例程序
add_executable(solve_linear_system ${CMAKE_SOURCE_DIR}/examples/solve_linear_system.cpp)
target_link_libraries(solve_linear_system numerical_analysis)