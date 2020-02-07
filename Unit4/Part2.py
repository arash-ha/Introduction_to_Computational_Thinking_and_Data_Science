"""
Problem 2: R^2
10.0/10.0 points (graded)
After we create some regression models, we also want to be able to evaluate our models to figure out how well each model represents our data, and tell good models from poorly fitting ones. One way to evaluate how well the model describes the data is computing the model's R^2 value. R^2 provides a measure of how well the total variation of samples is explained by the model.

Implement the function r_squared. This function will take in:

list, y, that represents the y-coordinates of the original data samples
estimated, which is a corresponding list of y-coordinates estimated from the regression model
This function should return the computed R^2 value. You can compute R^2 as follows, where  ei  is the estimated y value for the i-th data point (i.e. predicted by the regression),  yi  is the y value for the ith data point, and  mean  is the mean of the original data samples.


If you are still confused about R^2 , its wikipedia page has a good explanation about its use/how to calculate it.

"""

import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"
import numpy as np
def r_squared(y, estimated):
    """
    Calculate the R-squared error term.
    Args:
        y: list with length N, representing the y-coords of N sample points
        estimated: a list of values estimated by the regression model
    Returns:
        a float for the R-squared error term
    """
    # TODO
    y, estimated = np.array(y), np.array(estimated)
    num = ((estimated - y)**2).sum()
    den = (((y.sum()/float(len(y))) - y)**2).sum()
    return 1 - num/den