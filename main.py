from pathlib import Path
from md_prediction.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from md_prediction.pipeline.stage_02_data_validation import DataValidationPipeline
from md_prediction.pipeline.stage_03_model_training import ModelTrainingPipeline
from md_prediction.pipeline.stage_04_model_evaluation import ModelEvaluationPipeline

def main():
    # Define the path to the config.yaml file
    config_path = "config/config.yaml"

    # Run the data ingestion pipeline
    ingestion_pipeline = DataIngestionPipeline(config_path)
    ingestion_pipeline.run()

    # Run the data validation pipeline
    validation_pipeline = DataValidationPipeline(config_path)
    validation_pipeline.run()

    # Running the training pipiline
    training_pipeline = ModelTrainingPipeline(config_path)
    training_pipeline.run()

    #Running evaluation pipeline

    evaluation_pipeline = ModelEvaluationPipeline(config_path)
    evaluation_pipeline.run()

    
if __name__ == "__main__":
    main()