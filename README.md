# OCR-medicalword-detection
## Readme.md in progress ...




About the model:
## Model (YOLOv4)

In this section, we implement YOLOv4 for training on your own dataset.

We will take the following steps to implement YOLOv4 on our custom data:

 ### - Configure our GPU environment 

#### CUDA: Let's check that Nvidia CUDA drivers are already pre-installed and which version is it.

`/usr/local/cuda/bin/nvcc --version`

#### We need to install the correct cuDNN according to the previous line of code

`nvidia-smi`

#### Change the number depending on what GPU is listed above, under NVIDIA-SMI > Name.

- *Tesla K80: 30*
- *Tesla P100: 60*
- *Tesla T4: 75*

In the case of this project, we set it to: `%env compute_capability=60`

#### Then, install cuDNN according to the current CUDA version


 ### - Install the Darknet YOLOv4 training environment
 ### - Download our custom dataset for YOLOv4 and set up directories
 ### - Configure a custom YOLOv4 training config file for Darknet
 ### - Train our custom YOLOv4 object detector
 ### - Reload YOLOv4 trained weights and make inference on test images

When you are done you will have a custom detector that you can use. 



## Project pipeline
 

<p align="center">
  <img src="https://github.com/IsmaelMekene/OCR-medicalword-detection/blob/main/pipeline/tingy.png"/>
</p>


