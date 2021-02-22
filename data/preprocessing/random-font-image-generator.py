''' 
@uthor: Me_teor21
D@te: 11/12/20 4:35 pm

'''



from PIL import Image, ImageDraw, ImageFont
from tqdm import tqdm
import numpy as np
import pandas as pd
import os 
import codecs 


error_path = "/mekeneocr/computer-vision-ocr/errors"
images = "/mekeneocr/computer-vision-ocr/lesmultifonts/algerian"


def create_images(corpus, images):
    with open(corpus, 'r') as f:
        fl = f.readlines()
        fl = tqdm(fl)
        
        fnt = ImageFont.truetype(r'/mekeneocr/computer-vision-ocr/thefonts/algerian.ttf')
        
        with open(error_path + 'erreurdimages.txt', 'w') as errofile:
            
            for l in fl:
                
                if (len(l) <= 10):
                    img = Image.new('RGB', (150, 40), color = (255,255,255))
                else:
                    img = Image.new('RGB', (300, 40), color = (255,255,255))
                    d = ImageDraw.Draw(img)
                    
                    word = l.rstrip()
                    d.multiline_text((10,10), word, fill = 'black', spacing = 0, align = 'right', font = fnt)
                    
                    img.save(f'{images}/{word}.png')
                    
                    

                    
def main():
    create_images('/mekeneocr/computer-vision-ocr/txt-algerian.txt', images)
    
if __name__ == "__main__":
    main()
    
    
    
