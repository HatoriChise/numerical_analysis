import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

class InterpolationComparator:
    def __init__(self, xData, yData):
        """
        初始化插值比较器
        :param xData: x轴数据点
        :param yData: y轴数据点
        """
        self.xData = np.array(xData)
        self.yData = np.array(yData)
        self.interpolationMethods = {}
        self.methodColors = {
            'linear': 'blue',
            'cubic': 'red',
            'nearest': 'green',
            'spline': 'purple'
        }
        
    def prepareInterpolationMethods(self):
        """准备不同的插值方法"""
        # 创建更密集的x值用于插值
        self.xNew = np.linspace(self.xData.min(), self.xData.max(), 100)
        
        # 线性插值
        linearInterp = interpolate.interp1d(
            self.xData, self.yData, 
            kind='linear'
        )
        self.interpolationMethods['linear'] = linearInterp
        
        # 三次插值
        cubicInterp = interpolate.interp1d(
            self.xData, self.yData, 
            kind='cubic'
        )
        self.interpolationMethods['cubic'] = cubicInterp
        
        # 最近邻插值
        nearestInterp = interpolate.interp1d(
            self.xData, self.yData, 
            kind='nearest'
        )
        self.interpolationMethods['nearest'] = nearestInterp
        
        # 三次样条插值
        splineInterp = interpolate.CubicSpline(
            self.xData, self.yData
        )
        self.interpolationMethods['spline'] = splineInterp
        
    def plotComparison(self):
        """绘制插值结果对比图"""
        plt.figure(figsize=(12, 8))
        
        # 绘制原始曲线（使用更密集的点来绘制平滑曲线）
        xOriginal = np.linspace(self.xData.min(), self.xData.max(), 200)
        yOriginal = np.sin(xOriginal)  # 假设原始数据是正弦函数
        plt.plot(xOriginal, yOriginal, 
                color='gray', 
                linestyle='--', 
                linewidth=2,
                label='original curve',
                alpha=0.8)
        
        # 绘制原始数据点
        plt.scatter(self.xData, self.yData, 
                   color='black', s=50, 
                   label='original data points', 
                   zorder=5)
        
        # 绘制每种插值方法的结果
        for methodName, interpFunc in self.interpolationMethods.items():
            yNew = interpFunc(self.xNew)
            plt.plot(self.xNew, yNew, 
                    color=self.methodColors[methodName],
                    label=f'{methodName} interpolation', 
                    linewidth=2)
        
        plt.title('Comparison of Different Interpolation Methods', fontsize=14)
        plt.xlabel('X', fontsize=12)
        plt.ylabel('Y', fontsize=12)
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show()

        
    def calculateErrors(self):
        """计算每种插值方法的误差"""
        errors = {}
        for methodName, interpFunc in self.interpolationMethods.items():
            yInterpolated = interpFunc(self.xData)
            mse = np.mean((self.yData - yInterpolated) ** 2)
            errors[methodName] = mse
        return errors
    
    def printErrorComparison(self):
        """打印误差比较结果"""
        errors = self.calculateErrors()
        print("\n MSE:")
        for methodName, error in errors.items():
            print(f"{methodName.capitalize()} interpolation: {error:.6f}")

def main():
    # 示例数据
    xData = np.linspace(0, 2*np.pi, 10)
    yData = np.sin(xData) 
    
    # 创建比较器实例
    comparator = InterpolationComparator(xData, yData)
    
    # 准备插值方法
    comparator.prepareInterpolationMethods()
    
    # 绘制对比图
    comparator.plotComparison()
    
    # 打印误差比较
    comparator.printErrorComparison()

if __name__ == "__main__":
    main()
