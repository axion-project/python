# Predicting Credit Card Approvals in Python
# By Michael Morales

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder

# Load the dataset (replace with your dataset file path)
# Sample columns: Income, Age, Credit History, Debt, Previous Applications, Credit Card Approval
data = pd.read_csv("credit_card_applications.csv")

# Display the first few rows of the dataset
print("Dataset Preview:")
print(data.head())

# Data Preprocessing: Handle missing values and encode categorical variables
# Fill missing values with the mean for numerical columns and mode for categorical columns
data.fillna(data.mean(), inplace=True)
data['Credit History'].fillna(data['Credit History'].mode()[0], inplace=True)

# Convert categorical variables to numerical using Label Encoding
label_encoder = LabelEncoder()
data['Credit History'] = label_encoder.fit_transform(data['Credit History'])

# Split the dataset into features (X) and target (y)
X = data[['Income', 'Age', 'Credit History', 'Debt', 'Previous Applications']]
y = data['Credit Card Approval']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Build a Random Forest Classifier model
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
print("\nModel Evaluation:")
print(classification_report(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Feature Importance (to understand which features contribute most to the prediction)
feature_importance = model.feature_importances_
features = X.columns

# Visualize Feature Importance
plt.figure(figsize=(10, 6))
sns.barplot(x=feature_importance, y=features)
plt.title('Feature Importance in Predicting Credit Card Approval')
plt.show()

# Visualize predictions vs actual values
plt.figure(figsize=(10, 6))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix: Predicted vs Actual Credit Card Approval')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

# Example prediction (e.g., Income=50000, Age=30, Credit History=1, Debt=2000, Previous Applications=2)
sample_input = np.array([[50000, 30, 1, 2000, 2]])  # Example input
predicted_approval = model.predict(sample_input)
approval_map = {0: 'Denied', 1: 'Approved'}

print(f"\nPredicted Credit Card Approval: {approval_map[predicted_approval[0]]}")
