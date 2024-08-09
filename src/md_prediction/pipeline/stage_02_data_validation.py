from md_prediction.config.configuration import ConfigManager
from md_prediction.components.data_validation import DataValidation

class DataValidationPipeline:
    def __init__(self, config_path: str):
        self.config_manager = ConfigManager(config_path)
        self.data_validation_config = self.config_manager.data_validation_config

    def run(self):
        print("Validating data...")
        validation = DataValidation(self.data_validation_config)
        validation.validate()