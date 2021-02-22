import pandas as pd



def cleaner(corpus, authorized_alphabet):

  '''
  This function aims to clean the initial medical word corpus containing words from different languages and special characters.
  
  Input:
    corpus = '/mekeneocr/computer-vision-ocr/dico.txt', this is the path to the initial corpus
    authorized_alphabet = '/mekeneocr/computer-vision-ocr/ocrnames.names', this is the path to the desired alphabet 
  Return:
    This function returns the clean corpus with the diserd alphabet (english)
  '''


  # create an empty list 
  l = []
  # read dataset in
  with open(corpus,'r') as f:
  # read the content in list of lines
      l = f.readlines()

  # replace the newline character ("\n") by empty character
  l_no_backline = [el.replace("\n","") for el in l]
  # replace the single quotes by empty character
  l_no_quotes = [el.replace("'","") for el in l_no_backline]
  # replace the dots
  l_no_dot = [el.replace("."," ").replace(":","") for el in l_no_quotes]
  # replace special characters
  l_no_special_char = [el.replace("ö","o").\
                       replace("î","i").\
                       replace("í","i").\
                       replace("ó","o").\
                       replace("ô","o").\
                       replace("ø","o").\
                       replace("ñ","n").\
                       replace("ü","u").\
                       replace("µ","u").\
                       replace("û","u").\
                       replace("ú","u").\
                       replace("ç","c").\
                       replace("ê","e").\
                       replace("é","e").\
                       replace("è","e").\
                       replace("ë","e").\
                       replace("ä","a").\
                       replace("à","a").\
                       replace("á","a").\
                       replace("â","a").\
                       replace("ý","y").\
                       replace("(","").\
                       replace(")","").\
                       replace("[","").\
                       replace("]","").\
                       replace("&","").\
                       replace("+","").\
                       replace(",","")

                       for el in l_no_dot]
                       
  # authorized alphabet (original from Ismael)
  alphabet = list(pd.read_csv(authorized_alphabet, header=None).values.flatten())
  # extended alphabet original alphabet + space + chiffres
  for el in l_no_special_char:
      if (all(element in alphabet + [" "] + [str(el) for el in range(10)] for element in el)) is False :
          print(el)
  # new file (corrected)
  with open('/Users/assansanogo/Downloads/big_corrected.txt','a') as f:
      # iterate over elements from the list
      for line in l_no_special_char:
          # write each line in the document
          f.write(line)
          # write a line
          f.write("\n")


  return
        
        
        
        
        
#final classes        
a to z
A to Z
0 to 9
(tiret)
