import torch

x=torch.randn(2,4)
y=torch.randn(2)

linear_layer_1= torch.nn.Linear(4,16)
linear_layer_2=torch.nn.Linear(16,1)

sequential= torch.nn.Sequential(linear_layer_1,linear_layer_2)

y=sequential(x)

