import matplotlib.pyplot as plt
import numpy as np


class Plot:
    def __init__(self):
        pass

    @staticmethod
    def plot(
        x_data,
        y_data,
        interpolator,
        true_func=None,
        x_min=None,
        x_max=None,
        num_points=120,
    ):
        """
        Plot interpolation results and compare with true function.

        Parameters:
        x_data: list or array, original x data points.
        y_data: list or array, original y data points.
        interpolator: interpolator object, must have interpolate method for computing interpolation at any x.
        true_func: callable function, optional, represents the true function f(x) being interpolated.
        x_min: float, optional, minimum value of plotting x range. If None, uses min(x_data).
        x_max: float, optional, maximum value of plotting x range. If None, uses max(x_data).
        num_points: int, optional, number of points used to generate the curve. Default is 100.
        """

        # Set x range
        if x_min is None:
            x_min = min(x_data)
        if x_max is None:
            x_max = max(x_data)

        # Generate dense x points
        x_dense = np.linspace(x_min, x_max, num_points)

        # Calculate interpolated polynomial values at dense points
        y_interp = [interpolator.interpolate(x) for x in x_dense]

        # Plot original data points
        plt.plot(x_data, y_data, "o", label="Original Data", markersize=8)

        # Plot interpolated polynomial curve
        plt.plot(x_dense, y_interp, "-", label="Interpolated Polynomial", linewidth=2)

        # Plot true function curve if provided
        if true_func is not None:
            y_true = [true_func(x) for x in x_dense]
            plt.plot(x_dense, y_true, "--", label="True Function", linewidth=2)

        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        plt.grid(True)
        plt.show()
