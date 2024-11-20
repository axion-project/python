# Reducing Traffic Mortality with Machine Learning
# By Michael Morales

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Load the dataset (replace with your dataset file path)
# Sample columns: Weather, Road Type, Time of Day, Traffic Volume, Accident Severity
data = pd.read_csv("traffic_accident_data.csv")

# Display the first few rows of the dataset
print("Dataset Preview:")
print(data.head())

# Data Preprocessing: Convert categorical data to numerical values
data['Weather'] = data['Weather'].map({'clear': 0, 'rainy': 1, 'snowy': 2, 'foggy': 3})
data['Road Type'] = data['Road Type'].map({'urban': 0, 'rural': 1, 'highway': 2})
data['Time of Day'] = data['Time of Day'].map({'morning': 0, 'afternoon': 1, 'evening': 2, 'night': 3})
data['Traffic Volume'] = data['Traffic Volume'].map({'low': 0, 'medium': 1, 'high': 2})
data['Accident Severity'] = data['Accident Severity'].map({'mild': 0, 'severe': 1})

# Split the dataset into features (X) and target (y)
X = data[['Weather', 'Road Type', 'Time of Day', 'Traffic Volume']]
y = data['Accident Severity']

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

# Feature Importance (to understand which features contribute most to accident severity)
feature_importance = model.feature_importances_
features = X.columns

# Visualize Feature Importance
plt.figure(figsize=(10, 6))
sns.barplot(x=feature_importance, y=features)
plt.title('Feature Importance in Predicting Accident Severity')
plt.show()

# Visualize predictions vs actual values
plt.figure(figsize=(10, 6))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix: Predicted vs Actual Accident Severity')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

# Example prediction (e.g., weather=rainy, road_type=urban, time=afternoon, traffic_volume=high)
sample_input = np.array([[1, 0, 1, 2]])  # Example input (rainy, urban, afternoon, high traffic volume)
predicted_severity = model.predict(sample_input)
severity_map = {0: 'mild', 1: 'severe'}

print(f"\nPredicted Accident Severity for the sample input: {severity_map[predicted_severity[0]]}")
