
#If you get CUDA out of memory adjust subdivisions above!
#adjust max batches down for shorter training above


./darknet detector train /content/drive/MyDrive/veryTrueOcrData.data cfg/custom-yolov4-detector.cfg yolov4.conv.137 -dont_show -map

