from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pickle
import os
import numpy as np
import pandas as pd
from md_prediction.entity import ModelEvaluationConfig


class ModelEvaluator:
    def __init__(self, config_manager):
        self.config = config_manager.model_evaluation_config

    def evaluate_model(self, X_test, y_test, model_name):
        # Load the model
        model_path = self.config.models[model_name]['model_path']
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file '{model_path}' not found.")

        with open(model_path, 'rb') as model_file:
            model = pickle.load(model_file)

        # Make predictions
        try:
            predictions = model.predict(X_test)
        except ValueError as e:
            print(f"Error during prediction for {model_name}: {e}")
            return  # Exit if predictions can't be made

        # Calculate evaluation metrics
        accuracy = accuracy_score(y_test, predictions)
        precision = precision_score(y_test, predictions, average='weighted', zero_division=0)
        recall = recall_score(y_test, predictions, average='weighted', zero_division=0)
        f1 = f1_score(y_test, predictions, average='weighted', zero_division=0)

        # Create evaluation metrics dictionary
        metrics_dict = {
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "f1_score": f1,
        }

        # Ensure the output directory exists
        model_metrics_dir = os.path.join('artifacts', 'evaluation', model_name)  # Use model_name for sub-directory
        os.makedirs(model_metrics_dir, exist_ok=True)

        # Save metrics to a CSV file
        metrics_path = os.path.join(model_metrics_dir, f"{model_name}_metrics.csv")  # Unique file for each model
        metrics_df = pd.DataFrame([metrics_dict])
        metrics_df.to_csv(metrics_path, index=False)

        print(f"Evaluation metrics for {model_name} saved to {metrics_path}.")

    def evaluate_all_models(self, X_test, y_test, model_names):
        for model_name in model_names:
            self.evaluate_model(X_test, y_test, model_name)

    def run_evaluation(self):
        # Load test data
        heart_disease_test = pd.read_csv(self.config.data_paths['heart_disease'])
        parkinsons_test = pd.read_csv(self.config.data_paths['parkinsons'])
        diabetes_test = pd.read_csv(self.config.data_paths['diabetes'])

        # Split data into features and target
        heart_disease_X = heart_disease_test.drop(columns=['target'])  # Ensure 'target' matches your dataset
        heart_disease_y = heart_disease_test['target']
        
        parkinsons_X = parkinsons_test.drop(columns=['status'])  # Ensure 'status' matches your dataset
        parkinsons_y = parkinsons_test['status']
        
        diabetes_X = diabetes_test.drop(columns=['Outcome'])  # Ensure 'Outcome' matches your dataset
        diabetes_y = diabetes_test['Outcome']

        # Call evaluate_all_models with the respective data
        self.evaluate_all_models(heart_disease_X, heart_disease_y, ['heart_disease'])
        self.evaluate_all_models(parkinsons_X, parkinsons_y, ['parkinsons'])
        self.evaluate_all_models(diabetes_X, diabetes_y, ['diabetes'])