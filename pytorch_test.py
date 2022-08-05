import torch as th
import torch.nn as nn

x = th.ones((4, 4), dtype = th.float, requires_grad=True)
print(x)

y = 2 * th.sin(x) * x
print(y)

g = th.rand((4, 4))
print(g)

y.backward(g)
print("torch grad")
print(x.grad)

def bwd(x1, grd1):
    v = grd1 * (2 * th.cos(x1) * x + 2 * th.sin(x1))
    return v

print("self grad")
print(bwd(x, g))