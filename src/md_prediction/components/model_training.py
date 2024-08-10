from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import pickle
import os

class ModelTrainer:
    def __init__(self, config_manager):
        self.config = config_manager.get_model_training_config()  # Get model configuration

    def train_model(self, X, y, model_name):
        # Drop unnecessary 'name' column from the training data
        X = X.drop(columns=['name'], errors='ignore')

        model_config = self.config[model_name]
        model_type = model_config.model_type
        params = model_config.params
        
        # Identify categorical and numerical columns
        categorical_cols = X.select_dtypes(include=['object']).columns.tolist()
        numerical_cols = X.select_dtypes(exclude=['object']).columns.tolist()
        
        # Create a column transformer
        preprocessor = ColumnTransformer(
            transformers=[
                ('num', StandardScaler(), numerical_cols),
                ('cat', OneHotEncoder(), categorical_cols)
            ])

        # Create a pipeline with preprocessing and model
        if model_type == "LogisticRegression":
            model = Pipeline(steps=[('preprocessor', preprocessor),
                                     ('classifier', LogisticRegression(**params))])
        elif model_type == "SVC":
            model = Pipeline(steps=[('preprocessor', preprocessor),
                                     ('classifier', SVC(**params))])
        else:
            raise ValueError(f"Model type '{model_type}' is not recognized.")

        # Fit the model
        model.fit(X, y)

        # Save the model as a pickle file
        model_output_path = f"artifacts/models/{model_name}.pkl"
        os.makedirs(os.path.dirname(model_output_path), exist_ok=True)
        with open(model_output_path, 'wb') as model_file:
            pickle.dump(model, model_file)

        print(f"{model_name} model trained and saved to {model_output_path}.")