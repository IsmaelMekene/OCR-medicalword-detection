#set the folders and files paths to avoid heavy calls in the functions
vgg_csv = "vgg.csv"
vgg_csv_path = "C:\Users\Light\Desktop\ocr\vgg\"



#this is our dictionnary: to each alphabetic character including "-"" and "_" we assign a number 
letter_to_class_map = {
  "a": "0",
  "b": "1",
  "c": "2",
  "d": "3",
  "e": "4",
  "f": "4",
  "g": "6",
  "h": "7",
  "i": "8",
  "j": "9",
  "k": "10",
  "l": "11",
  "m": "12",
  "n": "13",
  "o": "14",
  "p": "15",
  "q": "16",
  "r": "17",
  "s": "18",
  "t": "19",
  "u": "20",
  "v": "21",
  "w": "22",
  "x": "23",
  "y": "24",
  "z": "25",
  "-": "26",
  "A": "27",
  "B": "28",
  "C": "29",
  "D": "30",
  "E": "31",
  "F": "32",
  "G": "33",
  "H": "34",
  "I": "35",
  "J": "36",
  "K": "37",
  "L": "38",
  "M": "39",
  "N": "40",
  "O": "41",
  "P": "42",
  "Q": "43",
  "R": "44",
  "S": "45",
  "T": "46",
  "U": "47",
  "V": "48",
  "W": "49",
  "X": "50",
  "Y": "51",
  "Z": "52",
  "_": "53"    
}




def convert_vgg_yolo(vgg_csv, image_files_path,):
    """"This function allows to convert the vgg annotations in the csv file into a txt file following the yolo annotations"""
    
    f = open(vgg_csv_path + vgg_csv, "r", encoding='utf-8') #read the vgg annotations csv file
    
    i = 0
    newfile = True
    for line in f:
        try:
            i = i + 1
            
            #skip header
            if ( i == 1):
                continue;  

            #for new line, close current file and create new file
            #one annotation file will be created for one image file
            #in the same folder as images
            if(line == "\n"):
                output_file_.close()
                newfile = True
                continue;
            elif(newfile == True):
                filename = line.split(',')[0]
                output_file_ = codecs.open(image_files_path + filename.split(".")[0] + '.txt', 'a', encoding = 'utf-8')   #append the lines of labelling of every single letter of the word assign to the image
                newfile = True
                        
            #filename = line.split(',')[0]
            x = line.split(',')[6].split(":")[1]
            y = line.split(',')[7].split(":")[1]
            width = line.split(',')[8].split(":")[1]
            height = line.split(',')[9].split(":")[1].split('}')[0]
            obj_class = line.split(',')[10].split(":")[1][2]
            obj_class = letter_to_class_map.get(obj_class)
            x = float(x)
            y = float(y)
            width = float(width)
            height = float(height)
            print(line)
            
            img = Image.open(image_files_path + filename)
            size = img.size
            print(x, y, width, height, size[0], size[1])
            
            #Re-Dimensioning in order to fit the yolo format
            _x      = Decimal(x + width) / Decimal(2 * size[0]) # relative position of center x of rect
            _y      = Decimal(y + height) / Decimal(2 * size[1]) # relative position of center y of rect
            _width  = Decimal(width / size[0])
            _height = Decimal(height / size[1])
            
            #write in created output_file_ txt file (obj_class, round(_x, 10), round(_y, 10), round(_width, 10), round(_height, 10))
            #this is the yolo annotation format we are aiming
            output_file_.write(str(obj_class) + " " + str(round(_x, 10)) + " " + str(round(_y, 10)) + " " + str(round(_width, 10)) + " " + str(round(_height, 10)))
            output_file_.write("\n")
            print(_x, _y, _width, _height)
            
        except Exception as runtime_except:       #in case of errors 
            print('exception')
            print(runtime_except)
            print(line)
            print("{0:.10f} {0:.10f} {0:.10f} {0:.10f}".format(_x, _y, _width, _height))
            pass
    output_file_.close()
    
