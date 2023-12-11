import os.path
import sys
import yaml
import base64

from PIL import Image
import random
import matplotlib.pyplot as plt
import torch

from image_segmentation.exception import CustomException
from image_segmentation.logging import logger


def read_yaml(file_path: str) -> dict:
    try:
        with open(file_path, "rb") as yaml_file:
            logger.info("Read yaml file successfully")
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise CustomException(e, sys) from e
    



def write_yaml(file_path: str, content: object, replace: bool = False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w") as file:
            yaml.dump(content, file)
            logger.info("Successfully write_yaml_file")

    except Exception as e:
        raise CustomException(e, sys)
    



def decodeImage(img_string, fileName):
    img_data = base64.b64decode(img_string)
    with open("./data/" + fileName, 'wb') as f:
        f.write(img_data)
        f.close()


def encodeImageIntoBase64(cropped_img_path):
    with open(cropped_img_path, "rb") as f:
        return base64.b64encode(f.read())


def create_directories(dirs_path: list):
    """
    creates a list of directories.

    Args:
        dirs_path (list): list of path of directories
    
    returns:
        None
    """
    for dir_path in dirs_path:
        os.makedirs(dir_path, exist_ok=True)
        logger.info(f"directory created at: {dir_path}")



def plot_transformed_images(image_paths, transform, n=2):
    """ Plots a series of random images from image_paths.

    Will open n image paths from image_paths, transform them
    with transform and plot them side by side.

    Args:
        image_paths (list): List of target image paths. 
        transform (PyTorch Transforms): Transforms to apply to images.
        n (int, optional): Number of images to plot. Defaults to 3.
        seed (int, optional): Random seed for the random generator. Defaults to 42.
    """
    random_image_paths = random.sample(image_paths, k=n)
    for image_path in random_image_paths:
        with Image.open(image_path) as f:
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,5))
            ax1.imshow(f) 
            ax1.set_title(f"Original \nSize: {f.size}")
            ax1.axis("off")

            # Transform and plot image
            # Note: permute() will change the shape of the image to suit matplotlib 
            # (PyTorch default is [C, H, W] but Matplotlib is [H, W, C])
            transformed_image = transform(f).permute(1, 2, 0) 
            ax2.imshow(transformed_image) 
            ax2.set_title(f"Transformed \nSize: {transformed_image.shape}")
            ax2.axis("off")

def plot_prediction(image, pred_image): 
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,5))

    ax1.imshow(image.permute(1,2,0), cmap = 'gray')
    ax1.axis("off")
    ax1.set_title('Image')

    ax2.imshow(pred_image.squeeze(dim=0).detach().cpu().permute(1,2,0), cmap = 'gray')
    ax2.axis("off")
    ax2.set_title('Segmented Image')
    plt.show()


      

def check_accuracy(loader, model, device="cuda"):
    num_correct = 0
    num_pixels = 0
    dice_score = 0
    model.eval()

    with torch.no_grad():
        for x, y in loader:
            x = x.to(device)
            y = y.to(device).unsqueeze(1)
            preds = torch.sigmoid(model(x))
            preds = (preds > 0.5).float()
            num_correct += (preds == y).sum()
            num_pixels += torch.numel(preds)
            dice_score += (2 * (preds * y).sum()) / (
                (preds + y).sum() + 1e-8
            )

    print(
        f"Accuracy {num_correct / num_pixels * 100:.2f}"
    )
    print(f"Dice score: {dice_score / len(loader)}")

    model.train()


# def save_predictions_as_imgs(
#     loader, model, folder="saved_images/", device="cuda"
# ):
#     model.eval()
#     for idx, (x, y) in enumerate(loader):
#         x = x.to(device=device)
#         with torch.no_grad():
#             preds = torch.sigmoid(model(x))
#             preds = (preds > 0.5).float()
#         torchvision.utils.save_image(
#             preds, f"{folder}/pred_{idx}.png"
#         )
#         torchvision.utils.save_image(y.unsqueeze(1), f"{folder}{idx}.png")

#     model.train()