#set the folders and files paths to avoid heavy calls in the functions
annotatins_path = "C:~\\Desktop\\ocr\\annotations"            #folder that will contain annotations in ocr


def generate_annotation(image_files_path):
    '''For every single image, this function will produce a tesseract annotation that labels each letter in the word (bounding boxes)'''
    
    try:
        # words that have no characters recognized
        error_words = []
        words_written_counter = 0
        
        # output file into which bounding boxes are written
        f = open("C:\\Users\\Light\\Desktop\\ocr\\annotations\\annotations.txt","w+")  #write the annotations txt file
        for filename in tqdm(os.listdir(image_files_path)): #tqdm allows to estimate to progess in runtime. It can be important
            try:
                img = cv2.imread(f'{image_files_path}/{filename}') #read the image at this exact location
                h, w, _ = img.shape #assumes color image

                # run tesseract, returning the bounding boxes
                boxes = pytesseract.image_to_boxes(img, lang='eng') #include and adapt any configuration options you use

                if (len(boxes.splitlines()) == 0):
                    error_words.append(filename.split('.')[0])
                else:
                    # draw the bounding boxes on the image
                    f.write('\n')
                    for b in boxes.splitlines():
                        f.write(filename + ' ' + str(b) + '\n')  #label
                        words_written_counter = words_written_counter + 1
                    if (words_written_counter % 500 == 0):       #to keep track on the tqdm progress in the labelling
                        print(words_written_counter , 'Files Processed Successfully')
                        
            except Exception as runtime_except:                  #in case of errors in the loop try
                print(f' handling error in loop try: exception in generate_annotation {filename}', runtime_except)
                pass            
        f.close()
        
    except Exception as runtime_except:                          #in case of errors in the main try
            print('Handling error in main try : generate_annotation:', runtime_except)
            
            
    return(error_words, len(error_words))
