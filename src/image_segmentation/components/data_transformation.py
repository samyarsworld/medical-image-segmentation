import os
import sys
from image_segmentation.logging import logger
from image_segmentation.exception import CustomException

class DataTransformation:
    def __init__(self, config):
        self.root_dir = config["root_dir"]
        # self.data_path = config["data_path"]


    def transform(self):
        try:
            logger.info(f"Data transformation started")

            # Download the dataset in zip format, the use extract zip to unzip

            logger.info(f"Data transformation finished")

        except Exception as e:
            exception = CustomException(e, sys)
            logger.exception(exception)
            raise exception
        