import yaml
from pathlib import Path
from md_prediction.entity import DataIngestionConfig, MultiAlgorithmDataIngestionConfig, DataValidationConfig, ModelTrainingConfig, ModelEvaluationConfig
 

class ConfigManager:
    def __init__(self, config_path: str):
        self.config_path = config_path
        self.config = self.load_config()
        self.data_ingestion_config = self.get_data_ingestion_config()
        self.data_validation_config = self.get_data_validation_config()
        self.model_evaluation_config = self.get_model_evaluation_config()

    def load_config(self):
        with open(self.config_path, "r") as f:
            return yaml.safe_load(f)

    def get_data_ingestion_config(self) -> MultiAlgorithmDataIngestionConfig:
        artifacts_root = Path(self.config["artifacts_root"])
        return MultiAlgorithmDataIngestionConfig(
            algorithms={
                key: DataIngestionConfig(
                    root_dir=artifacts_root / Path(algorithm["root_dir"]),
                    source_URL=algorithm["source_URL"],
                    local_data_file=artifacts_root / Path(algorithm["local_data_file"]),
                    unzip_dir=artifacts_root / Path(algorithm["unzip_dir"])
                )
                for key, algorithm in self.config["data_ingestion"].items()
            }
        )

    def get_data_validation_config(self) -> DataValidationConfig:
        artifacts_root = Path(self.config["artifacts_root"])
        return DataValidationConfig(
            artifacts_root=artifacts_root,
            heart_disease_train_data=artifacts_root / Path(self.config["data_validation"]["heart_disease"]["train_data_file"]),
            heart_disease_valid_data=artifacts_root / Path(self.config["data_validation"]["heart_disease"]["valid_data_file"]),
            heart_disease_test_data=artifacts_root / Path(self.config["data_validation"]["heart_disease"]["test_data_file"]),
            parkinsons_train_data=artifacts_root / Path(self.config["data_validation"]["parkinsons"]["train_data_file"]),
            parkinsons_valid_data=artifacts_root / Path(self.config["data_validation"]["parkinsons"]["valid_data_file"]),
            parkinsons_test_data=artifacts_root / Path(self.config["data_validation"]["parkinsons"]["test_data_file"]),
            diabetes_train_data=artifacts_root / Path(self.config["data_validation"]["diabetes"]["train_data_file"]),
            diabetes_valid_data=artifacts_root / Path(self.config["data_validation"]["diabetes"]["valid_data_file"]),
            diabetes_test_data=artifacts_root / Path(self.config["data_validation"]["diabetes"]["test_data_file"]),
        )
    

    def get_model_training_config(self):
        """Get the model training configuration."""
        return {
        model_name: ModelTrainingConfig(
            model_type=model_config['model_type'],
            params=model_config['params'],
            scaler=model_config.get('scaler', 'StandardScaler')  # Default to StandardScaler if not provided
        )
        for model_name, model_config in self.config["model_training"].items()
    }
    
    def get_model_evaluation_config(self):
        artifacts_root = Path(self.config["artifacts_root"])  # Use the correct key
        return ModelEvaluationConfig(
        metrics_path=artifacts_root / Path(self.config["model_evaluation"]["metrics_file"]),
        findings_file=artifacts_root / Path(self.config["model_evaluation"]["findings_file"]),
        models=self.config["model_evaluation"]["models"],
        data_paths=self.config["model_evaluation"]["data_paths"]
    )
