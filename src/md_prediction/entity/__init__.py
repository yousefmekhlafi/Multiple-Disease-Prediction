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
    def __init__(self, models: Dict[str, str], findings_file: str):
        self.models = models  # Make sure this is defined
        self.findings_file = findings_file