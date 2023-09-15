import json
import base64
from PIL import Image 

import os
 
# Get the list of all images
path = "/home/santhosh/NPS/JsonImage/Pimages"
img_list = os.listdir(path)

# reading parent json
with open('sample.json')as file:
    data = json.load(file)

for image in img_list:
    
    # converting image into base64
    with open("image.jpg", "rb") as img_file:
        my_string = base64.b64encode(img_file.read())
        print(my_string)

    
    
    with open(('/home/santhosh/NPS/JsonImage/output/json/%s.json')%(image),'w+')as f:
        data['imageData'] = my_string        
        json.dump(data,f, indent=2)


























    # # getting image data
    # # p = data['flags']['points']
    # x1,y1 = [18,48]
    # x2,y2 = [1080,650]
        

    # # print(data['imageData'])
    # img_data = data['imageData']
    # print(type(img_data))
    
    # encoded_data = img_data



    
    
    # img = Image.open(r"image.jpg") 
    
    
    # left = 0
    # top = 50
    # right = 510
    # bottom = 292
    
    # print(img.size)
    # img_res = img.crop((x1 , y1, x2, y2)) 
    
    
    # # img_res.show() 
    # img_res.save(('/home/santhosh/NPS/JsonImage/output/croppedImage/%s.jpg'%(n)))








    # # 64 to image
    # #decode base64 string data
    # decoded_data=base64.b64decode((encoded_data))

    # #write the decoded data back to original format in  file
    # img_file = open('image.jpg', 'wb')

    # img_file.write(decoded_data)
    # img_file.close()


