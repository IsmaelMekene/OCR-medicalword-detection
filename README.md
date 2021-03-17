# OCR-medicalword-detection
## Readme.md in progress ...



## Data

## Model (YOLOv4)

In this section, we implement the YOLOv4 model for training on your own dataset.

We will take the following steps to implement YOLOv4 on our custom data:

**1. Configure our GPU environment**

#### CUDA: Let's check that Nvidia CUDA drivers are already pre-installed and which version is it.

`/usr/local/cuda/bin/nvcc --version`

#### We need to install the correct cuDNN according to the previous line of code

`nvidia-smi`

#### Change the number depending on what GPU is listed above, under NVIDIA-SMI > Name.

- [ ] *Tesla K80: 30*
- [ ] *Tesla P100: 60*
- [ ] *Tesla T4: 75*


In the case of this project, we set it to: `%env compute_capability=60`

#### Then, install cuDNN according to the current CUDA version


**2. Install the Darknet YOLOv4 training environment**

#Installing Darknet for YOLOv4 

The easiest way to install YOLOv4 environment is through Darknet. 

- [x] `git clone https://github.com/roboflow-ai/darknet.git`


In this project, the darknet repository was cloned and modifications were made as mentionned in the following [shell file](https://github.com/IsmaelMekene/OCR-medicalword-detection/blob/main/model/darknet_for_YOLOv4.sh). Changes have been made to configure darknet for training.




 **3. Download our custom dataset for YOLOv4 and set up directories**
 
 The custom dataset has be loaded according the following structure.


       |__images-and-labels
       |
       |__ocrdata.data
 data__|
       |__ocrnames.names
       |
       |__train.txt
       |__valid.txt

- [x] images-and-labels: this folder contains all the images and there corresponding yolo annotation format
- [x] ocrdata.data: Inspired from the darknet repository, this file contains the infos about the number of classes, and the necessary directory paths
- [x] ocrnames.names: This file contains the classes. In the case of the this project, the classes are the character taken into account (a to z, A to Z, _ and -)
- [x] train.txt: This text file contains 80% of the total dataset, the paths of the images and labels.
- [x] valid.txt: This text file contains 20% of the total dataset, the paths of the images and labels.


**4. Configure a custom YOLOv4 training config file for Darknet**
 
Few modifications have to be made on the config file in the Darknet directory in order to set it up for the training session.
This python script [config.py](https://github.com/IsmaelMekene/OCR-medicalword-detection/blob/main/model/config_for_YOLOv4.py), explains it well.

**5. Train our custom YOLOv4 object detector**
 
The following [shell file](https://github.com/IsmaelMekene/OCR-medicalword-detection/blob/main/model/train_and_test_model_YOLOv4.sh) contains the script for training on YOLOv4.

`./darknet detector train /content/drive/MyDrive/veryTrueOcrData.data cfg/custom-yolov4-detector.cfg yolov4.conv.137 -dont_show -map`


 - **Reload YOLOv4 trained weights and make inference on test images**

When you are done you will have a custom detector that you can use. 



## Project pipeline
 

<p align="center">
  <img src="https://github.com/IsmaelMekene/OCR-medicalword-detection/blob/main/pipeline/tingy.png"/>
</p>


