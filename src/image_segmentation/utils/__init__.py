import os.path
import sys
import yaml
import base64

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



    