# OCR-medicalword-detection





Introduction
In this notebook, we implement YOLOv4 for training on your own dataset.

We also recommend reading our blog post on Training YOLOv4 on custom data side by side.

We will take the following steps to implement YOLOv4 on our custom data:

Configure our GPU environment on Google Colab
Install the Darknet YOLOv4 training environment
Download our custom dataset for YOLOv4 and set up directories
Configure a custom YOLOv4 training config file for Darknet
Train our custom YOLOv4 object detector
Reload YOLOv4 trained weights and make inference on test images
When you are done you will have a custom detector that you can use. It will make inference like this:







<p align="center">
  <img src="https://github.com/IsmaelMekene/OCR-medicalword-detection/blob/main/pipeline/tingy.png"/>
</p>
