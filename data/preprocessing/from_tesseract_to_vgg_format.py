#set the folders and files paths to avoid heavy calls in the functions
vgg = "C:\Users\Light\Desktop\ocr\vgg\vgg.txt"                         #file containing vgg annotations 
annotations = "C:\Users\Light\Desktop\ocr\annotations.txt" #file containing images annotations 


def convert_tesseract_to_vgg(annotations, vgg, encoding = 'latin1'):
    ''' This will help in converting from tesseract annotation to vgg annotation. 
        The target format is: Anesthetist.png,1076,"{}",11,1,"{""name"":""rect"",""x"":10,""y"":8,""width"":17,""height"":22}","{""name"":""A""}" 
        The source format is: Anesthetist.png A 10 8 17 22 0'''
    
    # holds all the lines for a word, one line for each character
    lines = ""
    title = ""
    
    #number of letters in the word
    letter_counter = 1
    
    #number of exceptions
    error_counter = 0
    outputfile = codecs.open(vgg, 'w', encoding = 'utf-8') #write file that will contain the vgg annotations 
    errorfile = codecs.open('errors_in_to_vgg.txt', 'w', encoding = 'utf-8') #file that will contain errors in case
    
    # header for the file
    title_words = ['filename',
                   'file_size',
                   'file_attributes',
                   'region_count',
                   'region_id',
                   'region_shape_attributes',
                   'region_attributes']
    
    for word in title_words:
        title = title + word + ','
    title = title + '\n'    
    outputfile.write(title)
    
    for each_line in open(annotations, "r", encoding =  'utf-8'):
        try:        
            if (each_line == "\n"):      #If empty line, then new word begining and write the previous word to file
                if len(lines) > 0:
                    lines = lines.replace("$", str(letter_counter-1)) # $ is the place holder for number of letters
                    letter_counter = 1               # reset letter counter
                    outputfile.write(lines)          # write all the lines (one for each letter) 
                    outputfile.write("\n")           # write new line
                    lines = ""                       # reset the lines for next word to empty
            else:
                # single word file name
                if len(each_line.split(' '))  == 7:
                    filename, letter, x, y, width, height, _ = each_line.split(' ') # not working for multiline words
                    
                #double word filen name
                elif len(each_line.split(' ')) == 8:
                    filenamew1, filenamew2, letter, x, y, width, height, _ = each_line.split(' ')
                    filename = filenamew1 + ' ' + filenamew2
                    
                #three words file name
                elif len(each_line.split(' ')) == 9:
                    filenamew1, filenamew2, filenamew3, letter, x, y, width, height, _ = each_line.split(' ')
                    filename = filenamew1 + ' ' + filenamew2 + ' ' + filenamew3
                 
                # file size is set to dummy value of 1076
                lines = lines + filename + "," + "1076,\"{}\"," + "$," + str(letter_counter) + "," + "\"{\"\"name\"\":" + "\"\"rect\"\","+ "\"\"x\"\"" + ":" + str(x) + ",\"\"y\"\"" + ":" + str(y) + ",\"\"width\"\"" + ":" + str(width) + ",\"\"height\"\"" + ":" + str(height) + "}\",\"{\"\"name\"\":" + "\"\"" + str(letter) + "\"\"}\"" +"\n"
                letter_counter = letter_counter + 1
                
        except Exception as runtime_except:        #in case of errors 
            print(each_line)
            errorfile.write(each_line)            
            print('error in converting to vgg for line:', each_line)
            error_counter = error_counter + 1
            print(runtime_except)
            pass
        
    errorfile.close()
    return(error_counter)




#converting the vgg.txt file in to .csv

read_file = pd.read_csv (r"C:\Users\Light\Desktop\ocr\vgg\vgg.txt")
read_file.to_csv (r'C:\Users\Light\Desktop\ocr\vgg\vgg.csv', index=None)
