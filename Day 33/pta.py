# 1. Data Preprocessing

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score, mean_squared_error
import seaborn as sns

# Load the dataset
data = pd.read_csv('data.csv')

# Check for missing values
print(data.isnull().sum())

# No missing values, so we can proceed
# Separate features and target
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)


# 2.Exploratory Data Analysis (EDA)

# Statistical summary
print("\nStatistical Summary:")
print(data.describe())

# Visualizations
plt.figure(figsize=(12, 8))
sns.pairplot(data, hue='target')
plt.suptitle('Pairplot of Iris Dataset', y=1.02)
plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(data.iloc[:, :-1].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# 3. Classification

models = {
    'Logistic Regression': LogisticRegression(),
    'Decision Tree': DecisionTreeClassifier(),
    'Random Forest': RandomForestClassifier()
}

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    print(f"\n{name}:")
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    
# 4. Regression

X_reg = data.iloc[:, 1:]  # Using all features except the first one
y_reg = data.iloc[:, 0]   # Using the first feature as the target

X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)

reg_models = {
    'Linear Regression': LinearRegression(),
    'Decision Tree Regressor': DecisionTreeRegressor()
}

for name, model in reg_models.items():
    model.fit(X_train_reg, y_train_reg)
    y_pred_reg = model.predict(X_test_reg)
    
    print(f"\n{name}:")
    print(f"R-squared: {r2_score(y_test_reg, y_pred_reg):.3f}")
    print(f"MSE: {mean_squared_error(y_test_reg, y_pred_reg):.3f}")
    
    
# 5. Confusion Matrix Visualization

# Assuming X_train, y_train, X_test, y_test are already defined
# Encode string labels into integers
label_encoder = LabelEncoder()
y_train_encoded = label_encoder.fit_transform(y_train)
y_test_encoded = label_encoder.transform(y_test)

# Fit the RandomForest model
rf_model = RandomForestClassifier()
rf_model.fit(X_train, y_train_encoded)
y_pred = rf_model.predict(X_test)

# Generate the confusion matrix
cm = confusion_matrix(y_test_encoded, y_pred)

# Plot the confusion matrix
plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix for Random Forest')
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.show()

# 6. Cross-Validation 

for name, model in models.items():
    cv_scores = cross_val_score(model, X_scaled, y, cv=5)
    print(f"\n{name}:")
    print(f"Cross-validation scores: {cv_scores}")
    print(f"Mean CV score: {cv_scores.mean():.3f} (+/- {cv_scores.std() * 2:.3f})")