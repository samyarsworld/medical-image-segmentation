import os
import sys
from image_segmentation.exception import CustomException
from image_segmentation.logging import logger

class DataValidation:
    def __init__(self, config):
        self.root_dir = config["root_dir"]
        self.data_path = config["data_path"]
        self.required_files = config["required_files"]
        self.status_path = config["status_path"]


    def validate(self) -> bool:
        try:
            status = None
            missing_file = None
            all_files = os.listdir(self.data_path)

            logger.log("Validating started")
            for file in all_files:
                if file not in self.required_files:
                    status = False
                    missing_file = file
                    break
                else:
                    status = True
                
            status = "Success" if status else "Failure"
            with open(self.status_path, 'w') as f:
                f.write(f"Validation status: {status}. File missing: {missing_file}")

            logger.log("Validating finished")

            return status


        except Exception as e:
            exception = CustomException(e, sys)
            logger.exception(exception)
            raise exception

