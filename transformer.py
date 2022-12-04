import torch
import torch.nn.functional as F

from torch import nn

import sys
import math
import random

class ScaledDotAttention(nn.Module):

    """
    Implementation of scaled fot attention as outlined in "Attention is all you need" (2017)
    """

    def __init__(self):
        super().__init__()