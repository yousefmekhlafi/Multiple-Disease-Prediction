from md_prediction.components.model_evaluation import ModelEvaluator
from md_prediction.config.configuration import ConfigManager

class ModelEvaluationPipeline:
    def __init__(self, config_path):
        self.config_manager = ConfigManager(config_path)

    def run(self):
        evaluator = ModelEvaluator(self.config_manager)
        evaluator.run_evaluation()