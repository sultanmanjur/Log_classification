# %matplotlib inline
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 1. Numpy: create some random data
x = np.arange(10)
y = 3 * x + 5 + np.random.randn(10) * 2
print("x:", x)
print("y:", y)

# 2. Pandas: make a small DataFrame
df = pd.DataFrame({"x": x, "y": y})
print("\nPandas DataFrame:")
print(df.head())

# 3. Seaborn + Matplotlib: quick scatter plot
sns.scatterplot(data=df, x="x", y="y")
plt.title("Scatter plot of x vs y")
plt.show()

# 4. scikit-learn: simple linear regression
model = LinearRegression()
model.fit(x.reshape(-1, 1), y)
print("\nLearned slope:", model.coef_[0])
print("Learned intercept:", model.intercept_)
