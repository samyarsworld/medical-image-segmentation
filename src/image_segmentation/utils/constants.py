import torch

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
IMG_CHANNELS = 3
MASK_CHANNELS = 1