import torch
from torch import nn
import sys
from image_segmentation.logging import logger
from image_segmentation.exception import CustomException
from image_segmentation.utils.constants import DEVICE, IMG_CHANNELS, MASK_CHANNELS
from image_segmentation.components.networks import SegmentationModel
# from datasets import load_from_disk
import numpy as np
from tqdm import tqdm


class ModelTrainer:
    def __init__(self, config):
        self.root_dir = config["root_dir"]
        # self.pre_trained_model = config["pre_trained_model"]
        self.model_path = config["model_path"]

        self.h_params = config["h_params"]
        self.EPOCHS = self.h_params["epochs"]
        self.LR = self.h_params["lr"]
        self.CHANNELS = self.h_params["channels"]

        # Model initialization
        self.model = SegmentationModel(in_channels=IMG_CHANNELS, out_channels=MASK_CHANNELS, channels=self.CHANNELS).to(DEVICE)

        # Optimizer
        self.optimizer = torch.optim.Adam(params=self.model.parameters(), lr=self.LR)

        # Loss functions
        self.loss_fn = nn.BCEWithLogitsLoss()


    def training(self, data_loader, model, optimizer, loss_fn):
        tot_loss = 0.0
        model.train()

        # Loop through batches (with progress bar)
        for images, masks in tqdm(data_loader):
            images = images.to(DEVICE)
            masks = masks.to(DEVICE)

            # Calculate the predictions (logits)
            logits = model(images)

            # Calculate the loss
            loss = loss_fn(logits, masks)

            # Set grads to zero
            optimizer.zero_grad()

            # Perform back propagation
            loss.backward()

            # Update weights and biases using ADAM
            optimizer.step()

            # Add batch loss to total loss
            tot_loss += loss.item()

        return tot_loss / (len(data_loader))

    def validating(self, data_loader, model, loss_fn):
        tot_loss = 0.0

        # Set the environment to evaluation/inference mode
        model.eval()
        with torch.inference_mode():
            # Loop through batches (with progress bar)
            for images, masks in tqdm(data_loader):
                images = images.to(DEVICE)
                masks = masks.to(DEVICE)

                # Calculate the predictions (logits)
                logits = model(images)

                # Calculate the loss
                loss = loss_fn(logits, masks)

                # Add batch loss to total loss
                tot_loss += loss.item()

        return tot_loss / (len(data_loader))

    def train(self, train_loader, validation_loader):
        try:
            # Download pretrained model
            # logger.info(f"Fetching the model")

            # ## Save model
            # model.save_pretrained(os.path.join(self.model_path, "model"))

            # logger.info(f"Model received")

            # Train model
            best_validation_loss = np.Inf
            validation_loss = None
        
            logger.info(f"Training started")

            for epoch in tqdm(range(self.EPOCHS)):
                train_loss = self.training(train_loader, self.model, optimizer=self.optimizer, loss_fn=self.loss_fn)
                validation_loss = self.validating(validation_loader, self.model, loss_fn=self.loss_fn)

                if validation_loss < best_validation_loss:
                    best_validation_loss = validation_loss
                    logger.info(f"Saving the model...")
                    torch.save(self.model.state_dict(), self.model_path)
                    logger.info(f"Model Updated")

                print(f"Iteration: {epoch}, Training loss: {train_loss}, Validation loss: {validation_loss}")
    
            logger.info(f"Training finished")

        except Exception as e:
            exception = CustomException(e, sys)
            logger.exception(exception)
            raise exception
        


       
