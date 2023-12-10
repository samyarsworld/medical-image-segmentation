from image_segmentation.exception import CustomException
from image_segmentation.logging import logger
import random
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

from torchvision import transforms
import torch

from image_segmentation.utils.networks import SegmentationModel
from image_segmentation.utils.constants import DEVICE, IMG_CHANNELS, MASK_CHANNELS


class TargetPredictionPipeline:
    def __init__(self, config):
        self.config = config.get_target_prediction_config()
        self.test_path = self.config["test_path"]
        self.model_path = self.config["model_path"]

        self.IMG_WIDTH = self.config["IMG_WIDTH"]
        self.IMG_HEIGHT = self.config["IMG_HEIGHT"]
        self.CHANNELS = self.config["channels"]


        self.data_transformer = transforms.Compose([
            # Resize the images
            transforms.Resize(size=(self.IMG_WIDTH, self.IMG_HEIGHT)),
            # Turn the image into a torch.Tensor
            transforms.ToTensor() # this also converts all pixel values from 0 to 255 to be between 0.0 and 1.0
        ])


    def run(self):
        try:
            # Get the list of training data
            test_ids = [sample.name for sample in os.scandir(self.test_path)]

            # Get a random image index
            ind = random.randint(0, len(test_ids) - 1)
            id = test_ids[ind]
            img_path = os.path.join(self.test_path, id, "images", id + ".png")

            img = np.asarray(Image.open(img_path).convert("RGB"))
            img = Image.fromarray(img.astype(np.uint8))
            img = self.data_transformer(img)

            logger.info("IMAGE RECEIVED")

            model = SegmentationModel(in_channels=IMG_CHANNELS, out_channels=MASK_CHANNELS, channels=self.CHANNELS).to(DEVICE)

            model.load_state_dict(torch.load(self.model_path))

            logger.info("MODEL LOADED")
            
            logits = model(img.to(DEVICE).unsqueeze(0)) # Unsqueeze to add the batch dimension (here would be just 1)

            pred = torch.sigmoid(logits)
            pred = (pred > 0.5)

            logger.info("PREDICTION SUCCESSFUL")


            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,5))
        
            ax1.imshow(img.squeeze(dim=0).permute(1,2,0), cmap = 'gray')
            ax1.set_title('Image')


            ax2.imshow(pred.detach().cpu().squeeze(0).permute(1,2,0), cmap = 'gray')
            ax2.set_title('Segmented Image')

            plt.show()
            
    
        except Exception as e:
            exception = CustomException(e, sys)
            logger.exception(exception)
            raise exception  


