import torch

x = torch.tensor([1.0, 2.0, 3.0])

print(x)
print(x.shape)
print(x.dtype)
print(x.device)

"""
Output:
    tensor([1., 2., 3.])
    torch.Size([3])
    torch.float32
    cpu
"""


import torch

a = torch.tensor([1, 2, 3])
b = torch.tensor([4, 5, 6])

print(a+b)

# output: tensor([5, 7, 9])