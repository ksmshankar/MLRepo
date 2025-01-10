import numpy as np
from sklearn.linear_model import LinearRegression

# Sample data for input 
X = np.array([[1], [2], [3]])
y = np.array([1, 2, 3])

# Model training
model = LinearRegression().fit(X, y)

# Prediction
print('Prediction for 4:', model.predict([[4]]))