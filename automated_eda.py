import dask.dataframe as dd
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import plotly.express as px
import logging

# Set up logging for better error tracking and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Optimized data loading with Dask for handling larger datasets
def load_large_data(file_path):
    try:
        logging.info(f"Loading data from {file_path}")
        data = dd.read_csv(file_path)
        logging.info(f"Data loaded successfully, with {data.shape[0]} rows.")
        return data
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        raise

# Automated EDA: Statistics and Visualizations
def perform_eda(data):
    logging.info("Performing basic EDA")
    
    # Convert to Pandas for small datasets (use Dask for large datasets)
    data_pandas = data.compute() if isinstance(data, dd.DataFrame) else data
    
    # Descriptive statistics
    print("\nDescriptive Statistics:\n", data_pandas.describe())

    # Check for missing values
    missing = data_pandas.isnull().sum()
    print("\nMissing Values:\n", missing[missing > 0])

    # Correlation heatmap
    corr_matrix = data_pandas.corr()
    plt.figure(figsize=(12, 10))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    plt.title("Correlation Heatmap")
    plt.show()

    # Distribution plots for numeric columns
    numeric_columns = data_pandas.select_dtypes(include=np.number).columns
    for col in numeric_columns:
        plt.figure(figsize=(8, 6))
        sns.histplot(data_pandas[col], kde=True)
        plt.title(f"Distribution of {col}")
        plt.show()

# Dimensionality Reduction with PCA
def perform_pca(data):
    from sklearn.decomposition import PCA
    
    logging.info("Performing PCA for dimensionality reduction")
    
    # Prepare the data for PCA
    numeric_columns = data.select_dtypes(include=np.number).columns
    X = data[numeric_columns].dropna()  # Drop rows with NaN values for PCA
    
    # Standardize the data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    
    # Plot PCA results
    pca_df = pd.DataFrame(data=X_pca, columns=['PCA1', 'PCA2'])
    pca_df['Target'] = data['target']  # Assuming 'target' column is present for coloring
    
    fig = px.scatter(pca_df, x='PCA1', y='PCA2', color='Target', title="PCA - 2D Visualization")
    fig.show()

# Model Training and Evaluation
def train_and_evaluate_model(data):
    logging.info("Training and evaluating a machine learning model")
    
    # Prepare data for training (Assumes 'target' column exists)
    X = data.drop(columns=['target'])
    y = data['target']
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Standardize features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Initialize and train RandomForest model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test_scaled)
    
    # Evaluation metrics
    print(classification_report(y_test, y_pred))
    
    # Confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=np.unique(y), yticklabels=np.unique(y))
    plt.title('Confusion Matrix')
    plt.show()

def main():
    logging.info("Expert-level EDA and Machine Learning Pipeline Started")
    
    # Load data
    file_path = input("Enter the path to the dataset (CSV format): ")
    data = load_large_data(file_path)
    
    # Perform EDA
    perform_eda(data)
    
    # Perform PCA (if target column exists)
    if 'target' in data.columns:
        perform_pca(data)
    
    # Train and evaluate the model
    if 'target' in data.columns:
        train_and_evaluate_model(data)

if __name__ == "__main__":
    main