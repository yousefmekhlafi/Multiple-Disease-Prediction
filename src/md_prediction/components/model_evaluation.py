import pickle
import os
import pandas as pd
from sklearn.metrics import accuracy_score
from md_prediction.entity import ModelEvaluationConfig

class ModelEvaluator:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def load_data_for_evaluation(self, model_name):
        # Define paths to the test data for each model
        data_path = self.config.data_paths.get(model_name)
        if not data_path:
            raise ValueError(f"No data path found for model: {model_name}")

        # Load the data (assume it's in CSV format)
        # Adjust the loading method based on your data format
        data = pd.read_csv(data_path)
        X = data.drop('target', axis=1)  # Replace 'target' with your actual target column name
        y = data['target']  # Replace 'target' with your actual target column name

        return X, y

    def run_evaluation(self):
        findings = []
        for model_name, model_info in self.config.models.items():
            model_path = model_info["model_path"]
            # Load the model
            with open(model_path, 'rb') as f:
                model = pickle.load(f)

            # Load the test data for evaluation
            X_test, y_test = self.load_data_for_evaluation(model_name)

            # Perform predictions
            predictions = model.predict(X_test)

            # Calculate accuracy or other metrics
            accuracy = accuracy_score(y_test, predictions)

            # Save findings
            findings.append(f"{model_name} accuracy: {accuracy:.4f}")

        # Write findings to the specified text file
        with open(self.config.findings_file, 'w') as f:
            for finding in findings:
                f.write(finding + '\n')