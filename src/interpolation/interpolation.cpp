/**
 * @file interpolation.cpp
 * @brief 数值插值库实现
 */
#include <algorithm>
#include <cmath>
#include <iostream>
#include <stdexcept>

#include "interpolation.h"

namespace interpolation
{
// tool function to check if x values are distinct
bool validate_input(const std::vector<double>& x, const std::vector<double>& y)
{
    if (x.size() != y.size())
    {
        throw std::invalid_argument("x and y must have the same length");
    }
    if (x.size() < 2)
    {
        throw std::invalid_argument("At least two data points are required");
    }

    for (size_t i = 1; i < x.size(); ++i)
    {
        if (x[i] <= x[i - 1])
        {
            throw std::invalid_argument("x values must be strictly increasing");
        }
    }
    return true;
}

/**
 * @brief todo
 * @return std::vector<double>
 */
std::vector<double> compute_divided_differences(const std::vector<double>& x, const std::vector<double>& y)
{
    if (x.size() != y.size() || x.empty())
        throw std::invalid_argument("Invalid input data for divided differences");
    std::cout << "code not implemented" << std::endl;
    return std::vector<double>();
}


} // namespace interpolation