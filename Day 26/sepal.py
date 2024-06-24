import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv('sample_dataset.csv')

# Display the first few rows
print(data.head())

# Generate summary statistics
summary_statistics = data.describe()

# Mean and standard deviation of Sepal Length
mean_sepal_length = summary_statistics.loc['mean', 'Sepal Length (cm)']
std_sepal_length = summary_statistics.loc['std', 'Sepal Length (cm)']

print(f"Mean Sepal Length: {mean_sepal_length}")
print(f"Standard Deviation of Sepal Length: {std_sepal_length}")

# Check for missing values
missing_values = data.isnull().sum()
print("Missing values in each column:")
print(missing_values)

# Mapping dictionary
species_mapping = {'FlowerA': 0, 'FlowerB': 1, 'FlowerC': 2}

# Apply mapping
data['Species'] = data['Species'].map(species_mapping)

print(data.head())

# Features and target
X = data.drop('Species', axis=1)
y = data['Species']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=42)

print(f"Training set size: {X_train.shape}")
print(f"Testing set size: {X_test.shape}")

# Initialize decision tree classifier
model = DecisionTreeClassifier(random_state=42)

# Train the model
model.fit(X_train, y_train)

# Plot the tree
# plt.figure(figsize=(20,10))
# plot_tree(model, feature_names=X.columns, class_names=['FlowerA', 'FlowerB', 'FlowerC'], filled=True)
# plt.show()

# Make predictions
y_pred = model.predict(X_test)

# Compute accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Classification report
report = classification_report(y_test, y_pred, target_names=['FlowerA', 'FlowerB', 'FlowerC'])
print("Classification Report:")
print(report)

# Confusion matrix
# conf_matrix = confusion_matrix(y_test, y_pred)
# print("Confusion Matrix:")
# print(conf_matrix)
