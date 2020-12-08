#[author: me_teor21]
#date:08-dec-20 12:54 am


#Script Goal: it will predict the annotations and send back (letter,confidence,(x,y,w,h)) for a set of images
#run this script in cmd by locating into the darknet folder 

import cv2
import numpy as np
import glob2
from pandas import DataFrame
import darknet
import sys 
import itertools
from tqdm import tqdm

sys.path.insert(0,'/mekeneocr/myUniverse/darknet')    #puth darknet path in first place in sys (this step is very important)

config= "/mekeneocr/tiny/yolov4-tiny-custom.cfg"
data= "/mekeneocr/tiny/letters.data"
weights= "/mekeneocr/tiny/yolov4-tiny-custom_best.weights"

network, class_names, class_colors = darknet.load_network(
        config,
        data,
        weights,
        batch_size=1
    )
def image_detection(image_path, network, class_names, class_colors, thresh):
    # Darknet doesn't accept numpy images.
    # Create one with image we reuse for each detect
    width = darknet.network_width(network)
    height = darknet.network_height(network)
    darknet_image = darknet.make_image(width, height, 3)

    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_resized = cv2.resize(image_rgb, (width, height),
                               interpolation=cv2.INTER_LINEAR)

    darknet.copy_image_from_bytes(darknet_image, image_resized.tobytes())
    detections = darknet.detect_image(network, class_names, darknet_image, thresh=thresh)
    darknet.free_image(darknet_image)
    image = darknet.draw_boxes(detections, image_resized, class_colors)
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB), detections

liste = []  #create an empty list for the paths of the csv files
liste_df = [] #create an empty list for the dataframes
tiny_images = glob2.glob("/mekeneocr/tiny/tiny_images/*.png") #list all png images
for idx, thing in tqdm(enumerate(tiny_images)):   #for every images add to liste its corresponding csv file path
    #path_to_csv_thing=thing.split(".")[0] + ".csv"
    #liste.append(path_to_csv_thing)
    
    _,det = image_detection(thing, network, class_names, class_colors, 0.5)  #for every images, find its detection 

    mescoordonnees =[]   #create an empty list for the coordinates (letter, confidence, x, y, w, h)
    mesvecteurs = []     #create an empty list for the vectors 
    for i in range(len(det)):     #for every detection that has a vector
        try:                       #try this out

            filename = thing.split("/")[4]
            vector_letter = det[i][0]
            vector_confidence = det[i][1]
            vector_x = int(det[i][2][0])
            vector_y = int(det[i][2][1])
            vector_w = int(det[i][2][2])
            vector_h = int(det[i][2][3])

            mescoordonnees.append(filename)
            mescoordonnees.append(vector_letter)
            mescoordonnees.append(vector_confidence)
            mescoordonnees.append(vector_x)
            mescoordonnees.append(vector_y)
            mescoordonnees.append(vector_w)
            mescoordonnees.append(vector_h)


            mesvecteurs.append(mescoordonnees)
            mescoordonnees = []

        except:                     #otherwise print the file that detection does not have a vector
            print(thing)
    liste_df.append(mesvecteurs)
#np_liste_df = np.array(liste_df)  #make a numpy array
merged = list(itertools.chain(*liste_df))
merged_array = np.array(merged)
print(merged_array.shape)  #print its dimension

merged_frame = DataFrame(merged_array)
merged_frame.to_csv(r'/mekeneocr/tiny/mycsv.csv', sep =',', index = False, header = True)
 
