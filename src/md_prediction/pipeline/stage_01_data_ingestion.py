import yaml
from pathlib import Path
from md_prediction.components.data_ingestion import DataIngestionConfig, prepare_data

class DataIngestionPipeline:
    def __init__(self, config_path: str):
        self.config_path = config_path
        self.config = self.load_config(config_path)
        self.artifacts_root = Path(self.config["artifacts_root"])

    def load_config(self, config_path: str) -> dict:
        """Load the configuration from the specified YAML file."""
        with open(config_path, "r") as f:
            return yaml.safe_load(f)

    def resolve_path(self, path: str) -> Path:
        """Resolve the path relative to artifacts_root, if not already absolute."""
        path_obj = Path(path)
        if not path_obj.is_absolute():
            return self.artifacts_root / path_obj
        return path_obj

    def run(self) -> None:
        """Run the data ingestion process for all algorithms."""
        for algorithm_name, algorithm_config in self.config["data_ingestion"].items():
            data_config = DataIngestionConfig(
                root_dir=self.resolve_path(algorithm_config["root_dir"]),
                source_URL=algorithm_config["source_URL"],
                local_data_file=self.resolve_path(algorithm_config["local_data_file"]),
                unzip_dir=self.resolve_path(algorithm_config["unzip_dir"])
            )
            print(f"\nPreparing data for {algorithm_name}...")
            prepare_data(data_config)

# Example usage
if __name__ == "__main__":
    pipeline = DataIngestionPipeline("config/config.yaml")
    pipeline.run()