import os

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader

import numpy as np

class AI(nn.Module):
    """
    the AI which playes abalone
    """
    #counstactor
    lstm = nn.LSTM()

    #train

    #save model

    def save(self):
        """
        saves the model
        """
        torch.save(model.state_dict(), 'large_variables\AI')

    #load model
    def load_model(self):
        """
        loads the model for use
        """
        model = AI()
        model.load_state_dict(torch.load('large_variables\AI'))
        model.eval()

model = AI()
