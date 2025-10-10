import numpy as np
from typing import Union, List, Optional, Callable
import warnings

class Interpolation:
    """
    插值基类
    提供通用的插值功能和接口定义
    """
    def __init__(self):
        self._x_data = None
        self._y_data = None
        self._is_initialized = False
    
    def initialize(self, x_data: np.ndarray, y_data: np.ndarray) -> bool:
        """
        初始化插值数据
        
        Args:
            x_data: 已知点的x坐标
            y_data: 已知点的y坐标
            
        Returns:
            bool: 初始化是否成功
        """
        if len(x_data) != len(y_data):
            warnings.warn("x_data和y_data长度不一致")
            return False
        
        if len(x_data) < 2:
            warnings.warn("至少需要2个数据点进行插值")
            return False
        
        # 检查x_data是否单调
        if not np.all(np.diff(x_data) > 0):
            warnings.warn("x_data应该是单调递增的")
            return False
        
        self._x_data = np.array(x_data, dtype=float)
        self._y_data = np.array(y_data, dtype=float)
        self._is_initialized = True
        return True
    
    def evaluate(self, x: Union[float, np.ndarray]) -> Union[float, np.ndarray]:
        """
        在给定点进行插值计算（需在子类中实现）
        """
        raise NotImplementedError("evaluate方法需要在子类中实现")
    
    def __call__(self, x: Union[float, np.ndarray]) -> Union[float, np.ndarray]:
        """使类可调用"""
        return self.evaluate(x)
    
    @property
    def is_initialized(self) -> bool:
        """获取初始化状态"""
        return self._is_initialized
    
    @property
    def data_points(self) -> tuple:
        """获取数据点"""
        return (self._x_data.copy(), self._y_data.copy())