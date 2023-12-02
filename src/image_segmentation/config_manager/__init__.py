from image_segmentation.utils import read_yaml, create_directories
from pathlib import Path
from typing import Dict

CONFIG_PATH = Path("config/config.yaml")
class ConfigManager:
    def __init__(self, config_filepath = CONFIG_PATH):
        self.config = read_yaml(config_filepath)
        self.params = self.config["model_trainer"]["h_params"]

        # Create directories: does not override files and folders that already exist 
        create_directories([self.config["artifacts_root"]])

    
    def get_data_ingestion_config(self) -> Dict:
        config = self.config["data_ingestion"]
        create_directories([config["root_dir"]])

        return config

    def get_data_validation_config(self) -> Dict:
        config = self.config["data_validation"]
        create_directories([config["root_dir"]])

        return config
    
    def get_data_transformation_config(self) -> Dict:
        config = self.config["data_transformation"]
        create_directories([config["root_dir"]])

        return config

    def get_model_trainer_config(self) -> Dict:
        config = self.config["model_trainer"]
        create_directories([config["root_dir"], config["root_dir"] + "/" + config["algorithm_name"]])

        return config

    def get_model_evaluation_config(self) -> Dict:
        config = self.config["model_evaluation"]
        create_directories([config["root_dir"]])

        return config
    
    def get_target_prediction_config(self) -> Dict:
        config = self.config["target_prediction"]
        create_directories([config["root_dir"]])

        return config

