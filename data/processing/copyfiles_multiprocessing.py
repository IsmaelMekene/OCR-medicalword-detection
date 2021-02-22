import multiprocessing
import pickle
import shutil 
import os

images_groupe10 = "/mekeneocr/computer-vision-ocr/images_groupe10"

def smart_copy(x):
    global images_groupe10
    
    try:
        
        shutil.copy(x, images_groupe10)
    except FileNotFoundError:
        print(x)
        #os.remove(x)


if __name__ == '__main__':
    
	with  open("/mekeneocr/computer-vision-ocr/groupe10.pkl",'rb')  as infile:
		groupe10 = pickle.load(infile)

	# create many processes
	p = multiprocessing.Pool(4)

	
	# apply in an asynchronous way the function
	res = [p.apply_async(smart_copy,args=(x,)) for x in (groupe10)]

	# get the results when done
	[el.get() for el in res]
