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
    


#RUN apt-get install jupyter -y


#clone myUNET repository
RUN git clone https://github.com/AlexeyAB/darknet.git



#get into darknet folder
WORKDIR mekeneocr 

#install the requirements file to secondDocker folder 
#install tqdm 
RUN pip3 install tqdm

