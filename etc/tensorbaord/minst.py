# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qLEN-Qo-E4aI0mXVJMXCM9bTirYQ9UTS
"""

# Commented out IPython magic to ensure Python compatibility.
import torch
import torchvision
import numpy as np
EPOCHS = 10
BATCH_SIZE= 64
xy_trainPT = torchvision.datasets.MNIST(root='./data', train=True, download=True,transform=torchvision.transforms.Compose([torchvision.transforms.ToTensor()]))
xy_trainPT_loader = torch.utils.data.DataLoader(xy_trainPT, batch_size=BATCH_SIZE)
def model(hidden):
    model= torch.nn.Sequential(
           torch.nn.Linear(784,hidden),
           torch.nn.Sigmoid(),
           torch.nn.Linear(hidden,10),
           torch.nn.LogSoftmax(dim=1)
           )
    return model
modelPT = model(10)
criterion = torch.nn.NLLLoss()
optimizer = torch.optim.SGD(modelPT.parameters(), lr=0.01)

from torch.utils.tensorboard import SummaryWriter
# %load_ext tensorboard

writer = SummaryWriter()
for e in range(EPOCHS):
    running_loss = 0
    for images, labels in xy_trainPT_loader:
        images = images.view(images.shape[0], -1)
        output = modelPT(images)
        loss = criterion(output, labels)
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()
        running_loss += loss.item()
    print("Epoch {} — Training loss: {}".format(e,   
           running_loss/len(xy_trainPT_loader)))
    writer.add_scalar("loss x epoch", 
           running_loss/len(xy_trainPT_loader), e)
writer.close()