import torch
from torch import nn
from image_segmentation.utils.constants import DEVICE

class DoubleConv(nn.Module):
  def __init__(self, in_c, out_c):
    super(DoubleConv, self).__init__()

    self.layers = nn.Sequential(
      nn.Conv2d(in_channels=in_c, out_channels=out_c, kernel_size=3, padding=1, device=DEVICE),
      nn.ReLU(),
      nn.Dropout2d(p=0.2),
      nn.Conv2d(in_channels=out_c, out_channels=out_c, kernel_size=3, padding=1, device=DEVICE),
      nn.ReLU(),
    )

  def forward(self, x):
    return self.layers(x)

class SegmentationModel(nn.Module):
  def __init__(self, in_channels, out_channels, channels):
    super(SegmentationModel, self).__init__()

    self.encodes = nn.ModuleList()
    self.decodes = nn.ModuleList()

    self.max_pool = nn.MaxPool2d(kernel_size=2)

    # Encoders
    for channel in channels:
      self.encodes.append(DoubleConv(in_channels, channel))
      in_channels = channel

    # Decoders
    for channel in channels[::-1]:
      self.decodes.append(nn.ConvTranspose2d(in_channels=channel*2, out_channels=channel, kernel_size=2, stride=2, padding=0, device=DEVICE))
      self.decodes.append(DoubleConv(channel * 2, channel))

    # Last encoder layer
    self.bottleneck = DoubleConv(channels[-1], channels[-1] * 2)

    # Prediction layer
    self.final = nn.Conv2d(channels[0], out_channels, kernel_size=1)

  def forward(self, x):
    # Encoder
    skip_connections = []
    for encode in self.encodes:
      x = encode(x)
      skip_connections.append(x)
      x = self.max_pool(x)

    x = self.bottleneck(x)
    skip_connections = skip_connections[::-1]

    # Decoder
    for i in range(0, len(self.decodes), 2):
      x = self.decodes[i](x)
      skip_connection = skip_connections[i // 2]
      x = torch.cat((skip_connection, x), dim=1)
      x = self.decodes[i + 1](x)

    logits = self.final(x)

    return logits