import os
import sys
# from pathlib import Path
from dotenv import load_dotenv
import zipfile
from io import BytesIO
# import requests

from image_segmentation.logging import logger
from image_segmentation.exception import CustomException



class DataIngestion:
    def __init__(self, config):
        self.root_dir = config["root_dir"]
        self.data_url = config["data_url"]
        self.data_path = config["data_path"]

        
    def download_files(self):
        """
        Downloads the files from the dataset url

        """
        try:
            logger.info(f"Downloading data from {self.data_url} into file {self.data_path}")

            # Download the dataset in zip format, the use extract zip to unzip

            logger.info(f"Download complete.")

            return self.data_path
        except Exception as e:
            exception = CustomException(e, sys)
            logger.exception(exception)
            raise exception



    def extract_zip(self):
        """
        Extracts the zip file into the data directory

        """
        try:
            with zipfile.ZipFile(self.data_path, 'r') as zip_ref:
                zip_ref.extractall()
            logger.info(f"Extracting zip file: {self.data_path}")

        except Exception as e:
            exception = CustomException(e, sys)
            logger.exception(exception)
            raise exception
        