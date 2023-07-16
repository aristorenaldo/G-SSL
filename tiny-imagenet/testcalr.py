import torch

class LinearModel(torch.nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.linear = torch.nn.Linear(10,3)

    def forward(self, x):
        out = self.linear(x)
        return out
epochs = 20    
model = LinearModel()
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
lr_scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=epochs, eta_min=0, verbose=True)

for i in range(epochs):
    print('Epoch '+str(i))
    lr_scheduler.step()