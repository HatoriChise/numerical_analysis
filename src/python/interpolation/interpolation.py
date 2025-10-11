from abc import ABC, abstractmethod
from typing import Union, Optional
import matplotlib.pyplot as plt
import numpy as np

# 尝试导入scipy，用于样条插值
try:
    from scipy.interpolate import CubicSpline
    SCIPY_AVAILABLE = True
except ImportError:
    SCIPY_AVAILABLE = False
    print("Warning: scipy is not installed. Cubic spline interpolation will not be available.")


class Interpolation(ABC):
    """
    Base class for interpolation methods.
    Abstract class for interpolation methods.
    """
    def __init__(self, x_data, y_data):
        self.x_data = np.array(x_data)
        self.y_data = np.array(y_data)
        self.checkData()
    
    @abstractmethod
    def interpolate(self, x):
        """
        interpolation method to be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses must implement interpolate method.")
    
    def checkData(self):
        """
        checks if x_data and y_data are valid.
        """
        if len(self.x_data) != len(self.y_data):
            raise ValueError("x_data and y_data must have the same length.")
        if len(self.x_data) != len(set(self.x_data)):
            raise ValueError("x_data must have unique values.")

class LagrangeInterpolation(Interpolation):
    def interpolate(self, x) -> float:
        n = len(self.x_data)
        result = 0.0
        for i in range(n):
            term = self.y_data[i]
            for j in range(n):
                if i != j:
                    term *= (x - self.x_data[j]) / (self.x_data[i] - self.x_data[j])
            result += term
        return result
    
def plot(x_data, y_data, interpolator, true_func=None, x_min=None, x_max=None, num_points=100):
    """
    plot interpolation results and compare with true function.
    
    参数：
    x_data: 列表或数组，原始x数据点。
    y_data: 列表或数组，原始y数据点。
    interpolator: 插值器对象，需有interpolate方法，用于计算任意x的插值。
    true_func: 可调用函数，可选，表示被插值的真实函数f(x)。
    x_min: 浮点数，可选，绘图x范围的最小值。如果为None，则使用min(x_data)。
    x_max: 浮点数，可选，绘图x范围的最大值。如果为None，则使用max(x_data)。
    num_points: 整数，可选，用于生成曲线的点数。默认为100。
    """

    # 设置x范围
    if x_min is None:
        x_min = min(x_data)
    if x_max is None:
        x_max = max(x_data)
    
    # 生成密集x点
    x_dense = np.linspace(x_min, x_max, num_points)
    
    # 计算插值多项式在密集点上的值
    y_interp = [interpolator.interpolate(x) for x in x_dense]
    
    # 绘制原始数据点
    plt.plot(x_data, y_data, 'o', label='Original Data', markersize=8)
    
    # 绘制插值多项式曲线
    plt.plot(x_dense, y_interp, '-', label='Interpolated Polynomial', linewidth=2)
    
    # 如果提供了真实函数，绘制真实曲线
    if true_func is not None:
        y_true = [true_func(x) for x in x_dense]
        plt.plot(x_dense, y_true, '--', label='True Function', linewidth=2)
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    # 示例用法
    x_data = np.linspace(-10, 10, 11)
    y_data = 1 / (1 + x_data**2)
    lagrange = LagrangeInterpolation(x_data, y_data)

    # 绘图示例
    plot(x_data, y_data, lagrange, true_func=lambda x: 1/(1 + x**2))


if __name__ == "__main__":
    main()