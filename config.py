import kagglehub
import pandas as pd
import os

# Download the dataset
path = kagglehub.dataset_download("valakhorasani/gym-members-exercise-dataset")
print("Path to dataset files:", path)

# Assuming the dataset contains CSV files, list all CSV files in the directory
csv_files = [file for file in os.listdir(path) if file.endswith(".csv")]

# Load and display each CSV file
for csv_file in csv_files:
    print(f"\nDisplaying data from: {csv_file}")
    file_path = os.path.join(path, csv_file)
    data = pd.read_csv(file_path)
    print(data.head())  # Display the first few rows of the dataset
