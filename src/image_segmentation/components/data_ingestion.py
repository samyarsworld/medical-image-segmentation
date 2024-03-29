import os
import sys
import boto3
from dotenv import load_dotenv
import zipfile
from io import BytesIO

from image_segmentation.logging import logger
from image_segmentation.exception import CustomException

class DataIngestion:
    def __init__(self, config):
        self.root_dir = config["root_dir"]
        self.data_folder_path = config["data_folder_path"]
        self.AWS_BUCKET_NAME = config["AWS_BUCKET_NAME"]
        self.AWS_DATASET_NAME = config["AWS_DATASET_NAME"]

    def download_files_from_cloud(self):
        """
        Downloads the files from AWS s3 to the data directory

        """        
        # Load environmental variables from .env file
        load_dotenv('.env')

        AWS_ACCESS_KEY_ID=os.environ.get("AWS_ACCESS_KEY_ID")
        AWS_SECRET_ACCESS_KEY=os.environ.get("AWS_SECRET_ACCESS_KEY")
        AWS_REGION=os.environ.get("AWS_REGION")
        
        try:
            # Create an S3 client
            s3 = boto3.client(service_name='s3', region_name=AWS_REGION, aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
            logger.info(f"Connection successful to AWS")
            
            logger.info(f"Download dataset started...")

            # Read the zip file from S3
            response = s3.get_object(Bucket=self.AWS_BUCKET_NAME, Key=self.AWS_DATASET_NAME)
            datasetZip = response['Body'].read()

            # Extract all contents to a specified directory
            self.extract_zip(datasetZip)

            logger.info(f"Download successful!")
        except Exception as e:
            exception = CustomException(e, sys)
            logger.exception(exception)
            raise exception


    def extract_zip(self, datasetZip):
        """
        Extracts the zip file into the data directory

        """
        logger.info(f"Unzip started...")

        # Create a BytesIO object from the zip file content
        zip_buffer = BytesIO(datasetZip)
        try:
            with zipfile.ZipFile(zip_buffer, 'r') as zip_ref:
                zip_ref.extractall(self.data_folder_path)
            logger.info(f"Unzip finished")

        except Exception as e:
            exception = CustomException(e, sys)
            logger.exception(exception)
            raise exception
        