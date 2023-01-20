import torch
def svg():
    U,S,V =torch.svg() 
    S = torch.diagonal(X)