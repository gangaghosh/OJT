# The first array will have the mean set to 5.0 with a standard deviation of 1.0.

# The second array will have the mean set to 10.0 with a standard deviation of 2.0:

# Example
# A scatter plot with 1000 dots:

import numpy as np
import matplotlib.pyplot as plt
x = np.random.normal(5.0, 1.0, 1000)
y = np.random.normal(10.0, 2.0, 1000)

plt.scatter(x, y)
plt.show()