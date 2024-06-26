import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score, precision_score, recall_score
from sklearn.model_selection import GridSearchCV

# Load dataset
data = pd.read_csv('loan_data.csv')

# Select features and target
x = data[['loan_id', 'loan_amount', 'interest_rate', 'term', 'income', 'credit_score', 'age', 'employment_length']]
y = data['loan_repaid']

# Split train and test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Initialize model
model = DecisionTreeClassifier(random_state=42)

# Train the model
model.fit(x_train, y_train)

# Make predictions
y_pred = model.predict(x_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy:.2f}")
print("Classification Report:")
print(classification_report(y_test, y_pred))

print('confusion matrix:',)
conf_matrix=confusion_matrix(y_test,y_pred)
print(conf_matrix)

# precision
precision=precision_score(y_test,y_pred)
print("precision:",precision)

# recall
recall=recall_score(y_test,y_pred)
print("recall:",recall)

# F1Score
f1score=f1_score(y_test,y_pred)
print("F1Score:",f1score)