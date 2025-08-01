import os
from distutils.util import strtobool

DYNAMIC = bool(strtobool(os.getenv("DYNAMIC", "False")))
DEVICE = os.getenv("DEVICE", "cpu")

os.environ["TORCH_TRACE"] = f"backend_logs/compile_{DYNAMIC}_{DEVICE}"
# os.environ["TORCH_LOGS"] = "+inductor,dynamo"

import torch
import torch.nn as nn
# import torch_npu
import torch.nn.functional as F
torch.manual_seed(0)


class BBaseModel(nn.Module):
    def __init__(self):
        super(BBaseModel, self).__init__()

    def forward(self, x):
        x+=80.0
        if x[0, 0] == 2.0:
            x = x*x
        if x[0, 0] < 2.0:
            x = x+50.0
        else:
            x = x-50.0
        return x


if __name__ == "__main__":
    print(f"Dynamic mode: {DYNAMIC}, Device: {DEVICE}")

    model = BBaseModel().to(DEVICE)
    model = torch.compile(model, dynamic=DYNAMIC)

    input_data = torch.tensor([[1.0, 2.0, 3.0, 4.0]]).to(DEVICE)

    model.eval()
    with torch.no_grad():
        
        # print(output)
        input_data[0,0]=5.0
        output = model(input_data)
        print(output)
        output = model(input_data)
        print(output)

        input_data[0,0]=1.0
        output = model(input_data)
        print(output)
        
        input_data = torch.tensor([[1.0, 2.0],[ 3.0, 4.0]]).to(DEVICE)
        
        output = model(input_data)
        print(output)
        
