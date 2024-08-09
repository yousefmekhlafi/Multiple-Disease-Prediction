import pandas as pd
from md_prediction.components.model_training import ModelTrainer
from md_prediction.config.configuration import ConfigManager

class ModelTrainingPipeline:
    def __init__(self, config_path):
        self.config_manager = ConfigManager(config_path)

    def run(self):
        # Load your heart disease data
        heart_disease_data = pd.read_csv(self.config_manager.data_validation_config.heart_disease_train_data)
        parkinsons_data = pd.read_csv(self.config_manager.data_validation_config.parkinsons_train_data)
        diabetes_data = pd.read_csv(self.config_manager.data_validation_config.diabetes_train_data)

        # Split data into features (X) and target (y)
        heart_disease_X = heart_disease_data.drop(columns=['target'])  # Replace 'target_column' with actual target column name
        heart_disease_y = heart_disease_data['target']  # Replace 'target_column' with actual target column name
        
        parkinsons_X = parkinsons_data.drop(columns=['status'])  # Replace 'status' with actual target column name
        parkinsons_y = parkinsons_data['status']  # Replace 'status' with actual target column name
        
        diabetes_X = diabetes_data.drop(columns=['Outcome'])  # Replace 'Outcome' with actual target column name
        diabetes_y = diabetes_data['Outcome']  # Replace 'Outcome' with actual target column name

        trainer = ModelTrainer(self.config_manager)

        # Train models
        trainer.train_model(heart_disease_X, heart_disease_y, 'heart_disease')
        trainer.train_model(parkinsons_X, parkinsons_y, 'parkinsons')
        trainer.train_model(diabetes_X, diabetes_y, 'diabetes')