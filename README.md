# OCR-medicalword-detection
## Readme.md in progress ...


## Project pipeline
 
<p align="center">
  <img src="https://github.com/IsmaelMekene/OCR-medicalword-detection/blob/main/pipeline/tingy.png"/>
</p>


## Data preparation
In this section, the goal is to make the dataset ready and accessible for the YOLOv4 model.
The raw dataset is a corpus (txt file) of medical word consisted of a word or maximum two words per line. This is how it can look like:
<p align="center">
  <img src="https://github.com/IsmaelMekene/OCR-medicalword-detection/blob/main/data/Screenshot%202021-03-17%20at%2008.24.42.png"/>
</p>

For each of those words and group of words, corresponding image were generated.
Example of the word: `post-polio`, the corresponding image would be: 
<p align="left">
  <img src="https://github.com/IsmaelMekene/OCR-medicalword-detection/blob/main/data/post-polio.png"/>
</p>

And finally generate for each letter on these single image the yolo format in terms of annotations. As an example, in the case of the previous image of `post-polio`, the corresponding label would look like the following [post-polio.txt file](https://github.com/IsmaelMekene/OCR-medicalword-detection/blob/main/data/post-polio.txt):

`
cls x1           y1           x2           y2
15  0.0483333333 0.2375000000 0.0600000000 0.3750000000
14  0.0550000000 0.3000000000 0.0600000000 0.5000000000
18  0.0700000000 0.4875000000 0.0600000000 0.7750000000
19  0.0850000000 0.6125000000 0.0600000000 1.0250000000
26  0.1050000000 0.6875000000 0.0700000000 1.1750000000
15  0.1066666667 0.8250000000 0.0466666667 1.3500000000
14  0.1283333333 0.8625000000 0.0600000000 1.6250000000
11  0.1416666667 1.0500000000 0.0600000000 1.9000000000
8   0.1666666667 1.1500000000 0.0733333333 2.1000000000
14  0.1733333333 1.2875000000 0.0600000000 2.3750000000
15  0.0433333333 0.2750000000 0.0500000000 0.4500000000
14  0.0583333333 0.2750000000 0.0666666667 0.4500000000
18  0.0916666667 0.3250000000 0.1033333333 0.4500000000
19  0.1233333333 0.3250000000 0.1366666667 0.4500000000
26  0.1483333333 0.3625000000 0.1566666667 0.5250000000
15  0.1733333333 0.3250000000 0.1800000000 0.3500000000
14  0.2066666667 0.2750000000 0.2166666667 0.4500000000
11  0.2383333333 0.3250000000 0.2533333333 0.4500000000
8   0.2700000000 0.3750000000 0.2800000000 0.5500000000
14  0.3016666667 0.3250000000 0.3166666667 0.4500000000
`

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
     __|
       |__ocrnames.names
       |
       |__train.txt
       |
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

*When you are done you will have a custom detector that you can use.*

**6. Predictions: Reload YOLOv4 trained weights and make inference on test images**







