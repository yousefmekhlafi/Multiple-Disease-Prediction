import pandas as pd
from pathlib import Path

class DataValidation:
    def __init__(self, config):
        self.config = config
        self.findings = []  # List to store validation findings

    def validate(self):
        # Validate heart disease data
        self.validate_dataset(self.config.heart_disease_train_data, "Heart Disease Train Data")
        self.validate_dataset(self.config.heart_disease_valid_data, "Heart Disease Validation Data")
        self.validate_dataset(self.config.heart_disease_test_data, "Heart Disease Test Data")

        # Validate Parkinson's data
        self.validate_dataset(self.config.parkinsons_train_data, "Parkinson's Train Data")
        self.validate_dataset(self.config.parkinsons_valid_data, "Parkinson's Validation Data")
        self.validate_dataset(self.config.parkinsons_test_data, "Parkinson's Test Data")

        # Validate diabetes data
        self.validate_dataset(self.config.diabetes_train_data, "Diabetes Train Data")
        self.validate_dataset(self.config.diabetes_valid_data, "Diabetes Validation Data")
        self.validate_dataset(self.config.diabetes_test_data, "Diabetes Test Data")

        # Save findings to a text file
        self.save_findings()

    def validate_dataset(self, dataset_path: Path, dataset_name: str):
        # Load the dataset
        try:
            df = pd.read_csv(dataset_path)
            print(f"Validating {dataset_name}...")

            # Check for missing values
            if df.isnull().sum().sum() > 0:
                finding = f"Warning: {dataset_name} contains missing values."
                print(finding)
                self.findings.append(finding)
            else:
                finding = f"{dataset_name} has no missing values."
                print(finding)
                self.findings.append(finding)

            # Check data types
            type_info = f"{dataset_name} data types:\n{df.dtypes}"
            print(type_info)
            self.findings.append(type_info)

            # Check for duplicates
            if df.duplicated().sum() > 0:
                finding = f"Warning: {dataset_name} contains duplicate records."
                print(finding)
                self.findings.append(finding)

            # Additional checks can be added here
            # For example: checking for specific value distributions, etc.

        except FileNotFoundError:
            finding = f"Error: {dataset_name} not found at {dataset_path}"
            print(finding)
            self.findings.append(finding)
        except Exception as e:
            finding = f"Error while validating {dataset_name}: {e}"
            print(finding)
            self.findings.append(finding)

 
    def save_findings(self):
        """Save validation findings to a text file."""
        output_file = Path(self.config.artifacts_root) / "validation_findings.txt"
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, 'w') as f:
            for finding in self.findings:
                f.write(finding + '\n')
        print(f"Validation findings saved to {output_file}")