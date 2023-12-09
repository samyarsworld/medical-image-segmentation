import os
import torch
import sys
from image_segmentation.logging import logger
from image_segmentation.exception import CustomException
# from datasets import load_from_disk


class ModelTrainer:
    def __init__(self, config):
        self.root_dir = config["root_dir"]
        self.data_path = config["data_path"]
        # self.model_ckpt = config["model_ckpt"]
        # self.main_path = config["main_path"]

        self.h_params = config["h_params"]


    def train(self):
        # Device agnostic training
        DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
        
        try:

            logger.info(f"Getting model")


            logger.info(f"Model received")


            logger.info(f"Training started")

            # trainer.train()


            logger.info(f"Training finished")


            logger.info(f"Saving the model...")

            # ## Save model
            # model.save_pretrained(os.path.join(self.main_path, "model"))
            # ## Save tokenizer
            # tokenizer.save_pretrained(os.path.join(self.main_path, "tokenizer"))

            logger.info(f"Model saved at")


        except Exception as e:
            exception = CustomException(e, sys)
            logger.exception(exception)
            raise exception
        


       
