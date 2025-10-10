#include "interpolation.h"

#include <stdexcept>
#include <vector>

namespace interpolation
{
class LagrangeInterpolator : public Interpolator
{
private:
    std::vector<double> xPoints_;
    std::vector<double> yPoints_;

public:
    LagrangeInterpolator(const std::vector<double>& x, const std::vector<double>& y)
    {
        if (!validate_input(x, y))
        {
            throw std::invalid_argument("Invalid input");
        }
        xPoints_ = x;
        yPoints_ = y;
    }

    double interpolate(double x) const override
    {
        double result = 0.0;
        size_t n = xPoints_.size();

        for (size_t i = 0; i < n; ++i)
        {
            double term = yPoints_[i];

            // 计算拉格朗日基函数L_i(x)
            for (size_t j = 0; j < n; ++j)
            {
                if (i != j)
                {
                    term *= (x - xPoints_[j]) / (xPoints_[i] - xPoints_[j]);
                }
            }

            result += term;
        }

        return result;
    }

    std::vector<double> coefficients() const override
    {
        return yPoints_;
    }

    ~LagrangeInterpolator() override = default;

    double operator()(double x) const override
    {
        return interpolate(x);
    }
};
} // namespace interpolation