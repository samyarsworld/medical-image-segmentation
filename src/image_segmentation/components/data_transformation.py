import os
import sys
from image_segmentation.logging import logger
from image_segmentation.exception import CustomException
from image_segmentation.components.dataset import ImageDataset
from torchvision import transforms
from torch.utils.data import DataLoader

class DataTransformation:
    def __init__(self, config):
        self.root_dir = config["root_dir"]
        self.base_train_path = config["base_train_path"]
        self.train_size = config["train_size"]
        self.image_width = config["image_width"]
        self.image_height = config["image_height"]

        # self.data_path = config["data_path"]

        self.data_transformer = transforms.Compose([
            # Resize the images
            transforms.Resize(size=(self.image_width, self.image_height)),
            # Turn the image into a torch.Tensor
            transforms.ToTensor() # this also converts all pixel values from 0 to 255 to be between 0.0 and 1.0
        ])

    def transform(self):
        try:
            logger.info(f"Data transformation started")

            train_dataset = ImageDataset(self.base_train_path, True, self.train_size, self.data_transformer)
            validation_dataset = ImageDataset(self.base_train_path, False, self.train_size, self.data_transformer)

            # Download the dataset in zip format, the use extract zip to unzip

            logger.info(f"Data transformation finished")

        except Exception as e:
            exception = CustomException(e, sys)
            logger.exception(exception)
            raise exception
        