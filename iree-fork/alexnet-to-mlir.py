# based on: https://pytorch.org/hub/pytorch_vision_alexnet/
# and: https://github.com/iree-org/iree-turbine/blob/28e39d1e37d3eac1f89829f8fdd5f6b036415246/examples/aot_mlp/mlp_export_simple.py#L36
import shark_turbine.aot as aot
import torch
import numpy as np
model = torch.hub.load('pytorch/vision:v0.10.0', 'alexnet', pretrained=True)
model.eval() # set this model up for INFERENCE, not training!

# Download an example image from the pytorch website
# import urllib
# url, filename = ("https://github.com/pytorch/hub/raw/master/images/dog.jpg", "dog.jpg")
# try: urllib.URLopener().retrieve(url, filename)
# except: urllib.request.urlretrieve(url, filename)

# ^^^ commenting out the above because we will use local images instead!
filename = './iree-fork/pics/dog.jpg'
filename2 = './iree-fork/pics/cactus-by-mathias-reding-from-unsplash.jpg'

# preprocess the images to prepare them to be input to alexnet
# preprocess dog
from PIL import Image
from torchvision import transforms
input_image = Image.open(filename)
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])
input_tensor = preprocess(input_image)
input_batch = input_tensor.unsqueeze(0) # create a mini-batch as expected by the model
# preprocess cactus
input_image2 = Image.open(filename2)
preprocess2 = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])
input_tensor2 = preprocess(input_image2)
input_batch2 = input_tensor2.unsqueeze(0) # create a mini-batch as expected by the model

# export the model to MLIR with an example input (I think input_batch is just used an example input???)
exported = aot.export(model, input_batch)
# exported.print_readable() # print MLIR output to console
exported.save_mlir("./iree-fork/out/alexnet-as-mlir.mlir")
# save the example output to a file
filepath = "./iree-fork/out/alexnet-ex-input.npy"
np.save(filepath, input_batch2)
# save the correct output on ex file
golden = model(input_batch2)
f = open('./iree-fork/out/alexnet-golden.txt', 'w')
f.write(str(golden))
f.close()



