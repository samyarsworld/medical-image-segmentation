import sys
from image_segmentation.logging import logger
from image_segmentation.exception import CustomException
from image_segmentation.utils.dataset import ImageDataset
from torchvision import transforms
from torch.utils.data import DataLoader

class DataConstruction:
    def __init__(self, config):
        self.root_dir = config["root_dir"]
        self.train_path = config["train_path"]
        self.h_params = config["h_params"]

        self.TRAIN_SIZE = self.h_params["TRAIN_SIZE"]
        self.IMG_WIDTH = self.h_params["IMG_WIDTH"]
        self.IMG_HEIGHT = self.h_params["IMG_HEIGHT"]
        self.BATCH_SIZE = self.h_params["BATCH_SIZE"]

        self.data_transformer = transforms.Compose([
            # Resize the images
            transforms.Resize(size=(self.IMG_WIDTH, self.IMG_HEIGHT)),
            # Turn the image into a torch.Tensor
            transforms.ToTensor() # this also converts all pixel values from 0 to 255 to be between 0.0 and 1.0
        ])
    
    def build(self):
        try:
            logger.info(f"Data construction started")

            train_dataset = ImageDataset(self.train_path, True, self.TRAIN_SIZE, self.data_transformer)
            validation_dataset = ImageDataset(self.train_path, False, self.TRAIN_SIZE, self.data_transformer)

            train_loader = DataLoader(dataset=train_dataset, batch_size=self.BATCH_SIZE, shuffle=False)
            validation_loader = DataLoader(dataset=validation_dataset, batch_size=self.BATCH_SIZE, shuffle=False)

            logger.info(f"Data construction finished")

            return train_dataset, validation_dataset, train_loader, validation_loader

        except Exception as e:
            exception = CustomException(e, sys)
            logger.exception(exception)
            raise exception

        
        