#import libraries
from paddleocr import PaddleOCR,draw_ocr
import os
import csv
from PIL import Image
import glob
from pymongo  import MongoClient
import cv2
# download and load model into memory
ocr = PaddleOCR(lang='en')

source_path = "exemples_images"
dic= {}
f= open('result.csv', 'w') 
writer = csv.writer(f)
for file in glob.glob("{}/*".format(source_path)):

    res=cv2.imread(file)
    result = ocr.ocr(res, cls=False)
    result = result[0]
    image = Image.open(file).convert('RGB')

    txts = [line[1][0] for line in result]
    dic[file]=txts
  #save text in csv file
    writer.writerow(dic[file])
        


#save text and path of image in mongodb database 
try:
    conn = MongoClient()
    print("Connected successfully!!!")
except:  
    print("Could not connect to MongoDB")
  
# database
db = conn.recog
# Created and insert the result
collection = db.result_recog
collection.insert_one(dic)
f.close()


