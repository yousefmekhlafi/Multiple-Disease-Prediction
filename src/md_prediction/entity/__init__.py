from dataclasses import dataclass
from pathlib import Path
from typing import Dict

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class MultiAlgorithmDataIngestionConfig:
    algorithms: Dict[str, DataIngestionConfig]


@dataclass(frozen=True)
class DataValidationConfig:
    artifacts_root: Path
    heart_disease_train_data: Path
    heart_disease_valid_data: Path
    heart_disease_test_data: Path
    parkinsons_train_data: Path
    parkinsons_valid_data: Path
    parkinsons_test_data: Path
    diabetes_train_data: Path
    diabetes_valid_data: Path
    diabetes_test_data: Path

@dataclass
class ModelTrainingConfig:
    def __init__(self, model_type: str, params: dict, scaler: str = "StandardScaler"):
        self.model_type = model_type
        self.params = params
        self.scaler = scaler 


@dataclass
class ModelEvaluationConfig:
    def __init__(self, metrics_path, findings_file, models, data_paths):
        self.metrics_path = metrics_path
        self.findings_file = findings_file
        self.models = models
        self.data_paths = data_paths
        # Add metrics attributes
        self.accuracy = None
        self.precision = None
        self.recall = None
        self.f1_score = None

    def to_dict(self):
        return {
            "metrics_path": self.metrics_path,
            "findings_file": self.findings_file,
            "models": self.models,
            "data_paths": self.data_paths,
            "accuracy": self.accuracy,
            "precision": self.precision,
            "recall": self.recall,
            "f1_score": self.f1_score,
        }