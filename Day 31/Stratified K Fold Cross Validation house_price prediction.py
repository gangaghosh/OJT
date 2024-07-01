import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

# Load the data
data = pd.read_csv('housing_price.csv')

# Prepare features (X) and target (y)
X = data[['size', 'bedrooms']]
y = data['price']

# Create bins for price to use in StratifiedKFold
y_binned = pd.cut(y, bins=3, labels=[0, 1, 2])

# Initialize StratifiedKFold
skf = StratifiedKFold(n_splits=3, shuffle=True, random_state=42)

# Initialize lists to store performance metrics
mse_scores = []
r2_scores = []

# Perform cross-validation
for fold, (train_index, val_index) in enumerate(skf.split(X, y_binned), 1):
    X_train, X_val = X.iloc[train_index], X.iloc[val_index]
    y_train, y_val = y.iloc[train_index], y.iloc[val_index]
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_val_scaled = scaler.transform(X_val)
    
    # Train the model
    model = LinearRegression()
    model.fit(X_train_scaled, y_train)
    
    # Make predictions
    y_pred = model.predict(X_val_scaled)
    
    # Calculate performance metrics
    mse = mean_squared_error(y_val, y_pred)
    r2 = r2_score(y_val, y_pred)
    
    mse_scores.append(mse)
    r2_scores.append(r2)
    
    print(f"Fold {fold}:")
    print(f"  MSE: {mse:.2f}")
    print(f"  R2 Score: {r2:.2f}")

# Print average performance across all folds
print("\nAverage Performance:")
print(f"  MSE: {np.mean(mse_scores):.2f} (+/- {np.std(mse_scores):.2f})")
print(f"  R2 Score: {np.mean(r2_scores):.2f} (+/- {np.std(r2_scores):.2f})")

# # Train final model on all data
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)
# final_model = LinearRegression()
# final_model.fit(X_scaled, y)

# # Function to predict house price
# def predict_price(size, bedrooms):
#     features = np.array([[size, bedrooms]])
#     scaled_features = scaler.transform(features)
#     predicted_price = final_model.predict(scaled_features)
#     return predicted_price[0]

# # Example prediction
# example_size = 1900
# example_bedrooms = 4
# predicted_price = predict_price(example_size, example_bedrooms)
# print(f"\nPredicted price for a {example_size} sq ft house with {example_bedrooms} bedrooms: ${predicted_price:.2f}")