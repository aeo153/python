import torch as th
import torch.nn as nn

# x = th.ones((4, 4), dtype = th.float, requires_grad=True)
# print(x)

# y = 2 * th.exp(x) * x
# print(y)

# g = th.rand((4, 4))
# print(g)

# y.backward(g)
# print("torch grad")
# print(x.grad)

# def bwd(x1, grd1):
#     v = 2 * grd1 * (th.exp(x1) * x + th.exp(x1))
#     return v

# print("self grad")
# print(bwd(x, g))

class SqueezeExcite(nn.Module):
    def __init__(self, in_ch:int, out_ch:int, se_ratio:float=0.5):
        super(SqueezeExcite, self).__init__()
        
        self.in_channel = in_ch
        self.out_channel = out_ch
        self.hidden_channel = max(1, int(self.in_channel * se_ratio))
        
        self.activation = nn.ReLU()
        self.linear = nn.Linear(self.in_channel, self.hidden_channel)
        self.linear_1 = nn.Linear(self.hidden_channel, self.out_channel)
        self.sigmoid = nn.Sigmoid()
        
    def forward(self, x):
        out = th.mean(x, (2,3))
        out = self.linear_1(self.activation(self.linear(out)))
        out = self.sigmoid(out)
        
        b,c,_,_ = x.size()
        return out.view(b,c,1,1).expand_as(x)
    
class StochDepth(nn.Module):
    def __init__(self, stochdepth_rate:float):
        super(StochDepth, self).__init__()
        self.drop_rate = stochdepth_rate
        
    def forward(self, x):
        if not self.training:
            return x
        
        batch_size = x.shape[0]
        rand_tensor = th.rand(batch_size, 1, 1, 1).type_as(x).to(x.device)
        keep_prob = 1 - self.drop_rate
        binary_tensor = th.floor(rand_tensor + keep_prob)
        print("binary_tensor")
        print(binary_tensor)
        
        return x * binary_tensor
            
    
class TstL(nn.Module):
    def __init__(self):
        super(TstL, self).__init__()
        
        self.activation = nn.ReLU()
        self.sin = th.sin
        self.sigmoid = nn.Sigmoid()
        
    def forward(self, x):        
        out = 2 * th.sin(x) * x
        return out
    
if __name__=='__main__':
    tst = StochDepth(stochdepth_rate = 0.25)
    #tst = TstL()
    # x = th.rand((2, 2), dtype = th.float, requires_grad=True)
    #x =th.tensor([[0.0992, 0.0751], [0.4912, 0.9893]], requires_grad=True)
    x = th.rand((2, 3, 4, 4), dtype = th.float, requires_grad=True)
    print("-----x-----")
    print(x)
    y = tst(x)
    print("\n-----y-----")
    print(y)
    
    g = th.rand(x.shape, dtype = th.float)
    print("\n-----gradiant-----")
    print(g)
    grd = y.backward(g)
    print("\n-----x grad-----")
    print(x.grad)