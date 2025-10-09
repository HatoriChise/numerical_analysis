#ifndef INTERPOLATION_H
#define INTERPOLATION_H

#include <vector>
#include <memory>
#include <functional>

/**
 * @file interpolation.h
 * @brief 数值插值库 - 提供多种插值算法实现
 * @author 谢振辉
 * @version 1.0
 * @date 2025/10/09
 * 
 * 包含拉格朗日插值、牛顿插值、样条插值等算法
 */

namespace interpolation {
    
    // 前向声明（减少依赖）
    class Interpolator;
    
    // 枚举和类型定义
    enum class Method {
        LAGRANGE,
        NEWTON,
        HERMITE,
        PIECEWISE_LINEAR,
        CUBIC_SPLINE
    };
    
    enum class BoundaryCondition {
        NATURAL,
        CLAMPED,
        NOT_A_KNOT
    };
    
    // 主要类声明
    class Interpolator {
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
    
    // 工厂函数声明
    std::unique_ptr<Interpolator> create_interpolator(
        Method method,
        const std::vector<double>& x,
        const std::vector<double>& y,
        const std::vector<double>& derivatives = {}
    );
    
    // 工具函数声明
    bool validate_input(const std::vector<double>& x, const std::vector<double>& y);
    std::vector<double> compute_divided_differences(const std::vector<double>& x, const std::vector<double>& y);
    
} // namespace interpolation

#endif // INTERPOLATION_H
