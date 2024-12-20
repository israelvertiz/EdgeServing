from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
import joblib

# Generate sample data for regression
X, y = make_regression(n_samples=100, n_features=3, noise=0.1, random_state=42)

# Train a simple linear regression model
model = LinearRegression()
model.fit(X, y)

# Save the model to a pickle file
joblib.dump(model, 'model.pkl')

print("Linear Regression model saved as 'model.pkl'")
