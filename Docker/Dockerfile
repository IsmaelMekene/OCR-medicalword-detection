#pull ubuntu image from docker registry
FROM ubuntu:bionic 


#update the ubuntu environment
#RUN update-ca-certificates



RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive 
    #apt-get -qq install jupyter
RUN apt-get install sudo
RUN apt-get install git -y
RUN apt-get install python3-pip -y
RUN apt-get install tesseract-ocr -y
RUN apt-get install nano -y
RUN apt-get install wget -y
RUN apt-get install byobu -y 
    

#RUN apt-get update && \
#    DEBIAN_FRONTEND=noninteractive


#RUN apt-get install jupyter -y

#install sudo
#RUN apt-get install sudo

#install git
#RUN apt-get install git -y

#clone myUNET repository
#RUN git clone https://github.com/AlexeyAB/darknet.git

#install pip
#RUN apt-get install python3-pip -y



#RUN apt-get install tesseract-ocr -y 

#install nano
#RUN apt-get install nano -y

#get into darknet folder
WORKDIR mekeneocr 

#install the requirements file to secondDocker folder 
#install tqdm 
RUN pip3 install tqdm
#RUN pip3 install -r /myUNET/requirements.txt
#CMD
#ENTRYPOINT ["pip3", "install", "-r", "requirements.txt"] 
#install wget to unable downloading from public intenet links
#RUN apt-get install wget -y 

#download weights file from darknet ripo on github
#RUN wget -O yolov4.weights https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.weights
#RUN apt-get install libopencv-dev python-opencv -y
#RUN pip3 install scikit-build
#RUN pip3 install cmake 
#RUN pip3 install opencv-python 
#ENTRYPOINT /bin/bash
