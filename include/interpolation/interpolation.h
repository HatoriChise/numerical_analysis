#ifndef INTERPOLATION_H
#define INTERPOLATION_H

#include <functional>
#include <memory>
#include <vector>

/**
 * @file interpolation.h
 * @brief 数值插值库 - 提供多种插值算法实现
 * @author 谢振辉
 * @version 1.0
 * @date 2025/10/09
 *
 * 包含拉格朗日插值、牛顿插值、样条插值等算法
 */
namespace interpolation
{
// 前向声明（减少依赖）
class Interpolator;

// 枚举和类型定义
enum class Method
{
    LAGRANGE,
    NEWTON,
    HERMITE,
    PIECEWISE_LINEAR,
    CUBIC_SPLINE
};

enum class BoundaryCondition
{
    NATURAL,
    CLAMPED,
    NOT_A_KNOT
};

// 主要类声明
class Interpolator
{
public:
    virtual ~Interpolator() = default;
    virtual double operator()(double x) const = 0;
    virtual double interpolate(double x) const = 0;
    virtual std::vector<double> coefficients() const = 0;
};

// 具体实现类的声明
class LagrangeInterpolator;
class NewtonInterpolator;
class HermiteInterpolator;
class PiecewiseLinearInterpolator;
class CubicSplineInterpolator;

/**
 * @brief 创建插值器的工厂函数
 *
 * 根据指定的方法创建相应的插值器实例
 *
 * @param method 插值方法枚举值
 * @param x 数据点的x坐标向量
 * @param y 数据点的y坐标向量
 * @param derivatives 数据点处的导数值（仅Hermite插值使用）
 * @return std::unique_ptr<Interpolator> 返回指向插值器的智能指针
 * @throws std::invalid_argument 当输入参数无效时抛出异常
 */
std::unique_ptr<Interpolator> create_interpolator(Method method, const std::vector<double> &x,
                                                  const std::vector<double> &y,
                                                  const std::vector<double> &derivatives = {});

/**
 * @brief 验证输入数据的有效性
 *
 * 检查输入的坐标向量是否有效，包括：
 * 1. 向量非空
 * 2. 向量长度相等
 * 3. x坐标严格单调递增
 *
 * @param x 数据点的x坐标向量
 * @param y 数据点的y坐标向量
 * @return bool 输入有效返回true，否则返回false
 */
bool validate_input(const std::vector<double> &x, const std::vector<double> &y);

/**
 * @brief 计算均差表（牛顿插值法所需）
 *
 * 使用递归方法计算给定数据点的均差表，
 * 结果可用于构造牛顿插值多项式
 *
 * @param x 数据点的x坐标向量
 * @param y 数据点的y坐标向量
 * @return std::vector<double> 返回均差表的一维向量形式
 */
std::vector<double> compute_divided_differences(const std::vector<double> &x, const std::vector<double> &y);

} // namespace interpolation

#endif // INTERPOLATION_H