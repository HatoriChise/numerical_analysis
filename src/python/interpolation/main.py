import interpolation as interp
import numpy as np


# 示例使用和测试
if __name__ == "__main__":
    # 测试数据
    x_data = np.array([1, 2, 3, 4])
    y_data = 1 / (1 + x_data**2)
    
    # 测试点
    test_points = [2.5, 3.5]
    
    print("Testing interpolation methods:")
    print("Data points: x =", x_data, ", y =", y_data)
    print("Test points:", test_points)
    print()
    
    # 测试线性插值
    try:
        linear = interp.LinearInterpolation(x_data, y_data)
        results = [linear.interpolate(x) for x in test_points]
        print("Linear interpolation results:", results)
    except Exception as e:
        print(f"Linear interpolation error: {e}")
    
    # 测试拉格朗日插值
    try:
        lagrange = interp.LagrangeInterpolation(x_data, y_data)
        results = [lagrange.interpolate(x) for x in test_points]
        print("Lagrange interpolation results:", results)
    except Exception as e:
        print(f"Lagrange interpolation error: {e}")
    
    # 测试牛顿插值
    try:
        newton = interp.NewtonInterpolation(x_data, y_data)
        results = [newton.interpolate(x) for x in test_points]
        print("Newton interpolation results:", results)
    except Exception as e:
        print(f"Newton interpolation error: {e}")