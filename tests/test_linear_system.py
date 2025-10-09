#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
线性方程组求解算法测试脚本
"""

import numpy as np
import matplotlib.pyplot as plt
import sys
import os

# 添加build目录到Python路径，以便导入C++扩展
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'build'))

try:
    # 如果有编译好的C++扩展模块可以在这里导入
    # import numerical_analysis_cpp as na
    pass
except ImportError:
    print("警告: 未找到C++扩展模块，使用纯Python实现进行测试")

def gaussian_elimination_python(A, b):
    """
    Python实现的高斯消元法（用于验证和对比）
    """
    n = len(b)
    # 创建增广矩阵的副本
    augmented = np.hstack([A.copy(), b.copy().reshape(-1, 1)])
    
    # 前向消元
    for i in range(n):
        # 部分主元选择
        max_row = np.argmax(np.abs(augmented[i:, i])) + i
        augmented[[i, max_row]] = augmented[[max_row, i]]
        
        # 检查是否为奇异矩阵
        if abs(augmented[i, i]) < 1e-10:
            raise RuntimeError("矩阵为奇异矩阵")
        
        # 消元
        for k in range(i + 1, n):
            factor = augmented[k, i] / augmented[i, i]
            augmented[k, i:] -= factor * augmented[i, i:]
    
    # 回代
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (augmented[i, -1] - np.dot(augmented[i, i+1:n], x[i+1:n])) / augmented[i, i]
    
    return x

def test_gaussian_elimination():
    """
    测试高斯消元法
    """
    print("测试高斯消元法:")
    
    # 测试案例1
    A1 = np.array([
        [2.0, 1.0, -1.0],
        [-3.0, -1.0, 2.0],
        [-2.0, 1.0, 2.0]
    ])
    b1 = np.array([8.0, -11.0, -3.0])
    
    print("测试案例1:")
    print("A = ", A1)
    print("b = ", b1)
    
    try:
        x1 = gaussian_elimination_python(A1, b1)
        print("解 x = ", x1)
        
        # 验证解
        residual = np.dot(A1, x1) - b1
        print("残差 = ", residual)
        print("残差范数 = ", np.linalg.norm(residual))
        print()
    except Exception as e:
        print("错误:", str(e))
        print()
    
    # 测试案例2
    A2 = np.array([
        [1.0, 2.0, 3.0],
        [4.0, 5.0, 6.0],
        [7.0, 8.0, 10.0]
    ])
    b2 = np.array([1.0, 2.0, 3.0])
    
    print("测试案例2:")
    print("A = ", A2)
    print("b = ", b2)
    
    try:
        x2 = gaussian_elimination_python(A2, b2)
        print("解 x = ", x2)
        
        # 验证解
        residual = np.dot(A2, x2) - b2
        print("残差 = ", residual)
        print("残差范数 = ", np.linalg.norm(residual))
        print()
    except Exception as e:
        print("错误:", str(e))
        print()

def performance_comparison():
    """
    性能对比测试
    """
    print("性能对比测试:")
    
    sizes = [10, 50, 100, 200]
    python_times = []
    
    for n in sizes:
        # 生成随机测试案例
        np.random.seed(42)  # 固定种子确保可重复性
        A = np.random.rand(n, n)
        b = np.random.rand(n)
        
        # 测试Python实现的时间
        import time
        start_time = time.time()
        try:
            x = gaussian_elimination_python(A, b)
            end_time = time.time()
            python_times.append(end_time - start_time)
            print(f"大小 {n}x{n}: Python用时 {end_time - start_time:.4f} 秒")
        except Exception as e:
            print(f"大小 {n}x{n}: 计算失败 - {str(e)}")
            python_times.append(float('inf'))
    
    # 绘制性能对比图
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, python_times, 'bo-', label='Python实现')
    plt.xlabel('矩阵大小')
    plt.ylabel('求解时间 (秒)')
    plt.title('高斯消元法性能测试')
    plt.legend()
    plt.grid(True)
    plt.yscale('log')
    plt.savefig('gaussian_elimination_performance.png')
    plt.show()

if __name__ == "__main__":
    test_gaussian_elimination()
    performance_comparison()