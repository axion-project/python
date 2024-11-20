"""
Data Analytics Script
Author: Michael Morales
Description: This script performs basic data analytics on a given CSV file,
including summary statistics, data visualization, and optional correlation analysis.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys

def load_data(file_path):
    """
    Loads the CSV file into a Pandas DataFrame.
    :param file_path: str, path to the CSV file.
    :return: DataFrame containing the data.
    """
    try:
        data = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}\n")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        sys.exit(1)

def basic_statistics(data):
    """
    Prints basic statistics about the DataFrame.
    :param data: DataFrame to analyze.
    """
    print("Basic Statistics:")
    print(data.describe())
    print("\nMissing Values:")
    print(data.isnull().sum())
    print("\n")

def visualize_data(data, column):
    """
    Generates a histogram for a specified column.
    :param data: DataFrame containing the data.
    :param column: str, column name to visualize.
    """
    try:
        plt.figure(figsize=(8, 6))
        sns.histplot(data[column], kde=True, bins=30, color='blue')
        plt.title(f"Distribution of {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.show()
    except Exception as e:
        print(f"Error visualizing data: {e}")

def correlation_heatmap(data):
    """
    Generates a correlation heatmap for numerical columns.
    :param data: DataFrame containing the data.
    """
    try:
        plt.figure(figsize=(10, 8))
        sns.heatmap(data.corr(), annot=True, cmap="coolwarm", fmt=".2f")
        plt.title("Correlation Heatmap")
        plt.show()
    except Exception as e:
        print(f"Error generating heatmap: {e}")

def main():
    print("Welcome to the Data Analytics Script by Michael Morales!\n")
    
    # Input CSV file
    file_path = input("Enter the path to your CSV file: ")
    data = load_data(file_path)

    # Display basic statistics
    basic_statistics(data)

    # Visualize a column
    column = input("Enter the column name to visualize: ")
    if column in data.columns:
        visualize_data(data, column)
    else:
        print(f"Column '{column}' not found in the data.")

    # Generate a correlation heatmap
    choice = input("Do you want to generate a correlation heatmap? (yes/no): ").strip().lower()
    if choice == "yes":
        correlation_heatmap(data)

if __name__ == "__main__":
    main()
