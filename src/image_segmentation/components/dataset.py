import torch
from torch.utils.data import Dataset
import numpy as np
import glob as glob
from PIL import Image

import os

class ImageDataset(Dataset):
  def __init__(self, base_dir: str, train=True, train_size=0.7, transform=None) -> None:
    self.base_dir = base_dir
    self.transform = transform
    self.train = train
    self.train_size = train_size

    # Get the list of training data
    train_obj = os.scandir(self.base_dir)
    train_ids = sorted([x.name for x in train_obj])
    self.image_paths = [os.path.join(self.base_dir, id, "images", id + ".png") for id in train_ids]
    index = int(np.round(self.train_size * len(self.image_paths)))

    if self.train:
      self.image_paths = self.image_paths[:index]
      self.mask_folder_paths = [os.path.join(self.base_dir, id, "masks") for id in train_ids][:index]
    else:
      self.image_paths = self.image_paths[index:]
      self.mask_folder_paths = [os.path.join(self.base_dir, id, "masks") for id in train_ids][index:]


  def combine(self, mask_folder_path):
    masks = glob(mask_folder_path + "/*.png")
    shape = np.asarray(Image.open(masks[0]).convert("L")).shape
    combined_mask = np.zeros(shape)
    for mask_path in masks:
      mask = np.asarray(Image.open(mask_path))
      combined_mask = np.maximum(combined_mask, mask)
    return combined_mask

  def load_data(self, index: int) -> Image.Image:
    img = np.asarray(Image.open(self.image_paths[index]).convert("RGB"))
    img = Image.fromarray(img.astype(np.uint8))

    mask = self.combine(self.mask_folder_paths[index])
    mask = Image.fromarray(mask.astype(np.uint8))

    return img, mask

  def __len__(self) -> int:
    return len(self.image_paths)

  def __getitem__(self, index: int) -> torch.Tensor:
    img, mask = self.load_data(index)
    # Transform if exists
    if self.transform:
      return self.transform(img), self.transform(mask)
    else:
      return img, mask