import numpy as np
from interpolation import LagrangeInterpolation
from interpolation import NewtonInterpolation
from plot import Plot


def main():
    # 示例用法
    x_data = np.linspace(-10, 10, 13)
    y_data = 1 / (1 + x_data**2)

    x_test_data = np.array([-10, -5, 0, 5, 10])

    lagrange = LagrangeInterpolation(x_data, y_data)
    newton = NewtonInterpolation(x_data, y_data)

    print(f"ture function result: \n{1 / (1 + x_test_data**2)}")
    print(f"lagrange interpolation result: \n{lagrange.interpolate(x_test_data)}")
    print(f"newtown interpolation result: \n{newton.interpolate(x_test_data)}")
    print("newtown interpolation divided differences: \n")
    print(newton.get_coeficients())

    # plot lagrange interpolation result
    Plot.plot(x_data, y_data, lagrange, true_func=lambda x: 1 / (1 + x**2))
    Plot.plot(x_data, y_data, newton, true_func=lambda x: 1 / (1 + x**2))


if __name__ == "__main__":
    main()
