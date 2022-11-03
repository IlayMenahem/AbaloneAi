import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader

import numpy as np

import os

class AI(nn.Module):
    """
    the AI which playes abalone
    """
    #counstactor
    lstm = nn.LSTM()

    #train

    #save model

    #load model
    def load_model():
        model = TheModelClass(*args, **kwargs)
        model.load_state_dict(torch.load(PATH))
        model.eval()

model = AI()

torch.save(model.state_dict(),/large_variables)