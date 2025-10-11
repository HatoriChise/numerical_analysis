from abc import ABC, abstractmethod
from typing import Union, Optional
import numpy as np

# 尝试导入scipy，用于样条插值
try:
    from scipy.interpolate import CubicSpline

    SCIPY_AVAILABLE = True
except ImportError:
    SCIPY_AVAILABLE = False
    print(
        "Warning: scipy is not installed. Cubic spline interpolation will not be available."
    )


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
        print("Checking data...")
        if len(self.x_data) != len(self.y_data):
            raise ValueError("x_data and y_data must have the same length.")
        if len(self.x_data) != len(set(self.x_data)):
            raise ValueError("x_data must have unique values.")
        print("Data is valid.")


class LagrangeInterpolation(Interpolation):

    def __init__(self, x_data, y_data):
        super().__init__(x_data, y_data)

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


class NewtonInterpolation(Interpolation):
    def __init__(self, x_data, y_data):
        super().__init__(x_data, y_data)
        self.divided_diff = self.compute_divided_differences()

    def compute_divided_differences(self) -> np.ndarray:
        n = len(self.x_data)
        coef = np.copy(self.y_data).astype(float)

        # compute divided differences in-place
        # coef[i] will hold f[x_i, x_{i+1}, ..., x_{i+j}]
        for j in range(1, n):
            for i in range(n - 1, j - 1, -1):
                coef[i] = (coef[i] - coef[i - 1]) / (
                    self.x_data[i] - self.x_data[i - j]
                )
        return coef

    def interpolate(self, x) -> float:
        n = len(self.x_data)
        result = self.divided_diff[n - 1]

        for i in range(n - 2, -1, -1):
            result = result * (x - self.x_data[i]) + self.divided_diff[i]
        return result

    def get_coeficients(self) -> np.ndarray:
        return self.divided_diff
