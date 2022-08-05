from pyclbr import Class
from turtle import forward
import torch as tch
import numpy as np
import torch.nn as nn
import torch.nn.functional as F

# a = tch.Tensor([[[1,2,3],[4,5,6],[7,8,9]],
#  [[10,11,12],[13,14,15],[16,17,18]]])
# print(a)
# mn = tch.mean(a,(0,1), True)
# print(mn)

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 6, 5)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 *5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = F.max_pool2d(F.relu(self.conv1(x)), (2,2))
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        # 如果是方阵,则可以只使用一个数字进行定义
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)
        x = x.view(-1, self.num_flat_features(x))
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

    def num_flat_features(self, x):
         size = x.size()[1:] # 除去批处理维度的其他所有维度
         num_features = 1
         for s in size:
             num_features *= s
         return num_features
        
if __name__ == '__main__':
    nt = Net()
    print(nt)
    params = list(nt.parameters())
    print(len(params))
    print(params[0].size())
    input = tch.randn(1, 1, 32, 32)
    # print(input)
    out = nt(input)
    target = tch.randn(10)
    target = target.view(1, -1)
    criterion = nn.MSELoss();
    loss = criterion(out, target)
    loss.backward()
    # print(out)
